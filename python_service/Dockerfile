FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY python_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY python_service/app ./app

# Copy proto into the same location where gRPC files will be generated
COPY proto ./app/proto

# Generate gRPC Python code inside app/proto/
RUN python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  ./app/proto/benchmark.proto

# Set Python module path
ENV PYTHONPATH=/app

# Run FastAPI app with gRPC server in background
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build --no-cache -f python_service/Dockerfile -t db-battle-python .
# docker run -p 8000:8000 -p 50051:50051 db-battle-python
