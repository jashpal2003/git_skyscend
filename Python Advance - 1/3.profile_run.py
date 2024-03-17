import cProfile

# cProfile.run('print("Hello")')

# f1 = open('1.decorator.py', 'r')
# f_str = f1.read()
# cProfile.run(f_str)

# 4 Function Calls n Time taken to execute
#
# ncalls = number of calls
# tottime = the total time taken for the function
# percall = quotient  = tottime / ncalls
# cumtime = total time including all subfunctions
# percall = quotient  = cumtime / all calls
# file_name:lineno(function)


import pstats
from datetime import datetime
import time
# # # # #
pr = cProfile.Profile()
# # # # # #
pr.enable()
# # # # #
cr_dt = datetime.now()
print(cr_dt)
#
x = 10
y = 20
z = x - y
time.sleep(3)
print(z)
z = abs(z)
print(z)

def print_hello():
    time.sleep(3)
    print("Hello")

print_hello()

time.sleep(5)
z = pow(z, 2)
print(z)


print("Hello, The Profiling has ended")
pr.disable()
# # # #
# # # # # cProfile.run('print("Hello, The Profiling has ended")')
# # # # # #
ps = pstats.Stats(pr)
ps.print_stats()
