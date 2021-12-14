class Cliente:
    
    
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        print("Camando @property nome()")
        return self.__nome.title()
    
    @nome.setter
    def nome(self,nome):
        print("Camando @property nome()")
        self.__nome = nome