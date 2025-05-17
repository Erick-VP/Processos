class Processo:
    def __init__(self, nome, ordem_chegada, tamanho):
        self.nome = nome
        self.ordem_chegada = ordem_chegada
        self.tamanho = tamanho
        self.tempo_espera = 0 
        self.turnaround = 0

    def __str__(self):
        return (f"{self.nome:<15} Ordem={self.ordem_chegada:<3} " f"Tamanho={self.tamanho:<3} Espera={self.tempo_espera:<3} " f"Turnaround={self.turnaround}")

class Calculadora:
    def __init__(self):
        self.processos = []
        self.media_espera = 0
        self.media_turnaround = 0

    def create(self):
        quantidade = int(input("Digite a quantidade de processos: "))
        for i in range(quantidade):
            nome = input(f"Digite o nome do processo {i + 1}: ")
            ordem= int(input(f"Digite a ordem do processo {nome}: "))
            tamanho = int(input(f"Digite o tempo de execução de {nome}: "))
            self.processos.append(Processo(nome, ordem, tamanho))

    def calcular_tempos(self):
        tempo_atual = 0
        for p in self.processos:
            p.tempo_espera = tempo_atual
            p.turnaround = p.tempo_espera + p.turnaround
            tempo_atual += p.tamanho
        total_espera = sum(p.tempo_espera for p in self.processos) / len(self.processos)
        total_turnaround = sum(p.turnaround for p in self.processos) /len(self.processos)
        self.media_espera = total_espera 
        self.media_turnaround = total_turnaround 

    def calcular_fifo(self):
        self.processos.sort(key=lambda p: p.ordem_chegada) # organiza 
        self.calcular_tempos()

    def calcular_sjf(self):
        self.processos.sort(key=lambda p: p.tamanho)
        self.calcular_tempos 


    def exibir_resultado(self):  # Fazer modificações no exibir resultados como se estivesse executando processo por processo
        print("\nResultados: \n")
        print(f"{'Processo':<15}{'Espera':<15}{'Turnaround'}")
        for p in self.processos:
            print(f"{p.nome:<15}{p.tempo_espera:<15}{p.turnaround}")
        print(f"\nTempo médio de espera: {self.media_espera}")
        print(f"Tempo médio de turnaround: {self.media_turnaround}")








c = Calculadora()
c.create()
c.calcular_()  # colocar _fifo ou _sjf
c.exibir_resultado() # Fazer modificações no exibir resultados como se estivesse executando processo por processo