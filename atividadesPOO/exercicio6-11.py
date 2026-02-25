#6. Escreva a classe Usuario e adicione as propriedades e o método (em Python):
class Usuario():
    primeiro_nome = ""
    sobrenome = ""
    def hello(self):
        return f"Olá {self.primeiro_nome} {self.sobrenome}, blz?"
#7. Crie a primeira instância e chame-a de usuario1.
usuario1 = Usuario()
#8. Defina os valores do primeiro e último nome para usuario1.
usuario1.primeiro_nome = "Matheus"
usuario1.sobrenome = "Bernardes"
#9. Obter o nome e sobrenome do usuário e imprima-os na tela com o comando print.
print(usuario1.primeiro_nome)
print(usuario1.sobrenome)
#10. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao usuário.
print(usuario1.hello())
#11. Crie (instancie) outro objeto. Chame-o de usuario2, dê a ele o primeiro nome de “Jane” e o sobrenome de “Silva”, e depois diga “Olá” ao usuário.
usuario2 = Usuario()
usuario2.primeiro_nome = "Jane"
usuario2.sobrenome = "Silva"
print(usuario2.hello())