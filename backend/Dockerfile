FROM python:3.11-slim

WORKDIR /app

# Install dependencies
# (COPY paths are relative to the Docker build context, which Render sets
#  to the rootDir of this service — i.e. the 'backend/' folder)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app ./app

# Expose port
EXPOSE 8000

# Start the server
# 'app.main:app' matches the module path: /app/app/main.py -> app.main -> app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
