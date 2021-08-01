import json
import random

from faker import Faker


class FakeUser:
    def __init__(self, name=None, email=None, gender=None, status=None):
        factory = Faker()
        self.id = None
        self.name = name if name else factory.first_name()
        self.email = email if email else factory.email()
        self.gender = gender if gender else random.choice(["male", "female"])
        self.status = status if status else random.choice(["active", "inactive"])

    def get_user_info_in_json(self):
        """data as payload for POST request"""
        return json.dumps({"name": self.name, "gender": self.gender, "email": self.email, "status": self.status})
