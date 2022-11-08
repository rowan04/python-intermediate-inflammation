# file: inflammation/models.py - write code her

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study"""
    def __init__(self, name: str):
        super().__init__(name)
        self.observations = []

    @property
    def last_observation(self):
        return self.observations[-1]


    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1
            except IndexError:
                day = 0

        new_observation = {
            'day': day,
            'value': value,
        }

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation

#tests

# alice = Patient('Alice')
# print(alice.name)
# observation = alice.add_observation(3)
# print(observation)
# print(alice.observations)

# alice = Patient("Alice")
# alice.add_observation(3)
# print("Last observation was: ", alice.last_observation)
# alice.add_observation(1)
# print("Last observation was: ", alice.last_observation)