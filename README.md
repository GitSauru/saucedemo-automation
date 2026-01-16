# SauceDemo Automation (Playwright + Pytest)

## Overview

UI automation framework for [https://www.saucedemo.com](https://www.saucedemo.com) using **Playwright (Python)** and **Pytest**. Covers login, product sorting, cart, and checkout flows. Designed with Page Object Model and CI/CD in mind.

## Tech Stack

* Python 3
* Playwright (sync API)
* Pytest
* pytest-xdist (parallel execution)
* pytest-html (reporting)
* GitHub Actions (CI)

## Project Structure

```
├── pages/          # Page Object classes
├── tests/          # Test cases
├── utils/          # Utilities (env config, helpers)
├── conftest.py     # Fixtures (browser, page, login)
├── requirements.txt
├── pytest.ini
└── README.md
```

## Environment Setup

Credentials are managed via `.env` (not committed).

Example `.env`:

```
URL=https://www.saucedemo.com/
User_id=standard_user
Password=secret_sauce
```

## Install & Run

```bash
pip install -r requirements.txt
playwright install
pytest
```

## Parallel Execution

```bash
pytest -n auto
```

## HTML Report

```bash
pytest --html=report.html --self-contained-html
```

## CI/CD

GitHub Actions runs tests automatically on push and pull requests.

## Design Principles

* Page Object Model
* Reusable fixtures
* Clean separation of test logic and UI locators

## Future Enhancements

* Allure reporting
* Cross-browser execution
* Docker support
