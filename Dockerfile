# 1. 베이스 이미지 설정
FROM python:3.11-slim

# 2. 환경변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 복사
COPY . .

# 6. Gunicorn으로 앱 실행 (3000번 포트 사용)
# core.wsgi는 본인의 Django 프로젝트 설정에 맞게 수정하세요.
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "core.wsgi"]
