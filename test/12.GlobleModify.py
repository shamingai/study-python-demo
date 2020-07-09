a = 1
b = [2, 3]
c = 4

def func():
    a = 5
    print ("in func a:", a)
    b[0] = 6
    b[1] = 7
    print ("in func b:", b)
    global c
    c = 8
    print ("in func c:", c, "\n")

if __name__ == '__main__':
    print ("before func a:", a)
    print ("before func b:", b)
    print ("before func c:", c, "\n")
    func()
    print ("after func a:", a)
    print ("after func b:", b)
    print ("after func c:", c)