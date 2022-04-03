# Telegram Local

Full example of Telegram local application.

## Contains

### Telegram Bot API

Local Telegram Bot API server based
on [aiogram Bot API Server image](https://github.com/aiogram/telegram-bot-api) \
There's no public ports and no domain names needed. \
All connections are made within docker network.

### Echo Bot

Telegram echo-bot based on [aiogram 3.x](https://docs.aiogram.dev/en/dev-3.x/) \
Bot receives updates from local Telegram Bot API via webhooks. \
All requests are sending also to local Telegram Bot API.

### Reverse Proxy

nginx reverse proxy is serving static files and API server

## Installation

Copy `examples/example.env` to your `.env` file. \
Fill all uncommented variables in `.env` files. \
Uncomment and fill other variables if you want to use them.

## Usage

Run `docker-compose up -d` to start.

## Development

Fill free to copy this project and edit it as you wish.

## Contribution

Fill free to send issues and pull requests.
