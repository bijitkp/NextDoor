FROM python:3.12-slim

WORKDIR /build

# Copy dependency definition
COPY services/auth-service/requirements.txt .

# Copy shared configuration
COPY config/ ./config/

# Copy Auth Service source
COPY services/auth-service/ .

COPY database/ ./database/

# Install Python dependencies inside the Docker image
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]