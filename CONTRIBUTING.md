# Contributing to SAP RPT-1 Benchmarking Study

Thank you for your interest in contributing to this academic benchmarking project! This document provides guidelines for contributing code, documentation, and other improvements.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Testing Requirements](#testing-requirements)
- [Documentation Standards](#documentation-standards)
- [Pull Request Process](#pull-request-process)
- [Contact](#contact)

---

## Code of Conduct

This project adheres to academic standards of integrity, collaboration, and respect. By participating, you agree to:

- Maintain professional and respectful communication
- Provide constructive feedback
- Respect diverse perspectives and experiences
- Follow proper attribution and citation practices
- Uphold reproducibility standards

---

## Getting Started

### Prerequisites

Before contributing, ensure you have:

1. **Development Environment**:
   - Python 3.8+ (recommend pyenv for version management)
   - Docker & Docker Compose
   - Git

2. **Repository Setup**:
   ```bash
   # Fork the repository on GitHub

   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/SAP-RPT1-Benchmarking.git
   cd SAP-RPT1-Benchmarking

   # Add upstream remote
   git remote add upstream https://github.com/ORIGINAL_OWNER/SAP-RPT1-Benchmarking.git

   # Install development dependencies
   cd code
   pip install -r requirements-dev.txt  # if exists
   ```

3. **Code Structure Understanding**:
   - Read [code/README.md](code/README.md)
   - Review [code/REPRODUCIBILITY.md](code/REPRODUCIBILITY.md)
   - Explore existing model wrappers in `code/models/`

---

## Development Workflow

### Branching Strategy

We follow a feature branch workflow:

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes, commit, and push
git add .
git commit -m "Descriptive commit message"
git push origin feature/your-feature-name
```

### Branch Naming Conventions

- `feature/` - New features (e.g., `feature/add-tabnet-wrapper`)
- `fix/` - Bug fixes (e.g., `fix/cross-validation-stratification`)
- `docs/` - Documentation updates (e.g., `docs/update-reproducibility-guide`)
- `refactor/` - Code refactoring (e.g., `refactor/model-wrapper-base-class`)
- `test/` - Test additions/fixes (e.g., `test/add-statistical-tests`)

---

## Contribution Guidelines

### Types of Contributions

We welcome the following contributions:

#### 1. Model Wrappers

Add new tabular ML models to the benchmark suite.

**Requirements**:
- Inherit from `code/models/base_wrapper.py:BaseModelWrapper`
- Implement sklearn-compatible API (`fit`, `predict`, `predict_proba`)
- Include Dockerfile with dependencies
- Add model configuration to `code/config/models.yaml`
- Document hyperparameters and training time

**Example**:
```python
# code/models/tabnet_wrapper.py
from models.base_wrapper import BaseModelWrapper
from pytorch_tabnet.tab_model import TabNetClassifier

class TabNetWrapper(BaseModelWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = TabNetClassifier(**kwargs)

    def fit(self, X, y):
        # Implementation
        pass

    def predict(self, X):
        # Implementation
        pass
```

#### 2. Dataset Integration

Add new benchmark datasets.

**Requirements**:
- Add download script to `code/datasets/`
- Update `code/datasets/dataset_catalog.py`
- Include dataset metadata (rows, columns, task type, domain)
- Provide preprocessing steps
- Document data source and license

#### 3. Evaluation Metrics

Enhance evaluation capabilities.

**Requirements**:
- Add metric to `code/evaluation/metrics.py`
- Follow sklearn metric conventions
- Include unit tests
- Update documentation

#### 4. Visualizations

Improve result visualization and reporting.

**Requirements**:
- Add to `code/analysis/` or `interactive/visualizations/`
- Use design system colors (Navy #1E3A8A, Slate #64748B, Teal #14B8A6)
- Ensure responsiveness for web-based visualizations
- Include usage examples

#### 5. Documentation

Improve project documentation.

**Requirements**:
- Use Markdown format
- Follow existing documentation structure
- Include code examples where applicable
- Check spelling and grammar

---

## Testing Requirements

### Code Quality

All code contributions must:

1. **Pass Linting**:
   ```bash
   # Run flake8
   flake8 code/ --max-line-length=100

   # Run black (code formatting)
   black code/ --check
   ```

2. **Include Type Hints** (Python 3.8+):
   ```python
   from typing import List, Dict, Optional

   def process_data(X: pd.DataFrame, y: pd.Series) -> Dict[str, float]:
       # Implementation
       pass
   ```

3. **Pass Unit Tests**:
   ```bash
   # Run pytest
   cd code
   pytest tests/ -v
   ```

### Model Wrapper Testing

New model wrappers must pass:

```python
# tests/test_model_wrappers.py
def test_model_wrapper(model_class):
    # Test sklearn API compliance
    X, y = load_sample_dataset()
    model = model_class()

    # Test fit
    model.fit(X, y)

    # Test predict
    predictions = model.predict(X)
    assert len(predictions) == len(y)

    # Test predict_proba (for classifiers)
    probabilities = model.predict_proba(X)
    assert probabilities.shape == (len(y), num_classes)
```

---

## Documentation Standards

### Code Documentation

Use Google-style docstrings:

```python
def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray,
                     task_type: str = 'classification') -> Dict[str, float]:
    """Calculate evaluation metrics for predictions.

    Args:
        y_true: Ground truth labels
        y_pred: Predicted labels
        task_type: Type of ML task ('classification' or 'regression')

    Returns:
        Dictionary mapping metric names to values

    Raises:
        ValueError: If task_type is not supported

    Example:
        >>> metrics = calculate_metrics(y_true, y_pred, 'classification')
        >>> print(metrics['accuracy'])
        0.92
    """
    # Implementation
    pass
```

### README Updates

When adding new features, update relevant READMEs:

- Main [README.md](README.md) - For major features
- [code/README.md](code/README.md) - For code changes
- Specific directory READMEs - For localized changes

---

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass**:
   ```bash
   pytest tests/ -v
   flake8 code/
   black code/ --check
   ```

2. **Update documentation**:
   - Add/update docstrings
   - Update READMEs if needed
   - Add examples to documentation

3. **Verify reproducibility**:
   - Test in Docker container
   - Document any new dependencies
   - Update requirements.txt

### PR Submission

1. **Create Pull Request** on GitHub with:
   - **Title**: Concise description (e.g., "Add TabNet model wrapper")
   - **Description**:
     - What changed
     - Why this change is needed
     - How to test the change
     - Related issues (if any)

2. **PR Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] New feature
   - [ ] Bug fix
   - [ ] Documentation update
   - [ ] Refactoring

   ## Testing
   - [ ] All existing tests pass
   - [ ] Added new tests for changes
   - [ ] Tested in Docker environment

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented if unavoidable)
   ```

3. **Review Process**:
   - At least one maintainer review required
   - Address reviewer feedback
   - Squash commits if requested
   - Maintain clean git history

### After Merge

- Delete your feature branch
- Update your local main branch
- Close related issues

---

## Project-Specific Guidelines

### Reproducibility Standards

All contributions must maintain REFORMS compliance:

- **R**eporting standards
- **E**valuation methodology
- **F**air comparison
- **O**pen-source code
- **R**esource documentation
- **M**ethodology clarity
- **S**tatistical rigor

See [code/REPRODUCIBILITY.md](code/REPRODUCIBILITY.md) for details.

### Design System Compliance

Visual contributions (diagrams, charts, web portal) must use:

**Colors**:
- Navy Blue: `#1E3A8A` (headings, primary)
- Slate Gray: `#64748B` (body text, secondary)
- Teal: `#14B8A6` (accents, highlights)

**Typography**:
- Font: Helvetica Neue, Arial, sans-serif
- Maintain 40-50% white space

---

## Areas for Contribution

### High Priority

- **Additional Models**: TabNet, FT-Transformer, SAINT, etc.
- **Compute Optimization**: GPU acceleration, distributed training
- **Statistical Tests**: Additional significance tests, effect size calculations
- **Interactive Dashboards**: Real-time experiment monitoring

### Medium Priority

- **Dataset Coverage**: Domain-specific benchmarks (healthcare, finance, etc.)
- **Visualization Enhancements**: Critical difference diagrams, performance profiles
- **Documentation**: Video tutorials, detailed guides
- **Cloud Integration**: AWS SageMaker, Azure ML, GCP Vertex AI

### Low Priority

- **Code Refactoring**: Performance optimizations, code cleanup
- **Testing**: Increase test coverage
- **CI/CD**: GitHub Actions workflows

---

## Questions and Support

### Getting Help

- **Documentation**: Start with [code/README.md](code/README.md)
- **Issues**: Check existing [GitHub Issues](https://github.com/OWNER/SAP-RPT1-Benchmarking/issues)
- **Email**: rahil911@uw.edu for project-specific questions

### Reporting Issues

When reporting bugs or requesting features:

1. **Check existing issues** first
2. **Provide detailed information**:
   - Python version
   - Operating system
   - Exact error message
   - Steps to reproduce
3. **Use appropriate labels**:
   - `bug` - Something isn't working
   - `enhancement` - New feature request
   - `documentation` - Documentation improvements
   - `question` - Further information requested

---

## Attribution

Contributors will be acknowledged in:

- Project README
- Academic publication acknowledgments
- GitHub contributor list

All contributions must respect:
- Original author attribution
- Academic citation practices
- Open-source license terms (MIT)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

See [LICENSE](LICENSE) for full license text.

---

## Thank You!

Thank you for contributing to advancing tabular ML benchmarking research! Your contributions help make this project more robust, reproducible, and valuable to the research community.

---

**Last Updated**: November 2025
**Maintainer**: Rahil M. Harihar (rahil911@uw.edu)
