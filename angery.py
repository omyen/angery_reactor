from fbchat import Client
from fbchat.models import *
import argparse

class AngeryReactor(Client):
    def __init__(self, email, password, enemy_name):
        super(AngeryReactor, self).__init__(email, password)
        users = self.searchForUsers(enemy_name)
        self.user = users[0]

        print("Enemy found:")
        print("Enemy's ID: {}".format(self.user.uid))
        print("Enemy's name: {}".format(self.user.name))
        print("Enemy's profile picture URL: {}".format(self.user.photo))
        print("Enemy's main URL: {}".format(self.user.url))

    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        if author_id == self.user.uid:
            print("Enemy messaged you!")
            self.reactToMessage(mid, MessageReaction.ANGRY)

parser = argparse.ArgumentParser(description='Angry react all your enemy\'s messages on Facebook Messenger!')
parser.add_argument('email', type=str, help='Your email to log in with')
parser.add_argument('password', type=str, help='Your password to log in with')
parser.add_argument('enemy', type=str, help='The full name of your enemy')

args = parser.parse_args()

client = AngeryReactor(args.email, args.password, args.enemy)
client.listen()
