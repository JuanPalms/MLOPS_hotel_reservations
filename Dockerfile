FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    ca-certificates \
    pkg-config \
    libssl-dev \
    libbz2-dev \
    zlib1g-dev \
    libgomp1 \
    libprotobuf-dev \
    protobuf-compiler \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -e .

RUN python pipeline/training_pipeline.python

EXPOSE 5000

CMD ["python","application.py"]

