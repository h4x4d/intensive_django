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
	poetry run python manage.py runserver

.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: pip-run
pip-run:
	python manage.py runserver


.PHONY: delete_allure
delete_allure:
	rm allure-results/* allure-results/.*

.PHONY: test
test:
	pytest --alluredir=allure-results -s -v -n auto


.PHONY: generate
generate: test
	allure generate --clean


.PHONY: run_server
run_server: test
	allure serve -p 30000