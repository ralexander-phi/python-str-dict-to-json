#!/bin/bash

source .venv/bin/activate
rm -Rf dist/
python setup.py sdist

