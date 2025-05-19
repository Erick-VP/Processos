import sys
import time

class Processo:
    def __init__(self, nome, ordem_chegada, tamanho):
        self.nome = nome
        self.ordem_chegada = ordem_chegada
        self.tamanho = tamanho
        self.tempo_espera = 0 
        self.turnaround = 0

    def __str__(self):
        return (f"{self.nome:<15} Ordem={self.ordem_chegada:<3} "
                f"Tamanho={self.tamanho:<3} Espera={self.tempo_espera:<3} "
                f"Turnaround={self.turnaround}")

def loading_animation(nome, duracao):
    simbolos = ['|', '/', '-', '\\']
    for i in range(duracao * 4):  # 4 frames por segundo
        sys.stdout.write(f"\rExecutando {nome} {simbolos[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.25)
    print(f"\r{nome} finalizado!{' ' * 10}")

class Calculadora:
    def __init__(self):
        self.processos = []
        self.media_espera = 0
        self.media_turnaround = 0

    def create(self):
        quantidade = int(input("Digite a quantidade de processos: "))
        for i in range(quantidade):
            nome = input(f"Digite o nome do processo {i + 1}: ")
            ordem = int(input(f"Digite a ordem do processo {nome}: "))
            tamanho = int(input(f"Digite o tempo de execução de {nome}: "))
            self.processos.append(Processo(nome, ordem, tamanho))

    def calcular_tempos(self):
        tempo_atual = 0
        for p in self.processos:
            p.tempo_espera = tempo_atual
            p.turnaround = p.tempo_espera + p.tamanho
            tempo_atual += p.tamanho
        total_espera = sum(p.tempo_espera for p in self.processos)
        total_turnaround = sum(p.turnaround for p in self.processos)
        self.media_espera = total_espera / len(self.processos)
        self.media_turnaround = total_turnaround / len(self.processos)

    def calcular_fifo(self):
        self.processos.sort(key=lambda p: p.ordem_chegada)
        self.calcular_tempos()

    def calcular_sjf(self):
        self.processos.sort(key=lambda p: p.tamanho)
        self.calcular_tempos()
    def exibir_resultado(self, titulo):
        print(f"\n{titulo}\n")
        print(f"{'Processo':<15}{'Espera':<15}{'Turnaround'}\n")

        for p in self.processos:
            print(f"{p.nome:<15}{p.tempo_espera:<15}{p.turnaround}")
            loading_animation(p.nome, p.tamanho)
        print(f"\nTempo médio de espera: {self.media_espera:.2f}")
        print(f"Tempo médio de turnaround: {self.media_turnaround:.2f}")








c = Calculadora()
c.create()

modo = input("Escolha o modo de execução (fifo / sjf): ").lower()

if modo == "fifo":
    c.calcular_fifo()
    c.exibir_resultado("🔁 Resultados - FIFO")
elif modo == "sjf":
    c.calcular_sjf()
    c.exibir_resultado("⚙️ Resultados - SJF")
else:
    print("Modo inválido.") 
    
    
    
    
    
    # def exibir_resultado(self, titulo):
    #     print(f"\n{titulo}\n")
    #     print(f"{'Processo':<15}{'Espera':<15}{'Turnaround'}")
    #     for p in self.processos:
    #         print(f"{p.nome:<15}{p.tempo_espera:<15}{p.turnaround}")
    #         # Simula execução
    #         for i in range(p.tamanho):
    #             print(f"  Executando {p.nome}... tempo restante: {p.tamanho - i}s")
    #             time.sleep(1)
    #     print(f"\nTempo médio de espera: {self.media_espera}")
    #     print(f"Tempo médio de turnaround: {self.media_turnaround}")