def add_one(x):
    return x + 1
def double(x):
    return x * 2

def compose(add_one,double,x):
    v = add_one(double(x))
    return v
def pipe(*funcs):
    def vale(value):

    v = x
    for func in funcs:
        v = func(v)
    return v
print(compose(add_one,double,5))
process = pipe(a)
print(process(5))
print(pipe(add_one,double)(5))