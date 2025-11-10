FROM python:3.11-slim

WORKDIR /app

# Copy metadata first (helps caching when deps don't change)
COPY pyproject.toml README.md ./

# Copy the package source BEFORE installing it
COPY src ./src

ENV PIP_NO_CACHE_DIR=1 PYTHONUNBUFFERED=1 PORT=8000

# Install runtime deps + your package (editable)
RUN python -m pip install --upgrade pip && \
    pip install "uvicorn[standard]" fastapi && \
    pip install -e .

EXPOSE 8000
CMD ["uvicorn", "botkin.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
