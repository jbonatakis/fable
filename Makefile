VENV = env
BIN=$(VENV)/bin

$(VENV):
	@if [ ! -d env/ ]; then \
		echo "Creating a virtual environment and installing dependencies..."; \
	fi;
	@python3 -m venv $(VENV)
	@$(BIN)/pip install --upgrade -q pip
	@$(BIN)/pip install -q -e '.[dev]'

lint: $(VENV)
	@$(BIN)/python -m ruff check

format: $(VENV)
	@$(BIN)/python -m ruff format

test: $(VENV)
	@$(BIN)/python -m pytest tests/

clean:
	@rm -rf env/ .ruff_cache/ fable.egg-info/ \
	src/fable.egg-info/ src/fable/__pycache__ \
	tests/__pycache__ .pytest_cache/

reset: clean $(VENV)

todo:
	@grep -inr "todo" src/ test/

run-example: $(VENV)
	@$(BIN)/python example/example.py
