# LLM Router

## Overview

A Dockerized API Router leveraging Hugging Face and dynamic routing logic to optimize API selection based on semantic analysis and real-time metrics.

## Features

- Semantic analysis for task-specific routing using Hugging Face.
- Dynamic routing based on latency, cost, and accuracy.
- Dockerized deployment for portability.
- Testable with a 93% routing accuracy.

## File Structure

llm_router_project/ ├── src/ │ ├── router.py # Flask API for routing │ ├── dynamic_routes.py # Logic for dynamic routing │ ├── semantic_analysis.py # Semantic analysis logic │ ├── static_routes.json # Static routing configuration │ ├── monitoring/ # Metrics for performance monitoring │ ├── metrics.py ├── tests/ │ ├── test_router.py # Unit tests for routing ├── Dockerfile # Docker container definition ├── docker-compose.yml # Multi-service container orchestration ├── requirements.txt # Python dependencies ├── README.md # Instructions and project overview └── run_on_notebook.ipynb # Jupyter notebook for experimentation

## Prerequisites

- Docker and Docker Compose installed.
- Python 3.8+ (for local testing).

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/llm-router.git
   cd llm-router

   ```

2. pip install -r requirements.txt

3. python src/router.py
