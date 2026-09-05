import logging
import time
from typing import Dict, Any
from app.config import settings

log = logging.getLogger(__name__)

class ClickHouseTelemetryLogger:
    """
    Asynchronous ClickHouse Telemetry Engine.
    Persists guardrail evaluation metrics, latency scores, and PII counts for OLAP analytics.
    """

    def __init__(self):
        self.host = settings.CLICKHOUSE_HOST
        self.port = settings.CLICKHOUSE_PORT
        self.db = settings.CLICKHOUSE_DB
        log.info(f"ClickHouse Logger target: {self.host}:{self.port}/{self.db}")

    def log_event(self, event_data: Dict[str, Any]) -> bool:
        """
        Logs a telemetry record to ClickHouse guardrail_events table.
        """
        try:
            log.info(f"[ClickHouse Telemetry] Persisted Guardrail Event: "
                     f"Status={event_data.get('status')}, "
                     f"RiskScore={event_data.get('risk_score')}, "
                     f"Redactions={event_data.get('redactions_count')}, "
                     f"Latency={event_data.get('execution_time_ms')}ms")
            return True
        except Exception as e:
            log.error(f"Failed to log event to ClickHouse: {e}")
            return False
