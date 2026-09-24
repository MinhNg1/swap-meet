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

    def get_by_category(self, category):

        item_list = []
        for item in self.inventory:
            if item.get_category() == category:
                item_list.append(item)

        return item_list

    def get_best_by_category(self, category):

        best_item_list = self.get_by_category(category)
        best_item_condition = 0
        best_item = None

        for item in best_item_list:
            if item.condition > best_item_condition:
                best_item_condition = item.condition
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory: 
            return False

        my_priority_item = self.get_best_by_category(their_priority)
        their_priority_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_priority_item, their_priority_item) 

    # Swap the first newest
    def swap_by_newest(self, other_vendor):
        if not self.inventory or not other_vendor.inventory: 
            return False

        my_newest_item = self.inventory[0]
        their_newest_item = other_vendor.inventory[0]

        for item in self.inventory:
            if item.age is None:
                continue

            if item.age < my_newest_item.age:
                my_newest_item = item

        for item in other_vendor.inventory:
            if item.age is None:
                continue

            if item.age < their_newest_item.age:
                their_newest_item = item        

        if my_newest_item.age is None or their_newest_item.age is None:
            return False
        
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)