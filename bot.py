import config
import pynder
from datetime import datetime
import sys
import logging

session = pynder.Session(config.facebook_id, config.auth_token)
logging.basicConfig(filename="run.log", level=logging.INFO)

while True:
    try:
        for user in session.nearby_users():
            print(user.name)
            logging.info(' User: ' + user.name + " Instagram: " + str(user.instagram_username))
            user.like()
    except ValueError:
        continue
