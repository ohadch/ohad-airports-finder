DOCKER_IMAGE_NAME = "airports-finder-server"

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

build-docker:
	docker build -t $(DOCKER_IMAGE_NAME) .

up-docker:
	# Build docker image if it doesn't exist
	if [ -z "$(shell docker images -q $(DOCKER_IMAGE_NAME))" ]; then \
		$(MAKE) build-docker; \
	fi

	docker run -p 8000:8000 $(DOCKER_IMAGE_NAME)
