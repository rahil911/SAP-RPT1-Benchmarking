## Problem Statement: Benchmarking SAP RPT (Relational Pre-trained Transformer) Models for Tabular AI

### Background

SAP recently launched RPT-1, claiming it to be the "first enterprise relational foundation model" that fundamentally changes how businesses approach predictive analytics on structured data. Unlike traditional machine learning that requires weeks of model training for each use case, or LLMs that excel at text but struggle with numerical reasoning, SAP RPT-1 promises immediate, accurate predictions on tabular business data through in-context learning - requiring only a few example records in an API call.

The model family (including sap-rpt-1-small, sap-rpt-1-large, and open-source sap-rpt-1-oss) was trained on 1.34TB of real-world tabular data and uses a transformer architecture specifically optimized for 2D table structures with semantic understanding of column names and business context.

### The Problem

While SAP has published initial research (the ConTextTab paper) and made bold claims about performance, there is currently:

1. **No independent, comprehensive benchmarking** of SAP RPT models against existing solutions in the tabular AI landscape

2. **No standardized evaluation framework** for comparing relational foundation models with traditional ML approaches, AutoML platforms, and LLM-based tabular reasoning

3. **Limited understanding** of when and where these models actually outperform conventional approaches in real enterprise scenarios

4. **No systematic analysis** of the trade-offs between zero-shot foundation models versus trained models across different business domains and data characteristics

5. **Absence of academic validation** of SAP's claims about eliminating the need for traditional ML pipelines

### Critical Questions Requiring Investigation

- Does in-context learning on tabular data truly eliminate the need for model training across diverse business prediction tasks?
- How does SAP RPT performance compare to state-of-the-art alternatives across different metrics (accuracy, speed, resource usage)?
- What are the boundary conditions - where does this approach excel versus fail?
- Can a single pre-trained model really replace hundreds of specialized ML models in enterprise settings?
- How does performance scale with table size, complexity, and domain specificity?

### Industry Context

The enterprise AI market is rapidly evolving with multiple competing approaches to tabular prediction:
- Traditional AutoML platforms (H2O.ai, DataRobot)
- Classical ML libraries (XGBoost, LightGBM) 
- Emerging tabular foundation models (TabPFN, TabICL)
- LLMs attempting structured reasoning (GPT-4, Claude)
- Specialized solutions (Kumo's graph-based approach)

Without rigorous, independent benchmarking, enterprises lack the evidence needed to make informed decisions about adopting these new foundation model approaches versus continuing with established ML practices.

### Deliverable Requirement

An academic-quality benchmarking study that provides objective, reproducible evaluation of SAP RPT models in the context of enterprise tabular AI, with sufficient rigor for peer review and practical relevance for industry adoption decisions.