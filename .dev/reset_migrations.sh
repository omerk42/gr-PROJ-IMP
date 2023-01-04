#!/bin/sh

find ../zaid/mainapp -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ../zaid/mainapp -path "*/migrations/*.pyc" -delete
