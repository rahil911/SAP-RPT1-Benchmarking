# Benchmark Datasets Repository

**Purpose**: Storage and management for all benchmark datasets
**Total Datasets**: 70+ (TabArena 51 + TabZilla 20 + OpenML subset)
**Estimated Size**: 5-10GB
**Owner**: Agent 4 (Infrastructure Engineer) or Research Agent

---

## 📁 Folder Structure

```
datasets/
├── README.md (this file)
├── tabarena/ (51 datasets)
├── tabzilla/ (20 subset)
├── openml-cc18/ (15 subset, optional)
└── metadata/
    ├── dataset_catalog.csv
    ├── dataset_statistics.json
    └── download_log.txt
```

---

## 📋 Dataset Sources

### 1. TabArena (51 datasets) - PRIMARY

**Source**: OpenML API via TabArena
**Website**: https://tabarena.ai
**GitHub**: https://github.com/autogluon/tabarena
**Type**: Living benchmark, curated real-world tasks

**Download Script** (in code/datasets/download_tabarena.py):
```python
import openml
import pandas as pd

TABARENA_TASK_IDS = [...]  # 51 task IDs from TabArena

def download_tabarena_datasets(output_dir='datasets/tabarena'):
    for task_id in TABARENA_TASK_IDS:
        task = openml.tasks.get_task(task_id)
        dataset = task.get_dataset()

        X, y, categorical_indicator, attribute_names = dataset.get_data(
            dataset_format="dataframe",
            target=dataset.default_target_attribute
        )

        # Save
        X.to_csv(f"{output_dir}/{dataset.name}_X.csv", index=False)
        y.to_csv(f"{output_dir}/{dataset.name}_y.csv", index=False)

        print(f"✅ Downloaded: {dataset.name}")
```

---

### 2. TabZilla (20 hardest subset) - EXTENDED

**Source**: GitHub repository
**GitHub**: https://github.com/naszilla/tabzilla
**Type**: "Hardest" datasets where simple baselines fail

**Download**:
```bash
cd datasets/tabzilla
git clone https://github.com/naszilla/tabzilla.git temp
cp -r temp/data/* ./
rm -rf temp
```

---

### 3. OpenML-CC18 (15 subset, OPTIONAL)

**Source**: OpenML Benchmark Suite 99
**Website**: https://www.openml.org/s/99
**Type**: Curated classification benchmark

**Download via API**:
```python
import openml

suite = openml.study.get_suite('OpenML-CC18')
for task_id in suite.tasks[:15]:  # Subset of 15
    task = openml.tasks.get_task(task_id)
    dataset = task.get_dataset()
    # Download and save...
```

---

## ✅ Download Checklist

- [ ] TabArena 51 datasets downloaded
- [ ] TabZilla 20 datasets downloaded
- [ ] OpenML-CC18 subset downloaded (optional)
- [ ] All datasets in CSV format
- [ ] Metadata catalog created (dataset_catalog.csv)
- [ ] Dataset statistics calculated
- [ ] Download log generated
- [ ] Total storage < 10GB
- [ ] All datasets readable (no corruption)

---

## 📊 Dataset Metadata Tracking

### dataset_catalog.csv

| Dataset Name | Source | Task Type | Rows | Columns | Classes | Missing % |
|--------------|--------|-----------|------|---------|---------|-----------|
| adult | TabArena | Classification | 48842 | 14 | 2 | 0% |
| ... | ... | ... | ... | ... | ... | ... |

**Created by**: code/datasets/dataset_catalog.py

---

## 🚨 Important Notes

- **Storage**: Keep datasets in .gitignore (too large for Git)
- **Caching**: Download once, use forever
- **Preprocessing**: Minimal (model-specific in code/datasets/preprocessors.py)
- **Validation**: Check file integrity after download

---

**Status**: ⏳ Download pending
**Estimated Download Time**: 2-4 hours (depending on network)
**Total Size**: 5-10GB
