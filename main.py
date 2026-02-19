""" Ao invés de criar funções separadas para cada operação matemática, este código define uma classe chamada Calculadora que encapsula 
as operações de soma, subtração, multiplicação e divisão. A classe é inicializada com dois números e possui métodos para realizar cada 
operação."""
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def soma(self):
        return self.num1 + self.num2
    def subtracao(self):
        return self.num1 - self.num2
    def multiplicacao(self):
        return self.num1 * self.num2
    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Erro: Divisão por zero não é permitida."

"""Uso da classe Calculadora para realizar operações com dois números fornecidos pelo usuário. 
O programa solicita ao usuário que insira dois números, cria uma instância da classe Calculadora 
com esses números e exibe os resultados das operações de soma, subtração, multiplicação e divisão."""
def menu():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Digite a opção (1/2/3/4/5): ")
    return escolha

def main():
    while True: 
        escolha = menu()
        
        if escolha == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        try:                                          
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            continue                                

        calculadora = Calculadora(num1, num2)

        if escolha == '1':
            print(f"Soma: {calculadora.soma():.2f}")
        elif escolha == '2':
            print(f"Subtração: {calculadora.subtracao():.2f}")
        elif escolha == '3':
            print(f"Multiplicação: {calculadora.multiplicacao():.2f}")
        elif escolha == '4':
            resultado = calculadora.divisao()
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Divisão: {resultado:.2f}")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()