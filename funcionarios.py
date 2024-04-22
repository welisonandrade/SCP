import abc
from empresa import Empresa
from controle_acesso import ControleDeAcesso
import calendar
from datetime import *
import time

class Funcionario(abc.ABC):
    def __init__(self,nome,cargo,setor,cpf):
        self._nome = nome  
        self._cargo = cargo
        self._setor = setor
        self._cpf = cpf
        self._temLogin = False
        self._username = nome
        self._senha = cpf
        self._historico = {}
    
    def __str__(self):
        nome = 'Nome: ' + self._nome + '\n'
        cargo = 'Cargo: ' + self._cargo + '\n'
        setor = 'Setor: ' + self._setor + '\n'
        cpf = 'CPF: ' + self._cpf + '\n'
        info = nome + cargo + setor + cpf
        return info

    @property
    def getHistorico(self):
        return self._historico

    def imprimirHistorico(self):
        print(self._historico)
 

    def registraPonto(self):
        pass


class Admin(Funcionario):
    def __init__(self,nome,cargo,setor,cpf):
        super().__init__(nome,cargo,setor,cpf)
        self._senhaAdmin = 'iamtheboss'

    @property
    def imprimir(self):
        print(self._nome)
        print(self._cargo)
        info = self._nome + '\n' + self._cargo
        return info

    def cadastraLogin(self,funcionario,empresa):
        funcionario._temLogin = True
        empresa.getFuncionarios[funcionario._cpf] = funcionario

    @property
    def getSenha(self):
        return self._senhaAdmin

    @property
    def getName(self):
        return self._nome

    def registraPonto(self):
        pass

class NotAdmin(Funcionario):
    def __init__(self,nome,cargo,setor,cpf):
        super().__init__(nome,cargo,setor,cpf)

    def realizaLogin(self,empresa,username,senha):
        loga = False
        for obj in empresa._funcionarioLogaveis.values():
                if obj._username == username:
                    if obj._senha == senha:
                        loga = True
                        return obj
        if loga == False:
            return loga

    def registraPonto(self):
        data_atual = date.today().strftime('%d/%m/%y')
        hora_atual = time.strftime('%H:%M:%S')
        tam = False
        
        if data_atual not in self._historico:
            self._historico[data_atual] = []
            self._historico[data_atual].append(hora_atual)
            print('\nPonto de entrada registrado com sucesso!')
        
        else:
            tam = 0
            for x in self._historico.keys():
                if data_atual == x:
                    for y in self._historico[data_atual]:
                        tam += 1
            if tam == 2: 
                print('\nVocê só pode registrar dois pontos por dia.')
            else:
                self._historico[data_atual].append(hora_atual)
                print('\nPonto de saída registrado com sucesso!')