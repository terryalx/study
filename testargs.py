#!/usr/bin/python3

def list1(*args):
    for x in args:
        print(x)
        print(type(x))
    return args

list1(1, 2, 'lots')
print(type(list1))

def combine_args_and_kwargs(arg1, arg2, *args, kwarg1=None, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"Additional positional arguments (if any): {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"Additional keyword arguments (if any): {kwargs}")

list_at = [1, 2, (3, 4), {1 : 'key1'}, {2 : 'circle', 3 : 'flaw', 4 : 'paw'}]

combine_args_and_kwargs('q1', 'q2', list_at, list_at, {1 : 'key1'}, {2 : 'circle', 3 : 'flaw', 4 : 'paw'})


class assign:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def push(self, *arg):
        try:
            self.x = arg[0]
            self.y = arg[1]
            self.z = arg[2]
        except IndexError:
            print("Not Successful")
        return [x for x in arg]

ass = assign(1, 2, 3)
#print(ass.push(2, 3, 4))
print(ass.x, ass.y, ass.z)

class in_from(assign):
    def __init__(self, x, y, z, matrix):
        super().__init__(x, y, z)
        self.matrix = matrix

ifr = in_from(2, 4, 6, 8)
print(ifr.matrix, ifr.x)

