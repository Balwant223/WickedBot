# WickeBot
### _How to Run_

- Clone project and move to project root directory. 
- Activate python environment .
- Update your pip to latest version . 
- Then run ```pip install -r requirments.txt``` .
- Install and setup postgresql and create Role and Database .
- Then add Database configuration at settings.py of WickedBot directory .
- Also install Redis server for channel layer from this link .
- If you don't want redis then config CHANNEL_LAYER setting in settings.py for InMemoryCache (Extra Info available here) .
- Start redis server by going to redis directory and then run ```src/redis-server``` (only in linux os) .
- then from project root run ```python manage.py makemigrations``` and ```python manage.py migrate``` .
- Then Finally run ```python manage.py runserver``` .

## Features
