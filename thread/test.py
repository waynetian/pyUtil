import threading
import time

class X(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = 0

    def stop(self):
        self.flag = 1

    def run(self):
        '''
        while True:
            print 'sleep 1s'
            if self.flag == 1:
                break
            time.sleep(1)
        '''
        x = X1()
        x.start()

        time.sleep(10)

        print 'set stop'
        x.stop()

        while True:
            time.sleep(1)
            print 'num is', x.isAliveNum()

        time.sleep(5)




class X1:
    def __init__(self):
        self.flag = 0
        self.threadList = []
        for i in xrange(0, 3):
            workName = 'eventWoker-%s' %(i)
            my_thread=threading.Thread(target=self.run,\
                    name=workName)
            my_thread.setDaemon(True)
            self.threadList.append(my_thread)


    def stop(self):
        self.flag = 1


    def start(self):
        for worker in self.threadList:
            worker.start()

    def isAliveNum(self):
        i = 0
        for worker in self.threadList:
            if worker.isAlive() == True:
                i += 1
        return i

    def run(self):
        while True:
            import thread
            print 'sleep 1s %s' %( thread.get_ident() )
            if self.flag == 1:
                break
            time.sleep(1)









      
x = X()
x.start()


while True:
    time.sleep(10)




'''
while True:
    time.sleep(1)
    print 'num is', x.isAliveNum()

#x.stop()

#jtime.sleep(5)
#print x.isAlive()
time.sleep(5)

'''
'''
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
'''
