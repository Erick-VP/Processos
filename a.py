class Processo:
    def __init__(self, name, ordem_chegada, tamanho):
        self.nome = name
        self.ordem_chegada = ordem_chegada
        self.tamanho = tamanho
        self.tempo_espera = 0 
        self.turnaround = 0

proc = 3
processos = []

for i in range(proc):
    nome = input(f"Digite o nome do processo {i + 1}: ")
    ordem= int(input(f"Digite a ordem do processo {nome}: "))
    tamanho = int(input(f"Digite o tempo de execução de {nome}: "))
    processos.append(Processo(nome, ordem, tamanho))

processos.sort(key=lambda p: p.ordem_chegada)

tempo_atual = 0
for p in processos:
    p.tempo_espera = tempo_atual
    p.turnaround = p.tempo_espera + p.turnaround
    tempo_atual += p.tamanho

print("\nResultados FIFO: \n")

print(f"{'Processo':<15}{'Espera':<15}{'Turnaround'}")

for p in processos:
    print(f"{p.nome:<15}{p.tempo_espera:<15}{p.turnaround}")

media_espera = sum(p.tempo_espera for p in processos) / len(processos)

media_turnaround = sum(p.turnaround for p in processos) / len(processos)

print(f"\nTempo médio de espera: {media_espera}")
print(f"Tempo médio de turnaround: {media_turnaround}")