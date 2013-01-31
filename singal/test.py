import signal, os

def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.CTRL_C_EVENT, signal_handler)
signal.alarm(10)   # Ten seconds
try:
    while 1:
        import time
        time.sleep(1)
except Exception, msg:
    print "Timed out!"
