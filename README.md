# PriceWatch

A cryptocurrency price monitoring tool built to learn Django, Celery, Redis, and Docker.

It tracks coin prices via the CoinGecko API and sends Telegram notifications when prices hit user-defined thresholds.

## Features

- Track multiple cryptocurrencies with customizable alert rules
- Alert when price goes above or below a threshold (with configurable tolerance)
- Hourly automated price checks via Celery Beat
- Price history stored in the database
- REST API to manage tracked coins and view snapshots
- Telegram notifications when alert conditions are met

## Tech Stack

- **Django** + **Django REST Framework**
- **Celery** + **Celery Beat** for task scheduling
- **Redis** as the message broker
- **CoinGecko API** for price data
- **Telegram Bot API** for notifications
- **Docker** / **Docker Compose**
- **Vue.js** for the frontend

## TODO

- [ ] Fix frontend graphics
- [ ] Deploy on AWS
