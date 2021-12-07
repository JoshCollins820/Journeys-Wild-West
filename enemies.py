# modules
import random


# Bandit class
class Bandit:
    # constructor
    def __init__(self):
        self.name = "Test"
        self.type = 1
        self.level = 1
        self.hp = 100
        self.x_location = 400

    # getters
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_x_location(self):
        return self.x_location

