.PHONY: help install-backend install-frontend install run-backend run-frontend run test clean

help:
	@echo "Available commands:"
	@echo "  make install        - Install all dependencies"
	@echo "  make run           - Run both backend and frontend"
	@echo "  make run-backend   - Run backend only"
	@echo "  make run-frontend  - Run frontend only"
	@echo "  make test          - Run all tests"
	@echo "  make clean         - Clean cache files"

install-backend:
	cd backend && pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

install: install-backend install-frontend

run-backend:
	cd backend && python -m app.main

run-frontend:
	cd frontend && npm start

run:
	@echo "Starting backend and frontend..."
	@make run-backend & make run-frontend

test:
	cd backend && pytest
	cd frontend && npm test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf backend/.pytest_cache
	rm -rf frontend/node_modules/.cache
