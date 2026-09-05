from typing import Dict, Any, List

class HallucinationScorer:
    """
    Semantic Similarity & Faithfulness Scorer.
    Evaluates LLM response text against retrieved RAG ground-truth context
    to calculate hallucination risk scores.
    """
    def score_faithfulness(self, response_text: str, grounded_context_chunks: List[str]) -> Dict[str, Any]:
        """
        Calculates grounding overlap confidence score.
        Returns: (faithfulness_score 0.0 - 1.0, is_grounded)
        """
        if not grounded_context_chunks:
            return {"faithfulness_score": 0.0, "is_grounded": False, "reason": "No grounded context provided"}
            
        lowered_response = response_text.lower()
        matched_chunks = 0
        
        for chunk in grounded_context_chunks:
            words = chunk.lower().split()
            # Calculate word overlap ratio
            matches = sum(1 for word in words if word in lowered_response)
            if matches / max(1, len(words)) > 0.3:
                matched_chunks += 1
                
        faithfulness_score = min(1.0, matched_chunks / len(grounded_context_chunks))
        
        return {
            "faithfulness_score": round(faithfulness_score, 2),
            "is_grounded": faithfulness_score >= 0.50,
            "hallucination_detected": faithfulness_score < 0.50
        }
