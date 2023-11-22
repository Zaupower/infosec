'''
Read a name from console and compute a frequency table for each character. As example, for
the name “Marilyn Monroe”:
M a r i l y n space o e
2 1 2 1 1 1 2   1   2 1
'''

name_read = str(input())

frequency = {}
 
for i in name_read:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Char frequency :\n "
      + str(frequency))