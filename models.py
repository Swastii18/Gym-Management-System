from datetime import datetime

class Member:
    def __init__(self, name, age, membership_type, start_date):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "membership_type": self.membership_type,
            "start_date": self.start_date.strftime('%Y-%m-%d')
        }
