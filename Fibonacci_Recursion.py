def fibonacci_recursive(n):
    """ Fibonacci Series using recursion """
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))


     
     
print(fibonacci_recursive(str(sys.argv[1])))

if __name__ == "__main__" :
     import sys
     fibonacci_recursive(int(sys.argv[1]))