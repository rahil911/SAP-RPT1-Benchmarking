# Baselines Docker Environment
# Python 3.10 for gradient boosting models
# XGBoost, CatBoost, LightGBM

FROM python:3.10-slim

LABEL maintainer="UW MSIM Team"
LABEL description="Gradient boosting baselines (XGBoost, CatBoost, LightGBM)"
LABEL version="1.0"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    wget \
    curl \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY docker/requirements-baselines.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

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
ENV MODEL_NAME=baselines

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import xgboost, catboost, lightgbm; print('All baselines loaded')" || exit 1

ENTRYPOINT ["python"]
CMD ["-m", "runners.run_experiment"]
