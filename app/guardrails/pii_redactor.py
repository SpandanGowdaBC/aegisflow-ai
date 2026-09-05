import re
from typing import Dict, Tuple

class PIIRedactor:
    """
    High-performance PII & Secret Redaction Engine.
    Scans raw LLM prompts for sensitive credentials, personal data, and tokens,
    replacing them with deterministic placeholder tokens.
    """
    
    PATTERNS: Dict[str, str] = {
        "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "PHONE": r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
        "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
        "CREDIT_CARD": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
        "API_KEY": r"(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?([a-zA-Z0-9_\-]{16,})['\"]?",
        "JWT": r"eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"
    }

    def redact(self, text: str) -> Tuple[str, int, Dict[str, int]]:
        """
        Redacts PII patterns from input text.
        Returns: (sanitized_text, total_redactions_count, redaction_breakdown_dict)
        """
        sanitized_text = text
        total_count = 0
        breakdown: Dict[str, int] = {}

        for pii_type, pattern in self.PATTERNS.items():
            matches = re.findall(pattern, sanitized_text)
            count = len(matches)
            if count > 0:
                placeholder = f"[REDACTED_{pii_type}]"
                sanitized_text = re.sub(pattern, placeholder, sanitized_text)
                total_count += count
                breakdown[pii_type] = count

        return sanitized_text, total_count, breakdown
