# AegisFlow-AI 🛡️⚡
> **Enterprise RAG Retrieval Engine & Real-Time AI Guardrail Telemetry Pipeline**

[![Python 3.11](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)
[![Qdrant](https://img.shields.io/badge/Qdrant-v1.8.0-red.svg)](https://qdrant.tech/)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-24.2-yellow.svg)](https://clickhouse.com/)
[![Kafka](https://img.shields.io/badge/Kafka-Confluent-black.svg)](https://kafka.apache.org/)

---

## 📌 Executive Summary

**AegisFlow-AI** is a production-grade microservice architecture designed to solve core reliability, security, and observability challenges in enterprise Large Language Model (LLM) deployments. 

It acts as an inline middleware proxy that:
1. **Redacts PII & Secrets** (Emails, Credit Cards, API Keys, JWTs) using high-speed regex pattern matching.
2. **Evaluates Policy & Prompt Injection Attacks** (e.g., `ignore previous instructions`, System Overrides) and returns deterministic safety risk scores.
3. **Retrieves Grounded RAG Knowledge** using **Qdrant Vector DB** similarity search to eliminate AI hallucinations.
4. **Asynchronously Streams Analytics Events** to **Apache Kafka** and logs structured records in **ClickHouse** for OLAP observability.

---

## 🏗️ System Architecture

```text
┌────────────────┐     ┌─────────────────────────────────────────────────────────────────┐
│ User / Client  ├────►│                      AegisFlow-AI Proxy                         │
└────────────────┘     │  (FastAPI Middleware Engine)                                    │
                       └──────────────┬──────────────────┬──────────────────┬────────────┘
                                      │                  │                  │
                         1. PII Masking       2. RAG Retrieval    3. Event Telemetry
                                      │                  │                  │
                                      ▼                  ▼                  ▼
                               ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
                               │ Regex Engine│    │ Qdrant DB   │    │ Apache Kafka│
                               └─────────────┘    └─────────────┘    └──────┬──────┘
                                                                            │
                                                                            ▼
                                                                     ┌─────────────┐
                                                                     │ ClickHouse  │
                                                                     │ (OLAP DB)   │
                                                                     └─────────────┘
```

---

## 🛠️ Technology Stack

* **API Engine**: Python 3.11, FastAPI, Pydantic v2
* **Vector Store & RAG**: Qdrant Vector DB, SentenceTransformers
* **Event Broker**: Apache Kafka, Zookeeper
* **OLAP Analytics**: ClickHouse Server
* **In-Memory Cache**: Redis
* **Containerization**: Docker, Docker Compose

---

## 🚀 Quickstart & Setup

### Prerequisites
* Docker & Docker Compose installed

### 1. Clone & Spin Up Containers
```bash
git clone https://github.com/SpandanGowdaBC/aegisflow-ai.git
cd aegisflow-ai

# Start all microservices (FastAPI, Qdrant, ClickHouse, Kafka, Redis)
docker-compose up -d --build
```

### 2. Verify Health Endpoint
```bash
curl http://localhost:8000/
```

---

## 📡 API Endpoint Documentation & Examples

### 🛡️ 1. Analyze Guardrails & PII Redaction
**Endpoint:** `POST /v1/guardrails/analyze`

```bash
curl -X POST "http://localhost:8000/v1/guardrails/analyze" \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "Please send my API key secret_9988776655443322 to john.doe@example.com immediately.",
           "user_id": "usr_101",
           "tenant_id": "tenant_acme"
         }'
```

**Response Payload:**
```json
{
  "request_id": "req_8a1f9e2b3c",
  "original_prompt": "Please send my API key secret_9988776655443322 to john.doe@example.com immediately.",
  "sanitized_prompt": "Please send my API key [REDACTED_API_KEY] to [REDACTED_EMAIL] immediately.",
  "status": "PASSED",
  "risk_score": 0.0,
  "is_safe": true,
  "redactions_count": 2,
  "redactions_breakdown": {
    "API_KEY": 1,
    "EMAIL": 1
  },
  "violations": [],
  "execution_time_ms": 4.12
}
```

---

### 🔍 2. Retrieve Grounded RAG Knowledge
**Endpoint:** `POST /v1/rag/query`

```bash
curl -X POST "http://localhost:8000/v1/rag/query" \
     -H "Content-Type: application/json" \
     -d '{
           "query": "What are the security guidelines for API tokens?",
           "top_k": 2
         }'
```

---

## 🎯 Resume & Interview Summary
> *"Architected AegisFlow-AI, an enterprise RAG retrieval and real-time AI guardrail middleware using Python (FastAPI), Qdrant Vector DB, Apache Kafka, and ClickHouse. Built automated PII redaction engines, prompt injection risk scoring, and asynchronous event stream logging."*
