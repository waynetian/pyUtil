import threading

class X(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.flag = 1 
    self.cond = threading.Condition()

  def run(self):
    print '&&2'
    
    print '&&1'
   
    while self.flag == 1:
      self.cond.acquire()
      self.cond.wait(3.0)
      import time
      while True:
        time.sleep(1)
        print '*'
      #self.cond.release()
      #self.cond.acquire()
      #self.condition.wait(300)



      
x = X()
x.start()

import time
time.sleep(10)


x.flag = 0
x.cond.acquire()
x.cond.wait(3)
#x.cond.acquire()
#x.cond.notify()
#x.cond.release()
while True:
        time.sleep(1)
        print 'sleep'
