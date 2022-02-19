import random
import string
import random

class Robot:
    def __init__(self):
        Robot.reset(self)
    def reset(self):
        self.name=generate_name()
def generate_name():
    random.seed()
    name=""
    for i in range(0,2):
        name+=random.choice(string.ascii_uppercase)
    for i in range(0,3):
        name+= random.choice(string.digits)
    return name
