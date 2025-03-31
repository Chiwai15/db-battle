from concurrent import futures
import grpc
import psutil
import time
from app.proto import benchmark_pb2_grpc, benchmark_pb2

class BenchmarkService(benchmark_pb2_grpc.BenchmarkServiceServicer):
    def RunBenchmark(self, request, context):
        start = time.time()

        # Simulate processing time
        time.sleep(0.1)

        end = time.time()
        latency = (end - start) * 1000
        throughput = request.num_operations / (end - start)

        return benchmark_pb2.BenchmarkResult(
            language=request.language,
            database=request.database,
            operation=request.operation,
            total_operations=request.num_operations,
            avg_latency_ms=latency,
            throughput_ops=throughput,
            cpu_percent=psutil.cpu_percent(),
            memory_mb=psutil.virtual_memory().used / 1024 / 1024,
            timestamp=str(time.time())
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    benchmark_pb2_grpc.add_BenchmarkServiceServicer_to_server(BenchmarkService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
