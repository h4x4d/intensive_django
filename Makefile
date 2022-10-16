.PHONY: install
install:
	poetry install

.PHONY: install-dev
install-dev:
	make install-dev

.PHONY: pip-install
pip-install:
	pip install -r requirements.txt

.PHONY: pip-install-dev
pip-install-dev:
	pip install -r requirements-dev.txt

.PHONY: use
use: install
	cd ./intensive_django && poetry run python manage.py runserver

.PHONY: run
run:
	cd ./intensive_django && poetry run python manage.py runserver

.PHONY: pip-run
pip-run:
	cd ./intensive_django && python manage.py runserver