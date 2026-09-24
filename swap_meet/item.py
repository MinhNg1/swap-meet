import uuid

class Item:
    def __init__(self, id=None, condition=0, age=None) -> None:
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        condition = self.condition
        
        if condition == 0:
            return "Sell as is. Use as part only"
        elif condition == 1:
            return "fair"
        elif condition == 2:
            return "good"
        elif condition == 3:
            return "very good"
        elif condition == 4:
            return "exellent, like new"
        elif condition == 5:
            return "New, never used"
        else:
            return "Unknown" 

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
