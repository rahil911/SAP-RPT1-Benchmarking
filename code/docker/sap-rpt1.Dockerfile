# SAP RPT-1 Docker Environment
# Python 3.11 required for SAP RPT-1-OSS
# GPU-enabled container for transformer models

FROM python:3.11-slim

LABEL maintainer="UW MSIM Team"
LABEL description="SAP RPT-1 benchmarking environment"
LABEL version="1.0"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    wget \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for layer caching
COPY docker/requirements-sap-rpt1.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install SAP RPT-1 from GitHub
RUN pip install --no-cache-dir git+https://github.com/SAP-samples/sap-rpt-1-oss.git

# Copy application code
COPY models/ /app/models/
COPY datasets/ /app/datasets/
COPY evaluation/ /app/evaluation/
COPY runners/ /app/runners/
COPY config/ /app/config/
COPY utils/ /app/utils/

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV MODEL_NAME=sap-rpt1
ENV TRANSFORMERS_CACHE=/app/.cache/huggingface
ENV HF_HOME=/app/.cache/huggingface

# Create cache directory
RUN mkdir -p /app/.cache/huggingface

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sap_rpt_1_oss; print('SAP RPT-1 loaded')" || exit 1

ENTRYPOINT ["python"]
CMD ["-m", "runners.run_experiment"]
