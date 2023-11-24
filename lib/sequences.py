#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []  
    
    if length <= 0:
        print([])
    elif length == 1:
        fib = [0]
        print(fib)
    elif length == 2:
        fib = [0, 1]
        print(fib)
    else:
        fib = [0, 1]
        for _ in range(2, length):
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        print(fib)




    
    

 



