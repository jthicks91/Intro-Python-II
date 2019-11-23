class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def inpsect(self):
        return "No Info"

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name,description)
        self.calories = calories

class Gold(Item):
    def __init__(self, value):
        super().__init__('Gold', 'Its shiny')
        self.value = value
        
    def inspect(self):
        return f'This gold is worth: {self.value}'


        # banana = Food('banana', 'its yellow', 100)

        #consume function treat like inspet function; 