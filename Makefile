# vim:set noet:

.PHONY: help server test

help:
	@echo 'Usage:'
	@echo '  make server        serve walis on port 3000'
	@echo '  make client        run whelper client'
	@echo '  make test          run unitests'
	@echo '  make install       install walis as a package'
	@echo '  make lint          run pylint'

server:
	python walis/server.py

thrift_server:
	python -m walis.thrift.server

client:
	python walis/helper.py

lint:
	flake8 walis

test:
	find . -name '*.pyc' -delete
	py.test tests/units -vvv -x

requirements:
	pip install -r dev_requirements.txt --download-cache /tmp/pip_eleme

develop: requirements config log
	python setup.py -q develop
	@echo "Build develop environment finished."

log:
	if [ ! -d "/var/log/walis" ]; then sudo mkdir -p /var/log/walis; fi
	sudo chmod -R og+w /var/log/walis

config:
	python genconfig.py --force_cover

all: develop
