# SAP RPT-1 Benchmarking Study

**A Comprehensive Academic Evaluation of SAP's Tabular Foundation Model**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## Overview

This repository contains a rigorous academic benchmarking study evaluating **SAP RPT-1 (ConTextTab)**, the first enterprise relational foundation model for tabular data, against state-of-the-art tabular ML approaches. This work is part of a University of Washington Master of Science in Information Management capstone project.

**Key Features:**
- 🔬 Production-ready benchmarking infrastructure with Docker isolation
- 📊 Evaluation across 70+ real-world datasets (TabArena, TabZilla, OpenML-CC18)
- 📈 Statistical rigor: Friedman tests, Nemenyi post-hoc analysis, critical difference diagrams
- 🎨 Interactive visualizations and stakeholder-ready materials
- 📝 Publication-quality documentation following REFORMS reproducibility standards

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [📄 Research Paper](2506.10707v4.pdf) | ConTextTab: Table Foundation Model for Relational Tables (SAP, 2025) |
| [💻 Web Portal](interactive/web-portal/index.html) | Interactive project dashboard |
| [🔧 Code Documentation](code/README.md) | Complete benchmarking codebase |
| [📊 Proposal](content/sap-executive-summary-v1.md) | Executive summary and methodology |
| [🤝 Stakeholder Materials](stakeholders/README.md) | SAP engagement resources |

---

## Project Structure

```
SAP-RPT1-Benchmarking/
│
├── 📂 code/                   Production benchmarking infrastructure
│   ├── docker/               5 isolated environments (Python 3.8-3.11)
│   ├── models/               sklearn-compatible model wrappers
│   ├── evaluation/           Metrics, CV, statistical tests
│   ├── datasets/             Data management & preprocessing
│   └── runners/              Experiment execution pipelines
│
├── 📂 content/               Proposal and research documentation
│   ├── sap-executive-summary-v1.md
│   ├── sap-problem-statement-v1.md
│   ├── sap-methodology-v1.md
│   └── ...                  (7 comprehensive documents)
│
├── 📂 visuals/               Professional diagrams and visualizations
│   ├── diagrams/             Mermaid + SVG system diagrams
│   ├── infographics/         Methodology & value proposition graphics
│   ├── charts/               Data visualizations
│   └── architecture/         Complete system architecture
│
├── 📂 interactive/           Web portal and interactive tools
│   ├── web-portal/           Responsive HTML/CSS/JS dashboard
│   ├── qr-codes/             Quick access codes
│   └── visualizations/       Dataset explorer, model comparison
│
├── 📂 research/              Research foundations and team data
├── 📂 stakeholders/          SAP engagement strategy & contact info
├── 📂 papers/                Academic references
├── 📂 datasets/              Dataset documentation
├── 📂 deliverables/          Final project outputs
├── 📂 Github/SAP-RPT1/      GitHub Projects automation scripts
│
├── 📂 config/                Project configuration files
│   ├── project-requirements.json
│   ├── shared-data.json
│   └── shared-data.schema.json
│
└── 2506.10707v4.pdf          SAP RPT-1 research paper
```

---

## Getting Started

### Prerequisites

- Python 3.8+ (multiple versions required for different models)
- Docker & Docker Compose
- 16GB+ RAM recommended
- CUDA-compatible GPU (optional, for faster training)

### Quick Setup

```bash
# Clone repository
git clone https://github.com/[username]/SAP-RPT1-Benchmarking.git
cd SAP-RPT1-Benchmarking

# Navigate to code directory
cd code

# Build Docker containers
docker-compose build

# Run sample experiment
docker-compose run sap-rpt1 python runners/run_experiment.py \
  --model sap_rpt1 \
  --dataset adult \
  --cv-folds 10
```

For detailed setup instructions, see [code/README_QUICKSTART.md](code/README_QUICKSTART.md).

---

## Models Evaluated

| Model | Type | Source | Python Version |
|-------|------|--------|----------------|
| **SAP RPT-1** | Foundation Model | [GitHub](https://github.com/sap/ConTextTab) | 3.11 |
| **TabPFN** | Transformer | [GitHub](https://github.com/automl/TabPFN) | 3.9+ |
| **TabICL** | In-Context Learning | [GitHub](https://github.com/microsoft/table-gpt) | 3.10 |
| **AutoGluon** | Ensemble | [GitHub](https://github.com/autogluon/autogluon) | 3.9 |
| **XGBoost** | Gradient Boosting | [GitHub](https://github.com/dmlc/xgboost) | 3.8+ |
| **LightGBM** | Gradient Boosting | [GitHub](https://github.com/microsoft/LightGBM) | 3.8+ |
| **CatBoost** | Gradient Boosting | [GitHub](https://github.com/catboost/catboost) | 3.8+ |

---

## Benchmark Datasets

- **TabArena**: 51 diverse real-world datasets
- **TabZilla**: 20 curated classification tasks
- **OpenML-CC18**: 18 standardized benchmarks

See [datasets/README.md](datasets/README.md) for complete catalog.

---

## Methodology

Our benchmarking approach follows three core pillars:

1. **Comprehensive Coverage**
   - 70+ real-world datasets spanning multiple domains
   - Classification, regression, and multi-class tasks
   - Small, medium, and large-scale data

2. **Statistical Rigor**
   - 10-fold stratified cross-validation
   - Friedman test for statistical significance
   - Nemenyi post-hoc analysis
   - Critical difference diagrams

3. **Reproducibility**
   - Docker isolation for dependency management
   - REFORMS checklist compliance
   - Comprehensive documentation
   - Open-source codebase

See [content/sap-methodology-v1.md](content/sap-methodology-v1.md) for details.

---

## Team

**University of Washington - Master of Science in Information Management**

This project leverages a multidisciplinary team with expertise in:
- AI/ML Product Strategy & Development
- Cloud & Data Engineering
- Software Engineering & AI Systems
- Operations & Analytics

See [research/team-matching.md](research/team-matching.md) for team profiles and capability mapping.

---

## Project Timeline

**Duration**: 12 weeks (January - March 2026)

- **Weeks 1-3**: Infrastructure setup, dataset acquisition, baseline experiments
- **Weeks 4-7**: SAP RPT-1 integration, full benchmark execution
- **Weeks 8-10**: Statistical analysis, results aggregation
- **Weeks 11-12**: Publication preparation, stakeholder presentation

See [visuals/diagrams/sap-project-timeline-gantt-v1.svg](visuals/diagrams/sap-project-timeline-gantt-v1.svg) for detailed Gantt chart.

---

## Stakeholder Engagement

This project includes comprehensive stakeholder engagement materials for SAP:

- **Organizational Mapping**: SAP AI Foundation team structure
- **Contact Intelligence**: Key personnel in RPT-1 product team
- **Value Propositions**: Role-specific messaging for technical and executive stakeholders
- **Outreach Playbook**: Engagement strategies and talking points

See [stakeholders/README.md](stakeholders/README.md) for complete materials.

---

## Interactive Demo

Open [interactive/web-portal/index.html](interactive/web-portal/index.html) in your browser to explore:

- Interactive team profiles with capability mapping
- 12-week project timeline visualization
- Dataset explorer (70+ datasets)
- Model comparison tools

Or scan the QR codes in [interactive/qr-codes/](interactive/qr-codes/) for quick access.

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Key areas for contribution:**
- Additional model wrappers (e.g., TabNet, FT-Transformer)
- New benchmark datasets
- Enhanced visualization tools
- Documentation improvements

---

## Reproducibility

This project follows the **REFORMS** (Reporting Standards for Machine Learning Based Science) checklist:

✅ Code availability (open-source)
✅ Data availability (public datasets)
✅ Dependency management (Docker, requirements.txt)
✅ Hyperparameter documentation (config files)
✅ Statistical testing (Friedman, Nemenyi)
✅ Results aggregation (critical difference diagrams)
✅ Compute resource documentation (see code/REPRODUCIBILITY.md)

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## Citation

If you use this benchmarking framework or results in your research, please cite:

```bibtex
@misc{sap-rpt1-benchmark-2026,
  title={Comprehensive Benchmarking of SAP RPT-1 Foundation Model for Tabular Data},
  author={University of Washington MSIM Team},
  year={2026},
  note={University of Washington Master of Science in Information Management Capstone Project}
}
```

---

## Contact

**Project Maintainer**: Rahil M. Harihar
**Email**: rahil911@uw.edu
**Institution**: University of Washington
**Program**: Master of Science in Information Management

For SAP-specific inquiries, see [stakeholders/sap-rpt1-product-team.md](stakeholders/sap-rpt1-product-team.md).

---

## Acknowledgments

- **SAP AI Foundation Team** for developing ConTextTab/RPT-1
- **University of Washington** for capstone project support
- **Open-source community** for TabPFN, TabICL, AutoGluon, and baseline model implementations

---

**Last Updated**: November 2025
**Status**: Active Development
**Version**: 1.0.0
