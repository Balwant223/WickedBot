### _How to Run_

- Clone project and move to project root directory. 
- Activate python environment .
- Update your pip to latest version otherwise installing requirements will give you error.
- Upgrade pip by running ```pip install --upgrade pip``` . 
- Then run ```pip install -r requirments.txt``` .
- Install and setup postgresql and create Role and Database .
- Then add Database configuration at settings.py of WickedBot directory .
- Also install Redis server for channel layer from this [link](https://redis.io/download) .
- If you don't want redis then config CHANNEL_LAYER setting in settings.py for InMemoryCache (Extra Info available [here](https://channels.readthedocs.io/en/stable/topics/channel_layers.html#:~:text=channel_layer%20.-,Redis%20Channel%20Layer,to%20install%20the%20channels_redis%20package.) .
- Start redis server by going to redis directory and then run ```src/redis-server``` (only in linux os) .
- then from project root run ```python manage.py makemigrations``` and ```python manage.py migrate```  (you might have to add app name(chat) after makemigration-: ```python manage.py makemigrations chat```  .
- Then Finally run ```python manage.py runserver```) .

## Features
- Visit ```http://localhost:8000/chat/room/``` then enter your name and start talking to Bot.
- If you want every users Joke Calls count and Total individual Joke calls then visit ```http://localhost:8000/chat/calls/``` .
- Thank You

### If you get any issues please email me balwantdod223@gmail.com .
