class Calculadora:
    def __init__(self):
        self.historico = []
    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"Adição: {a} + {b} = {resultado}")
        return resultado
    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"Adição: {a} - {b} = {resultado}")
        return resultado
    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"Multiplicação: {a} * {b} = {resultado}")
        return resultado
    def dividir(self, a , b):
        try:
            resultado = a / b
            self.historico.append(f"Divisão: {a} / {b} = {resultado}")
            return resultado
        except ZeroDivisionError:
            return "Erro, divisão por zero não é permitido"
    
    def mostrar_historico(self):
        print("Histórico de operações: ")


    def menu():
        calc = Calculadora()

        while True:
            print("/n ---CALCULADORA---")
            print("1. soma")
            print("2. subtração")
            print("3. multiplicação")
            print("4. divisão")
            print("5. mostrar histórico")
            print("6. Encerrar programa")

            opcao = input("Escolha uma opção (1-6)")

            if opcao == "6":
                print("Encerrando calculadora!")
                break

            if opcao in ("1", "2", "3", "4", "5"):
                try:
                    num1 = float(input("Escolha o primeiro número: "))
                    num2 = float(input("Escolha o segundo número: "))
                except ValueError:
                    print("Entrada inválida! Digite apenas números!")
                continue

            if opcao == "1":
                resposta = calc.somar(num1 , num2)
            elif opcao == "2":
                resposta = calc.subtrair(num1 , num2)
            elif opcao == "3":
                resposta = calc.multiplicar(num1 , num2)
            elif opcao == "4":
                resposta = calc.dividir(num1 , num2)

            print(f"Resultado {resposta}")
        else:
            print("Opção inválida!")




            


             
            


    