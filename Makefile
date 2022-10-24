#!/usr/bin/make
#

plone-version=60
python-version=3.8

setup:
	./venv-$(python-version)/bin/pip install --upgrade pip
	./venv-$(python-version)/bin/pip install -r requirements_plone$(plone-version).txt

buildout:
	if ! test -f venv-$(python-version)/bin/buildout;then make setup;fi
	./venv-$(python-version)/bin/buildout -c test_plone$(plone-version).cfg

.PHONY: plone43
plone43:
	make cleanall
	virtualenv-2.7 venv-$(python-version)
	make buildout plone-version=43

.PHONY: plone51
plone51:
	make cleanall
	virtualenv-2.7 venv-$(python-version)
	make buildout plone-version=51

.PHONY: plone52
plone52:
	make cleanall
	python3 -m venv venv-3.8
	make buildout plone-version=52

.PHONY: plone60
plone60:
	make cleanall
	python3 -m venv venv-3.8
	make buildout plone-version=60

.PHONY: run
run:
	if ! test -f bin/instance;then make plone60;fi
	bin/instance fg

.PHONY: cleanall
cleanall:
	rm -fr venv-2.7 venv-3.8 bin develop-eggs lib parts .installed.cfg .mr.developer.cfg downloads eggs lib64 include local/
