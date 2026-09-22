from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric

    def __str__(self):
        item_str = super().str()
        fabric_str = f"It is made from {self.fabric} fabric."

        return " ".join((item_str,fabric_str))