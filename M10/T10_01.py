import os
def clr(): os.system('cls')

class GameState(object):
    name = "menu"
    diperbolehkan = []
    def switch(self, state):
        if(state.name in self.diperbolehkan):
            print(f"Berganti dari state {self.name} menjadi {state.name}")
            self.__class__ = state
        else:
            print(f"Perpindahan ke state {state.name} tidak memungkinkan !")

class Menu(GameState):
    name = "menu"
    diperbolehkan = ["play"]

class Play(GameState):
    name = "play"
    diperbolehkan = ["pause", "gameover"]

class Pause(GameState):
    name = "pause"
    diperbolehkan = ["play", "menu"]

class Gameover(GameState):
    name = "gameover"
    diperbolehkan = ["menu"]

class Game(object):
    def __init__(self):
        self.state = Menu()
    def change(self, state):
        self.state.switch(state)

clr()
mygame = Game()
mygame.change(Play)

