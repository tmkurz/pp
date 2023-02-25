#moje
a= 14000
b= a + a * 0.4
c= b - 1500
d= c + c * 0.12

print(a + b + c + d) #źle

#pokazane
print(14_000, 'zł')
print(14_000 * 1.4, 'zł')
print((14_000 * 1.4) - 1_500, 'zł')
print(((14_000 * 1.4) - 1_500) * 1.12, 'zł')