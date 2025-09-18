import rpyc
import time

class SumService(rpyc.Service):
    def on_connect(self, conn):
        print("Nova conexão para o serviço de soma.")

    def on_disconnect(self, conn):
        print("Conexão de soma finalizada.")

    # [cite_start]Procedimento exposto para somar os elementos do vetor [cite: 66]
    def exposed_sum_vector(self, vector):
        # [cite_start]Medindo o tempo de execução no servidor [cite: 69]
        start_time = time.time()
        
        total = sum(vector) # Realiza a soma
        
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Servidor: Vetor de tamanho {len(vector)} somado em {execution_time:.6f} segundos.")
        
        # Retorna o resultado da soma e o tempo de execução do servidor
        return total, execution_time

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    print("Iniciando servidor de soma na porta 18861...")
    t = ThreadedServer(SumService, port=18861)
    t.start()