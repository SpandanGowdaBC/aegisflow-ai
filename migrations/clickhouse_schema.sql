-- ClickHouse Telemetry Database & Table Schemas for AegisFlow-AI
CREATE DATABASE IF NOT EXISTS aegisflow_telemetry;

CREATE TABLE IF NOT EXISTS aegisflow_telemetry.guardrail_events (
    request_id String,
    tenant_id String,
    user_id String,
    original_prompt String,
    sanitized_prompt String,
    status LowCardinality(String),
    risk_score Float32,
    is_safe UInt8,
    redactions_count UInt16,
    execution_time_ms Float32,
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY (created_at, tenant_id, status)
PRIMARY KEY (created_at, tenant_id);
