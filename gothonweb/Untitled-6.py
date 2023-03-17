
this is my updated planisphere.py file including the start room.

however the display is not shown.

class Room(object):
    def __init__(self, name, description, picture=None):
        self.name = name
        self.description = description
        self.picture = picture
        self.paths = {}

    def go(self, direction):
        room = self.paths.get(direction, None)
        if room:
            room.on_enter()
        return room

    def add_paths(self, paths):
        self.paths.update(paths)

    def on_enter(self):
        if self.picture:
            print(f"Displaying image: {self.picture}")
            # code to display the image using your preferred graphics library
        print(self.description)


eck = Room("Am  Eck", 
"""
Du bist so am späten Abend am Eck. Wie immer alles irgendwie langweilig aber nachhause ist auch irgendwie kacke. Du denkst wie
immer, dass noch irgendwas gehen muss.  Du entscheidest dich noch kurz irgendwo hin zu gehen. Nur das Lu oder das ChinChilla haben noch auf. Worauf hast du Bock?
                
1 = Ins Lu
2 = Richtung Dobben
3 = Richtung Bellini
4 = Ins Chinchilla

""", "static/uploads/eck.png"
)
