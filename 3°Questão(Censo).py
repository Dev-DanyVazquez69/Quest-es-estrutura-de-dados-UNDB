import os
from time import sleep


class censo:
    def __init__(self):
        self.resultado = {}
        self.id = 0
        self.media = 0
    def menu(self):
        while True:
            print("-~" * 30)
            print('''
      Bem vindo a hamburgueria FaceBurg\n
      [1] participar do censo
      [2] Ver resultados
      [3] sair
      ''')
            print("-~" * 30)
            try:
                self.menu = int(input("=>>"))
                if self.menu == 1:
                    os.system("clear")
                    self.redirecionar()
                    os.system('clear')
                    print("β  β    Dados armazenados com sucesso   β  β ")
                elif self.menu == 2:
                    self.redirecionar()
                elif self.menu == 3:
                    os.system("clear")
                    sleep(1)
                    print(" ππ  obrigado por participar ππ ")
                    break
                else:
                    os.system('clear')
                    print(" β  β  Digite 1 ou 2  β  β  ")
                    sleep(1)
            except:
                os.system('clear')
                print(" β  β  Erro, digite apenas os numeros apresentados β  β  ")
                sleep(1)
                pass

    def redirecionar(self):
        if self.menu == 1:
            self.perguntas()
        elif self.menu == 2:
            self.mostrar_resultado()

    def perguntas(self):
        print("-~" * 30)
        self.nome = input("Digite seu nome => ")
        print("-~" * 30)
        self.idade = int(input("Digite sua idade => "))
        print("-~" * 30)
        self.sexo = input("Sexo[M/F]=> ").lower()
        print("-~" * 30)
        self.validar()

    def validar(self):
      self.media+=1
      if self.idade >=20 and self.idade <=30:
        os.system("clear")
        print(" β β β VoΓ§Γͺ possui idade entre 20 e 30 anos portanto serΓ‘ incluso no resultado β β β ")
        sleep(2)
        self.registrar()
      else:
        os.system("clear")
        print(" β β β VoΓ§Γͺ nΓ£o possui idade entre 20 e 30 anos portanto nΓ£o serΓ‘ incluso no resultado β β β ")
        sleep(2)
        pass
    def registrar(self):
      if self.sexo == "m":
        self.sexo = "Masculino"
      elif self.sexo == "f":
        self.sexo = "Feminino"
      self.resultado[self.id] = {
          "NOME": self.nome,
          "IDADE": self.idade,
          "SEXO": self.sexo
          }
      self.id += 1

    def mostrar_resultado(self):
        os.system("clear")
        print(
            f'''\n β β β{self.media} pessoa(s) participaram
            A pesquisa qualificou {len(self.resultado)} pessoa(s)
            {self.media/len(self.resultado)*100}% das pessoas que participaram tem idade entre 20 e 30 anos
            '''
        )
        input("Tecle enter para ver")
        os.system("clear")
        if len(self.resultado)>0:
          for s in range((len(self.resultado))):
              chave = self.resultado[s].keys()
              valor = self.resultado[s].values()
              valor = list(valor)
              chave = list(chave)
              for x in range(3):
                  print("~" * 20)
                  print(chave[x], ">>", valor[x])
              print("~" * 20)
              print("π " * 10)
        else:
          print("π  π  NΓ£o hΓ‘ candidatos vΓ‘lidos  π  π")
        input("\nTecle enter para voltar")
        os.system("clear")


dany = censo()
dany.menu()
