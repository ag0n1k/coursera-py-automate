import os

pid = os.fork()

if pid:
    print(pid, os.getpid())
else:
    print(os.getpid())
