class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory: 
            return False

        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory: 
            return False

        return self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
