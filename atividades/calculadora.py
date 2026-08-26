class Calculadora:

    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"Adição: {a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"Subtração: {a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"Multiplicação: {a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        try:
            resultado = a / b
            self.historico.append(f"Divisão: {a} / {b} = {resultado}")
            return resultado
        except ZeroDivisionError:
            return "Erro, divisão por zero não é permitida"

    def mostrar_historico(self):
        if not self.historico:
            print("Nenhum cálculo realizado ainda.")
            return
        print("\nHistórico de operações:")
        for i, item in enumerate(self.historico, 1):
            print(f"{i}. {item}")


def menu():
    calc = Calculadora()

    while True:
        print("\n--- CALCULADORA ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Mostrar histórico")
        print("6. Encerrar programa")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "6":
            print("Encerrando calculadora!")
            break

        if opcao == "5":
            calc.mostrar_historico()
            continue

        if opcao in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Escolha o primeiro número: "))
                num2 = float(input("Escolha o segundo número: "))
            except ValueError:
                print("Entrada inválida! Digite apenas números!")
                continue

            if opcao == "1":
                resposta = calc.somar(num1, num2)
            elif opcao == "2":
                resposta = calc.subtrair(num1, num2)
            elif opcao == "3":
                resposta = calc.multiplicar(num1, num2)
            elif opcao == "4":
                resposta = calc.dividir(num1, num2)

            print(f"Resultado: {resposta}")
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()