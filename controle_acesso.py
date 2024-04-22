import abc
from funcionarios import *

class ControleDeAcesso(abc.ABC):
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def realizaLogin(self,empresa,username,senha):
        pass