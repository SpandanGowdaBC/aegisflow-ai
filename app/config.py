import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AegisFlow-AI Engine"
    ENVIRONMENT: str = "production"
    
    # Vector Database Settings (Qdrant)
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    QDRANT_COLLECTION_NAME: str = "enterprise_knowledge_base"
    
    # ClickHouse Telemetry Settings
    CLICKHOUSE_HOST: str = os.getenv("CLICKHOUSE_HOST", "localhost")
    CLICKHOUSE_PORT: int = int(os.getenv("CLICKHOUSE_PORT", 8123))
    CLICKHOUSE_DB: str = "aegisflow_telemetry"
    
    # Kafka Messaging Settings
    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_TELEMETRY_TOPIC: str = "aegis.telemetry.events"
    
    # Redis Cache & Rate Limiter Settings
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    
    # OpenAI Settings (Optional fallback)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "mock-key-for-local-demo")

    class Config:
        env_file = ".env"

settings = Settings()
