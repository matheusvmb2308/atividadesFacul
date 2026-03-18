"""
• Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles
através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário
tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu
deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os
bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa
mais interessante, dê para cada bichinho um nível inicial aleatório de fome e tédio.
"""
import threading
import time
import os
import random
class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.setHumor()
    def setHumor(self):
        if self.fome < 50 or self.saude < 50:
            if self.fome < 10 or self.saude < 10:
                self.humor = "Depressivo"
                return
            else:
                self.humor = "Triste"
            return
        elif self.fome >= 50 and self.saude >= 50:
            if self.fome > 80 and self.saude > 80:
                self.humor = "Animado"
            else:
                self.humor = "Feliz"
    def alterarNome(self, nome):
        self.nome = nome
    def setSaude(self):
        self.saude -= 1
        self.setHumor()
    def setFome(self):
        self.fome -= 1
        self.setHumor()
    def alimentar(self, quantidade):
        self.fome += quantidade
        if self.fome > 100:
            self.fome = 100
    def setBrincar(self, tempo_brincando):
        self.fome -= tempo_brincando / 2
        self.saude += tempo_brincando / 2
        if self.saude > 100 and self.fome > 100:
            self.saude = 100
            self.fome = 100
    def setAlterarIdade(self):
        self.idade += 1
    def portaEscondida(self):
        print("PARABÈNS!")
        print("VOCÊ ACHOU O TAMAGUCHI ESCONDIDO!!")
        ascii_art = r'''
         .^._.^.
         | . . |
        (  ---  )
        .'     '.
        |/     \|
         \ /-\ /
          V   V
        '''
        print(ascii_art)
    def getMostraDados(self):
        return f"\nNome: {self.nome}, Saúde: {self.saude}, Fome: {self.fome}, Humor: {self.humor}, Idade: {self.idade}"
alimentos = {"maçã": 10, "uva": 20, "banana": 30, "ameixa": 40}
def diminuiVidaSaude(lista_bichinhos):
    while True:
        time.sleep(5) # Espera 1 segundo
        # Supondo que sua classe tenha esses métodos
        for b in lista_bichinhos:
            b.setFome()
            b.setSaude() 
            print(b.getMostraDados())
        # Opcional: Se a vida chegar a 0, você pode tratar aqui
        if b.saude <= 0 or b.fome <= 0:
            print("\n[AVISO] Seu Tamaguchi morreu! Pressione Enter para sair.")
            break
def passar_tempo_idade(lista_bichinhos):
    while True:
        time.sleep(20)
        for b in lista_bichinhos:
            b.setAlterarIdade()
def aleatorio_saude():
    return random.randint(0, 100)
def aleatorio_fome():
    return random.randint(0, 100)
def mostraLista(lista):
    for b in lista:
        print(f"Dados: {b.getMostraDados()}")
def alterarNome(lista, nome_novo):
    for b in lista:
        b.alterarNome(nome_novo)
def brincar(lista, tempo):
    for b in lista:
        b.setBrincar(tempo)
def alimentar(lista, alimento):
    for b in lista:
        b.alimentar(alimentos[alimento.lower()])
tamaguchi = Bichinho("Tamaguchi", aleatorio_fome(), aleatorio_saude(), 0)
tamaguchi2 = Bichinho("Perolin", aleatorio_fome(), aleatorio_saude(), 0)
tamaguchi3 = Bichinho("Carlos", aleatorio_fome(), aleatorio_saude(), 0)
lista_bichinhos = [tamaguchi, tamaguchi2, tamaguchi3]
t = threading.Thread(target=diminuiVidaSaude, args=(lista_bichinhos ,), daemon=True)
t.start()
t2 = threading.Thread(target=passar_tempo_idade, args=(lista_bichinhos ,), daemon=True)
t2.start()
while True:
    mostraLista(lista_bichinhos)
    print("[1] ALTERAR NOME")
    print("[2] BRINCAR COM O TAMAGUCHI")
    print("[3] ALIMENTAR O TAMAGUCHI")
    print("[?] PORTA ESCONDIDA")
    print("[4] SAIR")
    opcao = int(input("Escolha uma opção: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == 1:
        nome = str(input("Novo nome: "))
        alterarNome(lista_bichinhos, nome)
    if opcao == 2:
        tempo = int(input("Quanto tempo vocês brincaram?: "))
        brincar(lista_bichinhos, tempo)
    if opcao == 3:  
        for i in alimentos.keys():
            print(i.upper(), " ganha: ", alimentos[i], " pontos de saúde")
        fruta = str(input("Escolha uma fruta: "))
        while fruta.lower() not in alimentos:
            fruta = str(input("Escolha uma fruta que esteja disponível: "))
        alimentar(lista_bichinhos, fruta)
    if opcao == 10:
        tamaguchi.portaEscondida()
        input("Enter para sair")
    if opcao == 4:
        break