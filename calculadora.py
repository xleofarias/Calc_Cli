import os

class Calculadora:
    def __init__(self):
        self.resultado: float
        self.operacao: int
        self.historico = []
       
    def escolher_operacao(self) -> None:
        escolher = int(input(
"""
Escolha a operação: 
[1] Somar 
[2] Subtrair 
[3] Mulplicar
[4] Dividir
[5] Histórico
[6] Sair:\n"""))
                
        if escolher < 7:
            if escolher == 1:
                self.somar()
            elif escolher == 2:
                self.subtrair()
            elif escolher == 3:
                self.multiplicar()
            elif escolher == 4:
                self.dividir()
            elif escolher == 5:
                self.mostrar_historico()
            elif escolher == 6:
                print("Fechando a calculadora")
                exit()
        else:
            raise Exception("O número precisa se de 1 a 6")
        self.operacao = escolher

    def somar(self) -> None:
        lista_numeros = self.obter_numeros()
        soma = lista_numeros[0]
        for n in lista_numeros[1:]:
            soma += n
        self.resultado = soma
        self.historico.append({'operacao': 'soma', 'resultado': self.resultado})
                   
    def subtrair(self) -> None:
        lista_numeros = self.obter_numeros()
        subtrai = lista_numeros[0]
        for n in lista_numeros[1:]:
            subtrai -= n
        self.resultado = subtrai
        self.historico.append({'operacao': 'subtração', 'resultado': self.resultado})
        
    def multiplicar(self) -> None:
        lista_numeros = self.obter_numeros()
        multiplica = lista_numeros[0]
        for n in lista_numeros[1:]:
            multiplica *= n
        self.resultado = multiplica
        self.historico.append({'operacao': 'multiplicação', 'resultado': self.resultado})

    def dividir(self) -> None:
        lista_numeros = self.obter_numeros()
        if lista_numeros[1] == 0:
            print("Erro: Divisão por Zero")
            return
        else:
            dividi = lista_numeros[0] / lista_numeros[1]
            self.resultado = dividi
            self.historico.append({'operacao': 'divisão', 'resultado': self.resultado})


    def mostrar_historico(self) -> None:
        if not self.historico:
            print("Nenhuma operação no histórico.")
        else:
            for indice, entrada in enumerate(self.historico):
                print(f"{indice}: {entrada['operacao']} = {entrada['resultado']}")
            self.usar_historico()

    def usar_historico(self) -> None:
        try:
            escolha = int(input("Escolha o índice do histórico para usar: "))
            if 0 <= escolha < len(self.historico):
                historico_resultado = self.historico[escolha]['resultado']
                self.resultado = historico_resultado
                print(f"Resultado selecionado do histórico: {self.resultado}")
                escolher = int(input(
"""
Escolha a operação: 
[1] Somar 
[2] Subtrair 
[3] Mulplicar
[4] Dividir
[5] Sair:
"""))
                if escolher == 1:
                    numero = float(input("Digite o número para somar com o histórico: "))
                    self.resultado += numero
                    print(f"{historico_resultado} + {numero} = {self.resultado}")
                    self.historico.append({'operacao': 'soma', 'resultado': self.resultado})             
                elif escolher == 2:
                    numero = float(input("Digite o número para subtrair com o histórico: "))
                    self.resultado -= numero
                    print(f"{historico_resultado} - {numero} = {self.resultado}")
                    self.historico.append({'operacao': 'subtração', 'resultado': self.resultado})
                elif escolher == 3:
                    numero = float(input("Digite o número para multiplicar com o histórico: "))
                    self.resultado *= numero
                    print(f"{historico_resultado} * {numero} = {self.resultado}")
                    self.historico.append({'operacao': 'multiplicação', 'resultado': self.resultado})
                elif escolher == 4:
                    numero = float(input("Digite o número para dividir com o histórico: "))
                    self.resultado /= numero
                    print(f"{historico_resultado} / {numero} = {self.resultado}")
                    self.historico.append({'operacao': 'divisão', 'resultado': self.resultado})
                elif escolher == 5:
                    print("Fechando calculdora...")
                    exit()
                input("Pressione [Enter] para continuar...")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Escolha um número válido.")

    def obter_numeros(self) -> list:
        lista_numeros = []
        while True:
            if len(lista_numeros) >= 2:
                calculo = int(input(
"""Deseja Calcular?
[1] Calcular
[2] Inserir mais um valor
"""))
                if calculo == 1:
                    break
                elif calculo == 2:
                    numero = float(input("Digite um número: "))
                    lista_numeros.append(numero)
            else:
                numero = float(input("Digite um número: "))
                lista_numeros.append(numero)
        return lista_numeros

def main():
    calculadora1 = Calculadora()

    print("*******MENU*******")
    while True:
        calculadora1.escolher_operacao()
        desc_operacao: str
        if calculadora1.operacao == 1:
            desc_operacao = "soma"
        elif calculadora1.operacao == 2:
            desc_operacao = "subtração"
        elif calculadora1.operacao == 3:
            desc_operacao = "multiplicação"
        elif calculadora1.operacao == 4:
            desc_operacao = "divisão"
        elif calculadora1.operacao == 5:
            continue
        else:
            break

        print(f"O resultado da {desc_operacao} é {calculadora1.resultado}")
        input("Pressione [Enter] para continuar...")

if __name__ == "__main__":
    main()