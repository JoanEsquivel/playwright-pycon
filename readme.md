[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Virtual environemnts (MacOS):

Requirements:

- Python3
- Pip3
- $ brew install python3 #upgrade
- Pip3 is installed with Python3

## Installation

To install virtualenv via pip run:

`$ pip3 install virtualenv`

## Usage

Creation of virtualenv:

`$ python3 -m venv playwright-python`

Activate the virtualenv:

`$ source <desired-path>/bin/activate`
Deactivate the virtualenv:

`$ deactivate`

# How to install Playwright + Python for the first time?

## Install packages

`pip install playwright`
`pip install pytest`
`pip install pytest-playwright`

## Install browsers

`playwright install`

## To install the requirements(dependencies)

`pip install -r requirements.txt`

# Run tests (different approaches)

`python -m pytest tests`
`python -m pytest tests --headed --slowmo 1000`
` python -m pytest tests --headed --slowmo 1000 --browser chromium`
`python -m pytest tests --headed --slowmo 1000 --browser firefox`
`python -m pytest tests --headed --slowmo 1000 --browser webkit`

### Execute in multiple browsers

` python -m pytest tests --headed --slowmo 1000 --browser chromium --browser firefox --browser webkit --verbose`

## Stock browsers

`python -m pytest tests --headed --slowmo 1000 --browser-channel chrome`

## Emulate mobile to test responsive layouts

`python -m pytest tests --headed --slowmo 1000 --browser webkit --device "iPhone 11"`
`python -m pytest tests --browser-channel chrome --screenshot on`
`python -m pytest tests --screenshot only-on-failure`
`python -m pytest tests --video on`
`python -m pytest tests --video retain-on-failure`

## How to trace your execution?

` python -m pytest tests --headed --slowmo 1000 --browser chromium --tracing on`

`playwright show-trace test-results/tests-test-todos-py-test-add-new-todo-chromium/trace.zip`

# Ruff commands for lint & format
` ruff check . `
` ruff format . `

