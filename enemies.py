# modules
import random
random.seed()

# Name list
list_names = ['Bob', 'Richard', 'Aaron', 'Arthur', 'Henry', 'Frank', 'Edward', 'Albert','James', 'John', 'Walter',
              'Roy', 'Louis', 'Carl', 'Paul', 'Pedro', 'Samuel', 'Raymond', 'Howard', 'Oscar', 'Leo', 'Jack', 'Lee']


# Bandit class
class Bandit:
    # constructor
    def __init__(self):
        self.name = random.choice(list_names)
        print(self.name)
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

