FROM python:3.11-slim 
WORKDIR /app 
RUN apt-get update && apt-get install -y gcc postgresql-client && rm -rf /var/lib/apt/lists/* 
COPY backend/requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt 
COPY backend/ /app/backend/ 
COPY frontend/ /app/frontend/ 
RUN mkdir -p /app/backend/staticfiles 
ENV PYTHONUNBUFFERED=1 
ENV DJANGO_SETTINGS_MODULE=backend.settings 
EXPOSE 8000 
CMD cd /app/backend && python manage.py migrate && gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT 
