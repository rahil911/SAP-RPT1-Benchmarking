/**
 * SAP RPT-1 Benchmarking Project - Interactive Timeline
 *
 * Dynamically loads project timeline from shared-data.json
 * Creates an interactive timeline visualization
 */

/**
 * Load and render project timeline
 */
async function loadTimeline() {
    const container = document.getElementById('timeline-container');

    if (!container) {
        console.error('Timeline container not found');
        return;
    }

    // Show loading state
    container.innerHTML = '<div class="loading">Loading project timeline</div>';

    try {
        // Load from shared-data.json
        const response = await fetch('../../shared-data.json');

        if (!response.ok) {
            throw new Error(`Failed to load timeline: ${response.status}`);
        }

        const data = await response.json();

        if (!data.timeline || !data.timeline.phases) {
            throw new Error('Timeline data not found in shared-data.json');
        }

        console.log('✅ Timeline data loaded');
        renderTimeline(data.timeline);

    } catch (error) {
        console.error('❌ Timeline loading failed:', error);
        container.innerHTML = `
            <div class="error-message" style="padding: 2rem; background: #FEE; border: 2px solid #C00; border-radius: 8px; color: #600;">
                <h3>Unable to load timeline</h3>
                <p><strong>Error:</strong> ${error.message}</p>
            </div>
        `;
    }
}

/**
 * Render timeline from data
 * @param {Object} timelineData - Timeline data from shared-data.json
 */
function renderTimeline(timelineData) {
    const container = document.getElementById('timeline-container');

    // Clear loading state
    container.innerHTML = '';

    // Timeline header
    const header = document.createElement('div');
    header.style.cssText = 'text-align: center; margin-bottom: 2rem;';
    header.innerHTML = `
        <h2 style="color: #1E3A8A; margin-bottom: 0.5rem;">Project Timeline</h2>
        <p style="color: #64748B;">
            ${formatDate(timelineData.start_date)} - ${formatDate(timelineData.end_date)}
            <strong>(${timelineData.total_weeks} weeks)</strong>
        </p>
    `;
    container.appendChild(header);

    // Timeline visualization
    const timeline = document.createElement('div');
    timeline.className = 'timeline';

    // Render phases
    if (timelineData.phases && timelineData.phases.length > 0) {
        timelineData.phases.forEach((phase, index) => {
            const phaseElement = createTimelinePhase(phase, index);
            timeline.appendChild(phaseElement);
        });
    }

    container.appendChild(timeline);

    // Add milestones summary
    if (timelineData.milestones && timelineData.milestones.length > 0) {
        const milestonesSection = createMilestonesSection(timelineData.milestones);
        container.appendChild(milestonesSection);
    }

    console.log('✅ Timeline rendered successfully');
}

/**
 * Create a timeline phase element
 * @param {Object} phase - Phase data
 * @param {number} index - Phase index
 * @returns {HTMLElement} Phase element
 */
function createTimelinePhase(phase, index) {
    const item = document.createElement('div');
    item.className = 'timeline-item';
    item.setAttribute('data-phase-index', index);

    // Timeline marker
    const marker = document.createElement('div');
    marker.className = 'timeline-marker';
    item.appendChild(marker);

    // Timeline content
    const content = document.createElement('div');
    content.className = 'timeline-content';

    content.innerHTML = `
        <h3 style="color: #1E3A8A; margin-bottom: 0.5rem;">
            ${escapeHtml(phase.phase_name || `Phase ${index + 1}`)}
        </h3>
        <p style="color: #14B8A6; font-weight: bold; margin-bottom: 0.75rem;">
            ${escapeHtml(phase.weeks || '')}
        </p>
        <p style="color: #64748B; margin-bottom: 1rem;">
            ${escapeHtml(phase.description || '')}
        </p>
    `;

    // Deliverables list
    if (phase.deliverables && phase.deliverables.length > 0) {
        const deliverablesList = document.createElement('ul');
        deliverablesList.style.cssText = 'list-style: none; padding-left: 0; margin-top: 0.75rem;';

        const deliverablesTitle = document.createElement('p');
        deliverablesTitle.innerHTML = '<strong style="color: #1E3A8A;">Deliverables:</strong>';
        content.appendChild(deliverablesTitle);

        phase.deliverables.forEach(deliverable => {
            const li = document.createElement('li');
            li.style.cssText = 'padding-left: 1.5rem; position: relative; margin-bottom: 0.5rem;';
            li.innerHTML = `
                <span style="position: absolute; left: 0; color: #14B8A6; font-weight: bold;">✓</span>
                ${escapeHtml(deliverable)}
            `;
            deliverablesList.appendChild(li);
        });

        content.appendChild(deliverablesList);
    }

    item.appendChild(content);

    // Add hover effect
    item.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-4px)';
        this.style.transition = 'transform 0.3s ease';
    });

    item.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });

    return item;
}

/**
 * Create milestones summary section
 * @param {Array} milestones - Array of milestone objects
 * @returns {HTMLElement} Milestones section
 */
function createMilestonesSection(milestones) {
    const section = document.createElement('div');
    section.className = 'section';
    section.style.cssText = 'margin-top: 3rem;';

    section.innerHTML = '<h2 style="color: #1E3A8A; margin-bottom: 1.5rem; text-align: center;">Key Milestones</h2>';

    const grid = document.createElement('div');
    grid.className = 'overview-grid';

    milestones.forEach(milestone => {
        const card = document.createElement('div');
        card.className = 'overview-card';
        card.innerHTML = `
            <h3 style="color: #1E3A8A; margin-bottom: 0.5rem;">
                ${escapeHtml(milestone.name || 'Milestone')}
            </h3>
            <p style="color: #14B8A6; font-weight: bold; margin-bottom: 0.75rem;">
                Week ${milestone.week}
            </p>
            <p style="color: #64748B; font-size: 0.95rem;">
                ${escapeHtml(milestone.description || '')}
            </p>
        `;
        grid.appendChild(card);
    });

    section.appendChild(grid);

    return section;
}

/**
 * Format date for display
 * @param {string} dateString - ISO date string
 * @returns {string} Formatted date
 */
function formatDate(dateString) {
    if (!dateString) return '';

    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };

    return date.toLocaleDateString('en-US', options);
}

/**
 * Escape HTML to prevent XSS
 * @param {string} text - Text to escape
 * @returns {string} Escaped text
 */
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Initialize on DOM ready
 */
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadTimeline);
} else {
    loadTimeline();
}
