"""
• Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""
"""
• Crie uma "porta escondida" no programa do bichinho virtual que mostre os valores exatos dos
atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu,
for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
Comentario: Fiz uma leve alteração na atividade.
"""
import threading
import time
import os
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
def diminuiVidaSaude(personagem):
    while True:
        time.sleep(5) # Espera 1 segundo
        # Supondo que sua classe tenha esses métodos
        personagem.setFome()
        personagem.setSaude() 
        print(personagem.getMostraDados())
        # Opcional: Se a vida chegar a 0, você pode tratar aqui
        if personagem.saude <= 0 or personagem.fome <= 0:
            print("\n[AVISO] Seu Tamaguchi morreu! Pressione Enter para sair.")
            break
def passar_tempo_idade(personagem):
    while True:
        time.sleep(20)
        personagem.setAlterarIdade()

tamaguchi = Bichinho("Tamaguchi", 20, 20, 30)
t = threading.Thread(target=diminuiVidaSaude, args=(tamaguchi,), daemon=True)
t.start()
t2 = threading.Thread(target=passar_tempo_idade, args=(tamaguchi,), daemon=True)
t2.start()
print(tamaguchi.getMostraDados())
alimentos = {"maçã": 10, "uva": 20, "banana": 30, "ameixa": 40}
while True:
    print("TAMAGUCHI", tamaguchi.getMostraDados())
    print("[1] ALTERAR NOME")
    print("[2] BRINCAR COM O TAMAGUCHI")
    print("[3] ALIMENTAR O TAMAGUCHI")
    print("[?] PORTA ESCONDIDA")
    print("[4] SAIR")
    opcao = int(input("Escolha uma opção: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == 1:
        nome = str(input("Novo nome: "))
        tamaguchi.alterarNome(nome)
    if opcao == 2:
        tempo = int(input("Quanto tempo vocês brincaram?: "))
        tamaguchi.setBrincar(tempo)
    if opcao == 3:  
        for i in alimentos.keys():
            print(i.upper(), " ganha: ", alimentos[i], " pontos de saúde")
        fruta = str(input("Escolha uma fruta: "))
        while fruta.lower() not in alimentos:
            fruta = str(input("Escolha uma fruta que esteja disponível: "))
        tamaguchi.alimentar(alimentos[fruta.lower()])
    if opcao == 10:
        tamaguchi.portaEscondida()
        input("Enter para sair")
    if opcao == 4:
        break