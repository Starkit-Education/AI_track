import json
import math

class Localization():
    def __init__(self, landmarks = "landmarks.json"):
        with open(landmarks, "r") as file:
            self.landmarks = json.load(file)
        self.position = ()

    def update(self, mesurements):
        
        """
        Здесь будет ваш код
        """
        pass

    def return_position(self):
        return self.position
        