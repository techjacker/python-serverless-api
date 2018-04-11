COVERAGE_MIN = 50

env:
	@python3 -m venv env

####################
# run local server
####################
server:
	@FLASK_APP=run.py flask run

server-debug:
	@$(shell FLASK_DEBUG=1 make server)

server-docker:
	@FLASK_APP=run.py flask run --host 0.0.0.0


####################
# dependencies
####################
deps:
	@pip install -r requirements.txt
	@pre-commit install

deps-update:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

deps-uninstall:
	@pip uninstall -yr requirements.txt
	@pip freeze > requirements.txt

####################
# lint
####################
lint:
	@pre-commit run \
		--allow-unstaged-config \
		--all-files \
		--verbose

autopep8:
	@autopep8 . --recursive --in-place --pep8-passes 2000 --verbose

autopep8-stats:
	@pep8 --quiet --statistics .

####################
# tests
####################
test: config/testing.py
	@pytest --cov-fail-under $(COVERAGE_MIN) --cov=app --cov-report html:htmlcov

test-debug:
	@pytest --pdb

test-deploy:
	@http-prompt $(shell cd terraform && terraform output api_url)

clean:
	@find . -name '__pycache__' | xargs rm -rf

.PHONY: deps* lint test* clean autopep8* migrate server*
