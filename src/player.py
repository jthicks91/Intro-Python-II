# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curr_room):
        self.name = name ## will try to write something for custom input for name for program, this will do for now.
        self.curr_room = curr_room 
        self.inventory = []
        # self.health  = 100 ## will implement later
    
    # def input for custom name input?? 

    def add_item(self, item):
        self.inventory.append(item)
        print(f'Well Done! {self.name} has picked up {self.inventory}!')

    def __str__(self):
        return f'{self.name} is in the {self.curr_room}'

    # def change_location(self, new_location):
    #     self.new_location = new_location

print(Player)