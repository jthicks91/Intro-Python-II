# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        # self.n_to = None
        # self.s_to = None
        # self.w_to = None
        # self.e_to = None
        

        #where to include items? in rooms or on players or both??

    # def retrieve_direction(self,command):
    #     if command == 'n':
    #         return self.n_to
    #     elif command == "s":
    #         return self.s_to
    #     elif command == "w":
    #         return self.w_to
    #     elif command == "e":
    #         return self.e_to
    #     else:
    #         return None

    # def str  print room and description nicely 