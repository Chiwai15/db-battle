# Universal Benchmarking Platform Design

## 🔧 Project Overview

A full-stack, extensible open-source benchmarking platform with the following characteristics:

- ✅ Multi-language support: Go, Rust, Python, Java (more can be added)
- ✅ Multi-database support: Cassandra, ScyllaDB, Postgres, MongoDB, Redis, etc.
- ✅ Services communicate via **gRPC**
- ✅ Central **Controller Service** orchestrates benchmarks
- ✅ Benchmarks include:
  - Write/read **latency**
  - **Throughput** (ops/sec)
  - **CPU and memory usage**
  - **Concurrency under load**
  - Realistic **data sizes**
- ✅ **Docker Compose** setup with all supported services and databases
- ✅ React-based **Dashboard** to trigger tests and visualize results
- ✅ Benchmark **results historized** in Postgres/InfluxDB

---

## 🧠 Key Concepts & Architecture

### 1. **Service-Level Design (Go, Rust, Python, Java)**
Each language service implements:
- Common gRPC contract (defined in `benchmark.proto`)
- Benchmark Engine (CRUD, payload generator, metrics recorder)
- DB Adapter Interface (pluggable DB clients)

**Recommended Architecture per Language:**
- **Java**: Spring Boot + grpc-spring-boot-starter
- **Python**: FastAPI + grpcio for gRPC server
- **Go**: Pure gRPC + clean architecture (cmd/internal/pkg)
- **Rust**: Tonic + modular services with traits and adapters

### 2. **Controller Service**
- Sends gRPC benchmark commands to any registered service
- Aggregates results and stores them in a results database
- Exposes REST API (and optionally WebSocket) for the UI

### 3. **React Frontend Dashboard**
React web UI that lets users:
- Choose language + DB + operation
- Configure concurrency, payload size, test duration
- Launch benchmark and view live & historical results
- Display results in real-time with charts (WebSocket optional)

### 4. **Database Adapters**

---

## 🚀 Phase 1 Goals

- [ ] Define `benchmark.proto` shared contract
- [ ] Build Python + Postgres microservice using FastAPI + grpcio
- [ ] Build Rust + ScyllaDB microservice using Tonic
- [ ] Build Go + Cassandra microservice using pure gRPC
- [ ] Create DB adapter interface in all languages
- [ ] Build controller service
- [ ] Build React dashboard with benchmark configuration and live results
- [ ] Store benchmark results with metadata
- [ ] Docker Compose with all databases and services

---

## 🚭 Long-term Vision

- Unified UI for multi-language benchmark testing
- Easy plugin system for adding new languages and databases
- Automated scheduled benchmarks via GitHub Actions
- Community-driven DB/Language adapter contribution
- Public dashboard or SaaS portal (optional)
