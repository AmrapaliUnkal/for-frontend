#!/bin/bash

# Start FastAPI Backend
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit Frontend
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false --server.headless true
