FROM python:3.11-slim

WORKDIR /app

# NOTE: Render always uses the repository root as the Docker build context,
# even when rootDir is set. So all COPY paths must be prefixed with backend/.
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY backend/app ./app

# Expose port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
