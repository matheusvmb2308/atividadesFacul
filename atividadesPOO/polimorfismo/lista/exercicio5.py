"""
5. Crie uma classe Empregado com um método pagar_salario(). Em seguida, crie duas classes
filhas, EmpregadoHora e EmpregadoMes, que herdam da classe Empregado. Cada uma das
classes filhas deve ter seu próprio método pagar_salario() que calcula o salário com base no
número de horas trabalhadas ou no salário mensal, respectivamente. Em seguida, crie uma lista de
funcionários que inclua um funcionário horista e um funcionário mensalista. Por fim, itere sobre a
lista e chame o método pagar_salario() de cada funcionário.
"""
class Empregado:
    def pagar_salario(self):
        pass
class EmpregadoHora(Empregado):
    def __init__(self, horas):
        self.horas = horas
    def pagar_salario(self):
        return f"Você recebeu {10 * self.horas}"
class EmpregadoMes(Empregado):
    def __init__(self, salario):
        self.salario = salario
    def pagar_salario(self):
        return f"Vocẽ recebeu {self.salario}"
funcionario_hora1 = EmpregadoHora(5)
funcionario_mes1 = EmpregadoMes(2000)
funcionario_hora2 = EmpregadoHora(10)
funcionario_mes2 = EmpregadoMes(4000)
empregados = [funcionario_hora1, funcionario_hora2, funcionario_mes1, funcionario_mes2]
for empregado in empregados:
    print(empregado.pagar_salario())