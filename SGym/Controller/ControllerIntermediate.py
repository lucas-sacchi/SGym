from Controller import ControllerDecorator

# Controller intermediador do decorator 
class ControllerIntermediate(ControllerDecorator):
    def __init__(self, controller: ControllerDecorator):
        self._controller = controller

    def verificaLogin(self, email, senha, lista):
        return self._controller.verificaLogin(email, senha, lista)

    def getUserByEmail(self, email, lista):
        return self._controller.getUserByEmail(email, lista)

    def loadData(self, persistencia, controlador):
        self._controller.loadData(persistencia, controlador)

    def saveData(self, persistencia, controlador):
        self._controller.saveData(persistencia, controlador)