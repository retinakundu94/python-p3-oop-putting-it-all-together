#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand: str, size: int):
        self.brand = brand
        self._size = size
        self.is_repaired = False
        self.condition = "Used"  

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value: int):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.is_repaired = True
        self.condition = "New"  
        print("Your shoe is as good as new!")
