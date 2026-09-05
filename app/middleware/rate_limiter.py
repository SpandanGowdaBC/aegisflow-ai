import time
import logging
from typing import Dict

log = logging.getLogger(__name__)

class RedisTokenBucketRateLimiter:
    """
    Token Bucket Rate Limiter Engine.
    Limits API request bursts per tenant to protect backend services.
    """
    def __init__(self, rate_limit: int = 100, window_seconds: int = 60):
        self.rate_limit = rate_limit
        self.window_seconds = window_seconds
        self.tenant_requests: Dict[str, list] = {}

    def is_allowed(self, tenant_id: str) -> bool:
        now = time.time()
        timestamps = self.tenant_requests.get(tenant_id, [])
        
        # Filter out timestamps outside the rate limit window
        valid_timestamps = [ts for ts in timestamps if now - ts < self.window_seconds]
        
        if len(valid_timestamps) >= self.rate_limit:
            log.warning(f"[RateLimiter] Rate limit exceeded for tenant '{tenant_id}' ({len(valid_timestamps)} reqs/{self.window_seconds}s)")
            return False
            
        valid_timestamps.append(now)
        self.tenant_requests[tenant_id] = valid_timestamps
        return True
