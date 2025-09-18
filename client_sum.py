import rpyc
import sys
import time

# Verifica se o endereço do servidor foi passado
if len(sys.argv) < 2:
    exit("Uso: {} SERVIDOR".format(sys.argv[0]))

server = sys.argv[1]

# [cite_start]Pede ao usuário o tamanho do vetor [cite: 64]
try:
    n = int(input("Digite o tamanho do vetor (n): "))
except ValueError:
    exit("Por favor, digite um número inteiro.")

# Conecta ao servidor
try:
    conn = rpyc.connect(server, 18861)
    print(f"Conectado a {server}.")

    # [cite_start]Cria o vetor com elementos de 0 a n-1 [cite: 64]
    my_vector = list(range(n))
    print(f"Vetor de tamanho {n} criado.")
    
    # [cite_start]Mede o tempo de execução da chamada remota no cliente [cite: 69]
    start_time_client = time.time()

    # Chama o procedimento remoto que soma o vetor
    result, server_time = conn.root.sum_vector(my_vector)
    
    end_time_client = time.time()
    
    client_round_trip_time = end_time_client - start_time_client

    # [cite_start]Imprime os resultados [cite: 67]
    print("\n--- Resultados ---")
    print(f"Soma recebida do servidor: {result}")
    print(f"Tempo de execução no SERVIDOR: {server_time:.6f} segundos")
    print(f"Tempo total da chamada (ida e volta) no CLIENTE: {client_round_trip_time:.6f} segundos")
    
    conn.close()

except Exception as e:
    print(f"Ocorreu um erro: {e}")