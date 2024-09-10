from Controller.Decorator import Decorator

# Classe onde as funções estão implementadas
class ControllerDecorator(Decorator):
    
    def verificaLogin(self, email, senha, lista):
        tipo = -1
        for user in lista:
            if user.email == email and user.senha == senha:
                tipo = user.tipo
        return tipo
    
    def getUserByEmail(self, email, lista):
        for user in lista:
           if user.email == email:
               return user
        return None 

    def loadData(self, persistencia, controlador):
        persistencia.leituraCadastro(controlador)

    def saveData(self, persistencia, controlador):
        persistencia.persistenciaCadastro(controlador)
