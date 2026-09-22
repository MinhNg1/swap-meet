class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        if item:
            self.inventory.append(item)
            return item

        return None

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return None

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None