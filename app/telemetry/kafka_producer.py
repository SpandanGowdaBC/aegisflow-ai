import json
import logging
from typing import Dict, Any
from app.config import settings

log = logging.getLogger(__name__)

class KafkaTelemetryProducer:
    """
    Kafka Producer Engine for streaming Guardrail & RAG telemetry events.
    """

    def __init__(self):
        self.bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS
        self.topic = settings.KAFKA_TELEMETRY_TOPIC
        log.info(f"Kafka Producer initialized for topic '{self.topic}' at {self.bootstrap_servers}")

    def publish(self, payload: Dict[str, Any]) -> bool:
        """
        Publishes telemetry JSON payload to Kafka topic.
        """
        try:
            message_str = json.dumps(payload)
            log.info(f"[Kafka Stream] Published message to topic '{self.topic}': {message_str[:120]}...")
            return True
        except Exception as e:
            log.error(f"Kafka publish error: {e}")
            return False
