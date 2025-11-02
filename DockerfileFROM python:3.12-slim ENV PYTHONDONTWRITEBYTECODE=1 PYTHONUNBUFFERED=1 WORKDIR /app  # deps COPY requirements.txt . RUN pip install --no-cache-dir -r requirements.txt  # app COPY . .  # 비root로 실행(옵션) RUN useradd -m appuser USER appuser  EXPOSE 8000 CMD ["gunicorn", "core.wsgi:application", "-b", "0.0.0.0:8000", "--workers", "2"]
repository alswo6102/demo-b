FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app
COPY . .

# 비root로 실행(옵션)
RUN useradd -m appuser
USER appuser

EXPOSE 8000
CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000", "--workers", "2"]
