import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_swap_newest_item():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    # Assert
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert not item_a in tai.inventory
    
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert not item_d in jesse.inventory


def test_swap_newest_item_no_inventory_returns_false():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    # Assert
    assert result == False
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_newest_item_no_other_vendor_inventory_returns_false():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    # Assert
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

def test_swap_newest_item_no_age_returns_false():
    # Arrange
    item_a = Decor()
    item_b = Electronics()
    item_c = Decor()
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing()
    item_e = Decor()
    item_f = Clothing()
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    # Assert
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
