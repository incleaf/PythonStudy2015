# sys
import sys

# sys args
print(sys.argv)

# sys exit
# sys.exit()

# sys path
sys.path.append('/Users/bek9/dev/study/python-study-2015/week03/bek9')
print(sys.path)

# pickle
import pickle

# pickle dump object
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# pickle load
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)

# os
import os

# os environ
print(os.environ['PATH'])

# os dir
print(os.getcwd())
os.chdir('/')
print(os.getcwd())

# os system
os.system('ls')

f = os.popen('ls -al')
print(f.read())

# os.mkdir('dirname')
# os.rmdir('dirname') # requires empty
# os.unlink('filename')
# os.rename('src', 'dst')

# shutil
# import shutil
# shutil.copy('src', 'dst')

# glob
import glob
print(glob.glob('/*'))

# tempfile
import tempfile
filename = tempfile.mktemp()
print(type(filename))

# time
import time
print(time.time()) # UTC 실수

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.ctime())

print(time.strftime('%c', time.localtime(time.time())))
for i in range(2):
    print(i)
    time.sleep(1)

# calendar
import calendar
calendar.prcal(2015) # print(calendar.calendar(2015))

calendar.prmonth(2015, 11)
print(calendar.weekday(2015, 11, 25)) # 2 weekday (mon=0, sun=6)

print(calendar.monthrange(2015, 11)) # (0, 30) weekday, day count

# random
import random
print(random.random())

print(random.randint(1,10)) # 1~10

print(random.choice(['a', 'b', 'c'])) 

d = [1,2,3]
random.shuffle(d)
print(d)

# threading
import threading

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(10):
    time.sleep(0.1)
    print(i)

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)

for msg in ['you', 'need', 'python']:
    t = MyThread(msg)
    t.start()

for i in range(10):
    time.sleep(0.1)
    print(i)

import webbrowser
webbrowser.open("http://wwww.google.com")
webbrowser.open_new("http://www.facebook.com")
