# Research Papers Repository

**Purpose**: Central repository for all research papers related to the SAP RPT-1 benchmarking project
**Owner**: Research Agent (Phase 0) or manual download
**Status**: ⏳ Download in progress

---

## 📋 Required Papers (7 Papers)

### 1. ConTextTab / SAP RPT-1 (NeurIPS 2025) ✅

**Status**: ✅ Already Downloaded
**File**: `2506.10707v4.pdf`
**Location**: `/Users/rahilharihar/TBD-Sponsers/SAP/2506.10707v4.pdf` (root folder)
**Title**: "ConTextTab: A Semantics-Aware Tabular In-Context Learner"
**Authors**: Marco Spinaci, Marek Polewczyk, Maximilian Schambach, Sam Thelin (SAP)
**Conference**: NeurIPS 2025
**arXiv**: https://arxiv.org/abs/2506.10707
**Size**: Check existing file

**Action**: Move to papers/ folder
```bash
mv /Users/rahilharihar/TBD-Sponsers/SAP/2506.10707v4.pdf /Users/rahilharihar/TBD-Sponsers/SAP/papers/ConTextTab_SAP_RPT1_NeurIPS2025.pdf
```

---

### 2. TabPFN (Nature 2025) ⏳

**File**: `TabPFN_Nature_2025.pdf`
**Title**: "Accurate predictions on small data with a tabular foundation model"
**Authors**: Noah Hollmann, Samuel Müller, Frank Hutter
**Journal**: Nature (January 2025)
**DOI**: https://doi.org/10.1038/s41586-024-08328-6
**arXiv**: https://arxiv.org/abs/2207.01848

**Download**:
```bash
# From arXiv (open access)
wget https://arxiv.org/pdf/2207.01848.pdf -O papers/TabPFN_Nature_2025.pdf
```

**Alternative**: Nature paywall - use institution access or arXiv version

---

### 3. TabICL (ICML 2025) ⏳

**File**: `TabICL_ICML_2025.pdf`
**Title**: "Scalable Tabular In-Context Learning"
**Authors**: SODA-INRIA Team
**Conference**: ICML 2025
**arXiv**: (Search for TabICL ICML 2025)
**GitHub**: https://github.com/soda-inria/tabicl

**Download**:
```bash
# Check arXiv for latest version
# Or download from ICML proceedings when published
```

**Note**: If not yet on arXiv, use GitHub README and documentation

---

### 4. TabArena (arXiv 2025) ⏳

**File**: `TabArena_2025.pdf`
**Title**: "TabArena: A Living Benchmark for Tabular Prediction"
**Authors**: AutoGluon Team
**Source**: arXiv 2025
**arXiv ID**: 2506.16791v2
**URL**: https://arxiv.org/abs/2506.16791

**Download**:
```bash
wget https://arxiv.org/pdf/2506.16791.pdf -O papers/TabArena_2025.pdf
```

---

### 5. TabZilla (NeurIPS 2023) ⏳

**File**: `TabZilla_NeurIPS_2023.pdf`
**Title**: "TabZilla: A Large-Scale Tabular Benchmark Suite"
**Authors**: Multiple authors
**Conference**: NeurIPS 2023 Datasets and Benchmarks Track
**arXiv**: https://arxiv.org/abs/2305.02997
**GitHub**: https://github.com/naszilla/tabzilla

**Download**:
```bash
wget https://arxiv.org/pdf/2305.02997.pdf -O papers/TabZilla_NeurIPS_2023.pdf
```

---

### 6. TALENT (Multiple Papers) ⏳

**File**: `TALENT_Toolkit.pdf`
**Title**: "TALENT: A Tabular Learning Toolkit"
**Authors**: LAMDA-Tabular Team
**Source**: GitHub + arXiv
**GitHub**: https://github.com/LAMDA-Tabular/TALENT
**arXiv**: (Search for TALENT tabular)

**Download**:
```bash
# Check GitHub for paper links
# Download main paper if available
```

---

### 7. AutoGluon Tabular Papers ⏳

**File**: `AutoGluon_Tabular.pdf`
**Title**: "AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data"
**Authors**: AWS AI Labs
**Source**: arXiv + GitHub
**arXiv**: https://arxiv.org/abs/2003.06505 (original)
**GitHub**: https://github.com/autogluon/autogluon

**Download**:
```bash
wget https://arxiv.org/pdf/2003.06505.pdf -O papers/AutoGluon_Tabular.pdf
```

---

## 🤖 Automated Download Script

### download_papers.sh

```bash
#!/bin/bash
# Automated paper download script

cd /Users/rahilharihar/TBD-Sponsers/SAP/papers

echo "📥 Downloading research papers..."

# 1. ConTextTab (move existing)
if [ -f "../2506.10707v4.pdf" ]; then
    mv ../2506.10707v4.pdf ConTextTab_SAP_RPT1_NeurIPS2025.pdf
    echo "✅ ConTextTab moved from root"
else
    wget https://arxiv.org/pdf/2506.10707.pdf -O ConTextTab_SAP_RPT1_NeurIPS2025.pdf
    echo "✅ ConTextTab downloaded"
fi

# 2. TabPFN
wget https://arxiv.org/pdf/2207.01848.pdf -O TabPFN_Nature_2025.pdf
echo "✅ TabPFN downloaded"

# 3. TabArena
wget https://arxiv.org/pdf/2506.16791.pdf -O TabArena_2025.pdf
echo "✅ TabArena downloaded"

# 4. TabZilla
wget https://arxiv.org/pdf/2305.02997.pdf -O TabZilla_NeurIPS_2023.pdf
echo "✅ TabZilla downloaded"

# 5. AutoGluon
wget https://arxiv.org/pdf/2003.06505.pdf -O AutoGluon_Tabular.pdf
echo "✅ AutoGluon downloaded"

echo ""
echo "📊 Download Summary:"
ls -lh *.pdf

echo ""
echo "✅ All papers downloaded to $(pwd)"
```

**Usage**:
```bash
chmod +x papers/download_papers.sh
./papers/download_papers.sh
```

---

## 📂 Folder Organization

```
papers/
├── README.md (this file)
├── download_papers.sh (automated download)
│
├── ConTextTab_SAP_RPT1_NeurIPS2025.pdf
├── TabPFN_Nature_2025.pdf
├── TabICL_ICML_2025.pdf
├── TabArena_2025.pdf
├── TabZilla_NeurIPS_2023.pdf
├── TALENT_Toolkit.pdf
├── AutoGluon_Tabular.pdf
│
└── supplementary/ (optional)
    ├── RealMLP_paper.pdf
    ├── CARTE_paper.pdf
    └── REFORMS_checklist.pdf
```

---

## ✅ Download Checklist

- [ ] ConTextTab_SAP_RPT1_NeurIPS2025.pdf (✅ already have, move to papers/)
- [ ] TabPFN_Nature_2025.pdf
- [ ] TabICL_ICML_2025.pdf (or use GitHub docs if not published)
- [ ] TabArena_2025.pdf
- [ ] TabZilla_NeurIPS_2023.pdf
- [ ] TALENT_Toolkit.pdf (or use GitHub docs)
- [ ] AutoGluon_Tabular.pdf
- [ ] All PDFs readable and uncorrupted
- [ ] File sizes verified (>1MB typically)

---

## 📖 Usage for Research

**These papers are used for**:
1. **Research Agent** (Phase 0): Extracting methodology, performance claims, limitations
2. **Content Agent** (Agent 1): Citations, competitive comparisons, background
3. **Technical Analysis**: Understanding model architectures, training protocols
4. **Benchmarking Methodology**: Statistical testing, evaluation protocols
5. **Publication Writing**: Literature review, related work section

**Citation Format** (APA for deliverables):
```
Spinaci, M., Polewczyk, M., Schambach, M., & Thelin, S. (2025).
ConTextTab: A Semantics-Aware Tabular In-Context Learner.
In Advances in Neural Information Processing Systems (NeurIPS 2025).
```

---

## 🚨 Copyright & Usage

**All papers are used for**:
- Academic research purposes
- Non-commercial educational use
- Citation in our benchmarking study
- Literature review

**Compliance**:
- All papers cited appropriately
- No redistribution of paywalled content
- Fair use for academic research
- arXiv versions used where available

---

**Status**: ⏳ Download in progress
**Target Completion**: Week 1
**Total Papers**: 7 (minimum)
**Total Size**: ~50-100MB
