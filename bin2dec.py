a = [int(x) for x in input('Enter the binary number to convert (maintain space after every digit):').split()]
print(sum(c * (2 ** i) for i, c in enumerate(a[::-1])))
