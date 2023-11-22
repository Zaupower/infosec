'''
Ask the user to provide an array of numbers (integers or floats, positive or negative) with
variable length. For the given array compute:
a. Mean
b. Median
c. Max, Minimum
d. Variance
e. Standard Deviation
f. Number of positive and negative numbers
'''
import math
numbers = []
numbers_to_input = int(input('Quantity of numbers to read?\n'))

for i in range(numbers_to_input):
    n = float(input(f'Add number {i+1}:\n'))
    numbers.append(n)
numbers_len = len(numbers)
mean = sum(numbers)/numbers_len
print(f'Mean: {mean}')
numbers.sort()
if numbers_len %2 == 0:
    n1 =numbers[int(numbers_len/2)] 
    n2 = numbers[int(numbers_len/2)-1]
    median = (n1+n2/2)
else:
    median = numbers[int(numbers_len/2)]
print(f'Median: {median}')

print(f'Max: {numbers[numbers_len-1]}, Minimum: {numbers[0]}')

num_less_mean = 0.0
for number in numbers:
    num_less_mean += (pow((mean - number), 2))
varience = num_less_mean / (numbers_len -1)
print(f'Variance: {varience}')


print(f'Standard Deviation: {math.sqrt(varience)}')
negatives= 0
for num in numbers:
    if num < 0:
        negatives+=1
print(f'Number of positives: {numbers_len - negatives} and negative numbers: {negatives}')

