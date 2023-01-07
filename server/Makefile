activate-venv:
	. venv/bin/activate

install:
	if [ ! -d venv ]; then \
		$(MAKE) install-venv; \
	fi

	$(MAKE) activate-venv
	pip install -r requirements.txt
	pre-commit install

up-source:
	$(MAKE) activate-venv
	python app.py
