from abc import ABC, abstractmethod

class washing :
    @abstractmethod
    def wash(self):
        pass

class drying:
    @abstractmethod
    def dry(self):
        pass

class expertMachine(washing, drying):
    def wash(self):
        pass
    def dry(self):
        pass

class simpleMachine(washing):
    def wash(self):
        pass