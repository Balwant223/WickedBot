# WickedBot
Clone project then move to Project Directory.
run pip install -r requirements.txt
You must install Redis server. I've used it for channel layers and group room join.
Follow instructions from this(https://redis.io/topics/quickstart) link to install Redis.
Move to redis directory then run 'src/redis-server'
(For linux os)
Install postgresql then create role and databse then update redis layer and databse settings in settings.py in WickedBot folder.
Then run 'python manage.py makemigrations' and 
'python manage.py migrate' then 'python manage.py runserver'
