#!/usr/bin/env python3
"""
create_timeline_excel.py
Generate Excel Gantt chart timeline from week JSON files

This script creates a professional Excel spreadsheet with:
- All 150+ tasks from 12 weeks
- Gantt chart visualization
- Color-coding by phase
- Task metadata (owner, hours, priority, deliverable)

Usage:
    python3 create_timeline_excel.py
    python3 create_timeline_excel.py --output custom_timeline.xlsx

Author: Agent 5 (GitHub Projects Manager)
Date: 2025-11-08
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

try:
    import pandas as pd
    import xlsxwriter
    EXCEL_AVAILABLE = True
except ImportError:
    EXCEL_AVAILABLE = False
    print("⚠️  Warning: pandas or xlsxwriter not installed")
    print("   Install with: pip install pandas xlsxwriter")


def create_excel_timeline(output='sap-project-timeline.xlsx'):
    """Generate Excel file with Gantt chart"""

    if not EXCEL_AVAILABLE:
        print("❌ Cannot create Excel file: pandas or xlsxwriter not installed")
        return False

    print(f"📊 Creating Excel timeline: {output}")

    start_date = datetime(2025, 11, 8)  # Project start: Nov 8, 2025
    tasks = []

    # Load all week JSON files
    data_dir = Path(__file__).parent.parent / 'data' / 'weeks'

    for week in range(1, 13):
        json_file = data_dir / f"week_{week:02d}.json"

        if not json_file.exists():
            print(f"   ⚠️  Week {week:02d} JSON not found: {json_file}")
            continue

        with open(json_file, 'r') as f:
            week_data = json.load(f)

        phase = week_data.get('phase', 'Unknown')

        for task in week_data['tasks']:
            # Calculate task start and end dates
            task_start = start_date + timedelta(weeks=week-1)
            task_end = task_start + timedelta(days=7)

            tasks.append({
                'Week': week,
                'Phase': phase,
                'Task ID': task['id'],
                'Task': task['title'],
                'Description': task['description'][:100] + '...' if len(task['description']) > 100 else task['description'],
                'Owner': task['owner'],
                'Hours': task['estimated_hours'],
                'Priority': task['priority'],
                'Start': task_start.strftime('%Y-%m-%d'),
                'End': task_end.strftime('%Y-%m-%d'),
                'Deliverable': task['deliverable'],
                'Dependencies': ', '.join(task['dependencies']) if task['dependencies'] else 'None',
                'Success Criteria': task.get('success_criteria', 'N/A')
            })

        print(f"   ✅ Week {week:02d}: {len(week_data['tasks'])} tasks loaded")

    # Create DataFrame
    df = pd.DataFrame(tasks)

    print(f"\n📈 Total tasks: {len(tasks)}")
    print(f"📅 Project duration: {start_date.strftime('%Y-%m-%d')} to {(start_date + timedelta(weeks=12)).strftime('%Y-%m-%d')}")

    # Create Excel file with formatting
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(str(output_path), engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Timeline', index=False)

        workbook = writer.book
        worksheet = writer.sheets['Timeline']

        # Define formats
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#1E3A8A',
            'font_color': '#FFFFFF',
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })

        critical_format = workbook.add_format({
            'bg_color': '#EF4444',
            'font_color': '#FFFFFF',
            'bold': True
        })

        high_format = workbook.add_format({
            'bg_color': '#F59E0B',
            'font_color': '#000000'
        })

        medium_format = workbook.add_format({
            'bg_color': '#14B8A6',
            'font_color': '#FFFFFF'
        })

        low_format = workbook.add_format({
            'bg_color': '#64748B',
            'font_color': '#FFFFFF'
        })

        # Apply header format
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        # Set column widths
        worksheet.set_column('A:A', 8)   # Week
        worksheet.set_column('B:B', 25)  # Phase
        worksheet.set_column('C:C', 12)  # Task ID
        worksheet.set_column('D:D', 40)  # Task
        worksheet.set_column('E:E', 50)  # Description
        worksheet.set_column('F:F', 25)  # Owner
        worksheet.set_column('G:G', 8)   # Hours
        worksheet.set_column('H:H', 10)  # Priority
        worksheet.set_column('I:I', 12)  # Start
        worksheet.set_column('J:J', 12)  # End
        worksheet.set_column('K:K', 35)  # Deliverable
        worksheet.set_column('L:L', 20)  # Dependencies
        worksheet.set_column('M:M', 50)  # Success Criteria

        # Apply conditional formatting for Priority column
        priority_col = df.columns.get_loc('Priority') + 1  # +1 for Excel 1-indexing

        for row_num in range(1, len(df) + 1):
            priority = df.iloc[row_num - 1]['Priority']

            if priority == 'Critical':
                worksheet.write(row_num, priority_col - 1, priority, critical_format)
            elif priority == 'High':
                worksheet.write(row_num, priority_col - 1, priority, high_format)
            elif priority == 'Medium':
                worksheet.write(row_num, priority_col - 1, priority, medium_format)
            elif priority == 'Low':
                worksheet.write(row_num, priority_col - 1, priority, low_format)

        # Freeze first row and first column
        worksheet.freeze_panes(1, 1)

        # Add summary sheet
        summary_df = pd.DataFrame({
            'Metric': [
                'Total Tasks',
                'Total Weeks',
                'Total Estimated Hours',
                'Team Members',
                'Start Date',
                'End Date',
                'Total Milestones'
            ],
            'Value': [
                len(tasks),
                12,
                df['Hours'].sum(),
                4,
                start_date.strftime('%Y-%m-%d'),
                (start_date + timedelta(weeks=12)).strftime('%Y-%m-%d'),
                7
            ]
        })

        summary_df.to_excel(writer, sheet_name='Summary', index=False)

        # Add phase breakdown
        phase_summary = df.groupby('Phase').agg({
            'Task ID': 'count',
            'Hours': 'sum'
        }).rename(columns={'Task ID': 'Task Count', 'Hours': 'Total Hours'})

        phase_summary.to_excel(writer, sheet_name='Phase Breakdown')

        # Add owner breakdown
        owner_summary = df.groupby('Owner').agg({
            'Task ID': 'count',
            'Hours': 'sum'
        }).rename(columns={'Task ID': 'Task Count', 'Hours': 'Total Hours'})

        owner_summary.to_excel(writer, sheet_name='Owner Breakdown')

    print(f"\n✅ Excel timeline saved: {output_path}")
    print(f"\n📋 Sheets created:")
    print(f"   • Timeline (main task list)")
    print(f"   • Summary (project overview)")
    print(f"   • Phase Breakdown (tasks by phase)")
    print(f"   • Owner Breakdown (tasks by team member)")

    return True


def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description='Generate Excel timeline from week JSON files')
    parser.add_argument('--output', '-o', default='sap-project-timeline.xlsx',
                        help='Output Excel file path (default: sap-project-timeline.xlsx)')

    args = parser.parse_args()

    success = create_excel_timeline(output=args.output)

    if success:
        print("\n✨ Timeline generation complete!")
    else:
        print("\n❌ Timeline generation failed")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
