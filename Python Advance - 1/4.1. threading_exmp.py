import threading
import time


class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter, delay):
      super(MyThread,self).__init__()
      # threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.delay = delay

   def run(self):
      print("Starting " + self.name)
      print_time(self.name, self.counter, self.delay,self.threadID)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay,threadID):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time()),threadID))
      counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1", 3, 3)
thread2 = MyThread(2, "Thread-2", 4, 2)
thread3 = MyThread(3, "Thread-3", 5, 5)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

print("Exiting Main Thread")