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

check-dist: $(VENV)
	@$(BIN)/python -m pip install --upgrade build && \
	$(BIN)/python -m pip install --upgrade twine && \
	$(BIN)/python -m build && \
	$(BIN)/python -m twine check --strict dist/fabledata*.whl 

format: $(VENV)
	@$(BIN)/python -m ruff format

test: $(VENV)
	@$(BIN)/python -m pytest tests/

clean:
	@rm -rf env/ .ruff_cache/ fable.egg-info/ \
	src/fable.egg-info/ src/fable/__pycache__ \
	tests/__pycache__ .pytest_cache/ dist/

reset: clean $(VENV)

todo:
	@grep -inr "todo" src/ tests/

run-example: $(VENV)
	@$(BIN)/python example/example.py
