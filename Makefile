VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

.PHONY: all
all: install

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) web_scrap_emails_from_europarl.py

clean:
	rm -rf $(VENV)

format:
	$(PYTHON) -m ruff format .

lint:
	$(PYTHON) -m ruff check .