from abc import ABC, abstractmethod

# Abstraksi Developer
class Developer(ABC):
    @abstractmethod
    def develop(self):
        pass

# Backend Developer
class BackendDeveloper(Developer):
    """This is a low-level module"""
    def develop(self):
        return "Writing Python Code"

# Frontend Developer
class FrontendDeveloper(Developer):
    """This is a low-level module"""
    def develop(self):
        return "Writing JavaScript Code"

# Developers Manager
class Developers:
    """An Abstract module"""
    def __init__(self, developers):
        self.developers = developers

    def develop(self):
        tasks = [developer.develop() for developer in self.developers]
        return "\n".join(tasks)

# High-Level Project
class Project:
    """This is a high-level project"""
    def __init__(self):
        self.__developers = Developers([
            BackendDeveloper(),
            FrontendDeveloper()
        ])
    def develops(self):
        return self.__developers.develop()

# Eksekusi
project = Project()
print(project.develops())
