import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[i+1] = temp

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ler a listagem do ls_out
def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

# Medir o tempo de execução (time)
def medir_tempo(func, arr):
    inicio = time.time()
    func(arr)
    fim = time.time()
    return fim - inicio

# App
if __name__ == "__main__":
    listagem = "ls_out.txt"
    arquivos = ler_arquivo(listagem)

    # Definir tamanhos dos arrays
    tamanhos = [200, 400, 600, 800, 1000]
    
    # Lista de algoritimos a ser executados
    algoritmos = [("Bubble Sort", bubble_sort), 
                  ("Selection Sort", selection_sort), 
                  ("Insertion Sort", insertion_sort)]

    # Armazenar resultados em dicionário em 3 listas por algoritimo
    resultados = {algoritmo: [] for algoritmo, _ in algoritmos}

    # Testar cada algoritmo para diferentes tamanhos
    for tamanho in tamanhos:
        sublista = arquivos[:tamanho]
        for algoritmo, func in algoritmos:
            lista = sublista[:]
            tempo = medir_tempo(func, lista)
            
            # Lista com tempos para criação do gráfico
            resultados[algoritmo].append(tempo)
            
            print(f"{algoritmo} - Tamanho {tamanho}: {tempo:.6f} segundos")
        print("")

    # Criar gráfico
    plt.figure(figsize=(10, 6))
    for algoritmo, tempos in resultados.items():
        plt.plot(tamanhos, tempos, marker='x', label=algoritmo)

    plt.title("Comparação de Algoritmos de Ordenação por Tamanho do Array")
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
