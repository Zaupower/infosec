'''
Read a number from console. The number will be the length of the Fibonacci sequence to
generate. Fibonacci is a sequence of numbers where the next number in the sequence is the sum
of the previous two numbers in the sequence
'''
length = int(input('Fib size\n'))
t1 = 0
t2 = 1
next_term = t1 + t2
for i in range(length):
    print(next_term)
    t1 = t2
    t2 = next_term
    next_term = t1 + t2