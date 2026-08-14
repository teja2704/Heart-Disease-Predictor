FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=10000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

COPY app.py KNN_Heart.pkl scaler.pkl columns.pkl ./

RUN useradd --create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app

ENV PATH="/usr/local/bin:/home/appuser/.local/bin:$PATH"

USER appuser

EXPOSE 10000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.getenv('PORT', '10000') + '/_stcore/health', timeout=3)"

CMD ["sh", "-c", "python -m streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-10000} --server.headless=true"]
