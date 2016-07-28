import pynder
import auth
import time
import logging
from datetime import datetime

session = pynder.Session(auth.facebook_id, auth.token)
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(message)s')
logging.basicConfig(filename='friends.log', level=logging.WARNING, format='%(message)s')

def like_users():
    while True:
        try:
            users = session.nearby_users()
            for user in users:
                print(user.name)
                logging.info("=" * 50)
                logging.info(user.name + ", " + str(user.age))
                logging.info("School: " + str(user.schools))
                logging.info("-" * 50)
                logging.info("Instagram: " + str(user.instagram_username))
                logging.info("Distance: " + str(user.distance_km))
        except pynder.errors.RequestError:
            continue

def view_friends():
    friends = session.get_fb_friends()
    print(", ".join([x.name for x in friends]))

    user_info_objects = []
    for friend in friends:
        user_info_objects.append(friend.get_tinder_information())

    for user_info, friend in zip(user_info_objects, friends):
        logging.warning("=" * 50)
        logging.warning(friend.name)
        logging.warning(friend.facebook_link)
        logging.warning(user_info.bio)

like_users()
