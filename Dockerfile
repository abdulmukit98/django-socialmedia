# Dockerfile
FROM python:3.12.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Run server (override in docker-compose)
CMD [ "gunicorn", "socialmedia.wsgi:application", "--bind", "0.0.0.0:8000"]