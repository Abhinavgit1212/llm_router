import numpy as np
from semantic_analysis import analyze_request_semantics

MODEL_METRICS = {
    "gpt-4": {"latency": 200, "cost": 0.5, "accuracy": 0.95},
    "gpt-3.5": {"latency": 150, "cost": 0.2, "accuracy": 0.90},
    "opt-66b": {"latency": 180, "cost": 0.3, "accuracy": 0.88},
}

MODEL_CAPABILITIES = {
    "gpt-4": ["complex", "reasoning", "creative"],
    "gpt-3.5": ["general", "balanced", "efficient"],
    "opt-66b": ["simple", "fast", "low-latency"]
}

METRIC_WEIGHTS = {"latency": -0.4, "cost": -0.3, "accuracy": 0.3}

def calculate_model_score(metrics, weights):
    scores = [metrics[metric] * weights[metric] for metric in weights]
    return np.sum(scores)

def dynamic_route_with_semantics(request_text, real_time_metrics):
    semantic_label = analyze_request_semantics(request_text)
    model_scores = {}
    for model, baseline_metrics in MODEL_METRICS.items():
        capabilities = MODEL_CAPABILITIES[model]
        semantic_match = 1 if semantic_label in capabilities else 0
        combined_metrics = {k: real_time_metrics.get(k, baseline_metrics[k]) for k in METRIC_WEIGHTS}
        score = calculate_model_score(combined_metrics, METRIC_WEIGHTS) + (semantic_match * 0.5)
        model_scores[model] = score
    return max(model_scores, key=model_scores.get)
