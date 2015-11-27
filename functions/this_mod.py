__author__ = 'evgen'

var = 99

def local():
    var = 0

def glob_one():
    global var
    var += 1

def glob_two():
    var = 0
    import sys
    glob = sys.modules['this_mod']
    glob.var += 1

def test():
    print(var)
    local()
    glob_one()
    glob_two()
    print(var)


