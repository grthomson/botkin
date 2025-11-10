# ops/Dockerfile
FROM python:3.11-slim

# System deps (add build tools only if you need to compile libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy metadata first for better caching
COPY pyproject.toml README.md ./ 
# Optional: if you create a requirements.txt later, copy it here too:
# COPY requirements.txt ./

# Install deps (editable install of our src package after copying code below)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir "uvicorn[standard]" fastapi && \
    pip install --no-cache-dir -e .

# Now copy source
COPY src ./src
# If you serve from ops/api:
# COPY ops/api ./ops/api

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

EXPOSE 8000
# Adjust import path to wherever your app is (we scaffolded botkin.api.app)
CMD ["uvicorn", "botkin.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
