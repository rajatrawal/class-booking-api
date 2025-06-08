# 1. Use official Python image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project files
COPY . /app/



# 7. Expose port (optional, for dev testing)
EXPOSE 8000

# 8. Start app with gunicorn
CMD ["gunicorn", "fitness_api.wsgi:application", "--bind", "0.0.0.0:8000"]
