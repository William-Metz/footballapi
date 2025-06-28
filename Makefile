.PHONY: setup run clean

# Create virtual environment and install dependencies
setup:
	@echo "Creating virtual environment..."
	@mkdir -p venv
	@{ \
		if python3 -m venv venv; then \
			echo "Created venv using python3"; \
		elif python -m venv venv; then \
			echo "Created venv using python"; \
		else \
			echo "Failed to create virtual environment with both python3 and python"; \
			exit 1; \
		fi \
	}
	@echo "Activating virtual environment and install requirements"
	@. venv/bin/activate && pip install -r requirements.txt || { echo "Dependency install failed"; exit 1; }


run:
	@echo "Running Flask app..."
	@. venv/bin/activate && flask --app example run || { echo "Flask failed to run"; exit 1; }

# Remove venv
clean:
	@echo "Removing virtual environment..."
	@rm -rf venv

