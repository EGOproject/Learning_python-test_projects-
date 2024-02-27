# instance
"""
class Activity:
    def __init__(self, name, category, type, description):
        self.name = name.capitalize()
        self.category = category
        self.type = type
        self.description = description
    
    def __str__(self):
        print(self.name, "is done", self.category, "with", self.type, "physicality.", "Briefly,", self.description)

    def about(self):
        print(self.name, "is done", self.category, "with", self.type, "physicality.", "Briefly,", self.description)


game = Activity("tennis", "indoor", "active", "it's played by swinging a bat to hit a small ball to either sides but the ball shouldn't bounce more than once on one side. Also a player is always required to hit the ball back to the oponent's side.")

game.about()
"""

# inheritance
class Activity:
    def __init__(self, name, type, category, energy):
        self.name = name
        self.type = type
        self.category = category
        self.energy = energy

    def __str__(self):
        pass

class Games(Activity):
    pass

class Chores(Activity):
    pass

class Leisure(Activity):
    pass

class Body(Activity):
    pass


tennis = Games("table tennis", "indoor", "active", "moderate")
washing = Chores("washing dishes", "indoor", "active", "moderate")


print(tennis.category)
print(washing.energy)