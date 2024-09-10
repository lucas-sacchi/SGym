from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def leituraCadastro(self, controlador):
        pass

    @abstractmethod
    def escritaUser(self, user):
        pass

    @abstractmethod
    def persistenciaCadastro(self, controlador):
        pass

    @abstractmethod
    def deleteUserByEmail(self, email):
        pass


    
