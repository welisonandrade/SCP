class Empresa:
    def __init__(self):
        self._funcionarioLogaveis = {}

    def __str__(self):
        return self._funcionarioLogaveis

    @property
    def getFuncionarios(self):
        return self._funcionarioLogaveis

    def imprimirF(self):
        for x in self._funcionarioLogaveis.values():
            print(x)

    def imprimirFName(self):
        for item in self._funcionarioLogaveis.values():
            print('\nNome: ',item._nome,'\n','CPF: ',item._cpf)