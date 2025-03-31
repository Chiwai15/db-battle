import threading
from fastapi import FastAPI
from app.grpc_server import server as grpc_server

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

def start_grpc():
    grpc_server.serve()

grpc_thread = threading.Thread(target=start_grpc, daemon=True)
grpc_thread.start()