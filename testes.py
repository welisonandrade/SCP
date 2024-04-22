import calendar
from datetime import *
import time
class Teste():
    def __init__(self):
        self._dicio = {}
    
    def adiciona(self,pessoa):
        self._dicio['123'] = (pessoa)

    def adiciona2(self,pessoa):
        self._dicio['321'] = (pessoa)

    def getDicio(self):
        return self._dicio

class Pessoa():
    def __init__(self,nome, cargo, setor):
        self._nome = nome
        self._cargo = cargo
        self._setor = setor
    
    def __str__(self):
        return self._nome + ' ' + self._cargo + ' ' + self._setor
        

teste = Teste()
pessoa1 = Pessoa('Welison', 'Gerente', 'RH')
pessoa2 = Pessoa('Flávio', 'Dev', 'Front-end')


teste.adiciona(pessoa1)
teste.adiciona2(pessoa2)

a = teste.getDicio()
# print(a , 'aqui')

nome = 'Welison'
senha = 'Dev'


# for cpf in a.items():
#     print(cpf, ' testeee')
#     for y in cpf[1]:
#         print(y)
#         if nome == y._nome:
#             print('nome existe')
#             if senha == y._cargo:
#                 print('senha tbm existe')
#             else:
#                 print('usuário certo mas senha errada')


# for cpf in a.values():
#     print(cpf, ' testeee')
#     if nome == cpf._nome:
#         print('nome existe')
#         if senha == cpf._cargo:
#             print('senha tbm existe')
#         else:
#             print('usuário certo mas senha errada')



#  for lista_obj in empresa.getFuncionarios.values():
#             for obj in lista_obj:
#                 if obj._username == username:
#                     print('usuario correto')
#                     if obj._senha == senha:
#                         print('senha correta')
#                         print(obj)


dicio = {
    'Data atual': ['entrada','saida']
}

#Quantos dias tem o mês
qtd_dia_mes = calendar.monthrange(2022,5)
print('O mês de maio tem: ',end='')
print(qtd_dia_mes[1],end=' dias.')

# Pega data atual
print('\nA data de hoje é: ',end=' ')
data_atual = date.today().strftime('%d/%m/%y')
print(data_atual)

# Pega horário atual
hora_atual = time.strftime('%H:%M:%S')
print('A hora atual é: ',end='')
print(hora_atual)