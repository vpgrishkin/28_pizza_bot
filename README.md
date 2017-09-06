# Telegram Bot for Pizzeria

The telegram bot for a pizzeria. Send "/menu" and get the pizzeria catalog.

# How to Use

## Step 1. Install virtual environment and requirements

``` #!bash

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Step 2. Import a catalog from json to the database

``` #!bash

python manage_db.py -c db
python manage_db.py -j [json_file]
```

JSON file example:
```
[
    {
        "title": "Маргарита",
        "description": "соус,сыр Моцарелла",
        "choices": [
            {
                "title": "30 см (450гр)",
                "price": 360
            },
            {
                "title": "40 см (750гр)",
                "price": 460
            }
        ]
    },
    {
        "title": "Маргарита <Помидоро>",
        "description": "соус,сыр Моцарелла,помидоры",
        "choices": [
            {
                "title": "30см (500гр)",
                "price": 400
            },
            {
                "title": "40cм (850гр)",
                "price": 490
            }
        ]
    }
]
```

## Step 3. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

## Step 4. Config environment add your values:

### Linux, example:
``` #!bash
export ADMIN_LOGIN='admin'
export ADMIN_PASSWORD='password'
export SECRET_KEY='your secret key'
export DATABASE_URI='sqlite:////Users/youruser/Python/28_pizza_bot/app.db'
export BOT_TOKEN="you_bot_token"
```
### Windows: use 'SET'

## Step 5. Run the bot

``` #!bash

python bot.py
```

## Step 6. Run the sever to open the admin panel

``` #!bash

python server.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
