from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, age=None, type="Unknown"):
        super().__init__(id, condition, age)
        self.type = type

    def __str__(self):
        item_str = super().__str__()
        item_specific_str = f"This is a {self.type} device."

        return " ".join((item_str, item_specific_str))
