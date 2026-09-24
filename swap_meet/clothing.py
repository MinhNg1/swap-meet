from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, age=None, fabric="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        item_str = super().__str__()
        item_specific_str = f"It is made from {self.fabric} fabric."

        return " ".join((item_str, item_specific_str))