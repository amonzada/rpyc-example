import rpyc
import time 
start = time.time()

class MyService(rpyc.Service):
  def on_connect(self, conn):
    pass

  def on_disconnect(self, conn):
    pass

  def exposed_get_answer(self): 
    return 42

  exposed_the_real_answer_though = 43 
  
  def get_question(self): # este método não é exposto
    return "Qual é a cor do cavalo branco de Napoleão?"
  
if __name__ == "__main__":
  from rpyc.utils.server import ThreadedServer

  t = ThreadedServer(MyService, port=18861)
  t.start()

  end = time.time()
  print(end-start)
