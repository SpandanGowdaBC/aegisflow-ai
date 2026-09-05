from typing import List, Dict, Any

class PolicyChecker:
    """
    Evaluates LLM prompts against safety guardrails, prompt injection patterns,
    and compliance policies.
    """
    
    PROMPT_INJECTION_KEYWORDS: List[str] = [
        "ignore previous instructions",
        "system override",
        "bypass security",
        "act as DAN",
        "reveal system prompt",
        "sudo mode",
        "forget all rules"
    ]
    
    RESTRICTED_TOPICS: List[str] = [
        "malware generation",
        "exploit payload",
        "credential harvesting",
        "unauthorized database dump"
    ]

    def evaluate(self, prompt: str) -> Dict[str, Any]:
        """
        Evaluates safety risk score (0.0 = completely safe, 1.0 = highly malicious).
        """
        lowered_prompt = prompt.lower()
        violations: List[str] = []
        risk_score: float = 0.0

        # Check Prompt Injection
        for keyword in self.PROMPT_INJECTION_KEYWORDS:
            if keyword in lowered_prompt:
                violations.append(f"Prompt Injection Attempt: '{keyword}'")
                risk_score += 0.45

        # Check Restricted Topics
        for topic in self.RESTRICTED_TOPICS:
            if topic in lowered_prompt:
                violations.append(f"Restricted Content: '{topic}'")
                risk_score += 0.50

        risk_score = min(1.0, risk_score)
        
        status = "PASSED"
        if risk_score >= 0.70:
            status = "BLOCKED"
        elif risk_score >= 0.30:
            status = "FLAGGED"

        return {
            "status": status,
            "risk_score": round(risk_score, 2),
            "is_safe": status == "PASSED",
            "violations": violations
        }
