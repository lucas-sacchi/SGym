from abc import ABC, abstractmethod

class Decorator(ABC):

    @abstractmethod
    def verificaLogin(self, email, senha, lista):
        pass

    @abstractmethod
    def getUserByEmail(self, email, lista):
        pass

    @abstractmethod
    def loadData(self, controlador):
        pass

    @abstractmethod
    def saveData(self, controlador):
        pass

    
