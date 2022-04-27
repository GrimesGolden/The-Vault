
sum = 0
start = int(input("Input starting value a: "))
stop = int(input("Input final value b: "))
n = int(input("Input rectangle number n: "))
delta = (stop - start)/n

def f(x):
    result = (x**2) + 1
    return result

i = start + delta
while i <= stop:
    product = (float(f(i)) * float(delta))
    sum += product
    i += delta

print("Right endpoint estimate is : ")
print(sum)
sum = 0

i = start
while i <= (stop - delta):
    product = (float(f(i)) * float(delta))
    sum += product
    i += delta

print("Left endpoint estimate is : ")
print(sum)

sum = 0
i = start + (delta * 1/2)
while i <= (stop - (delta * 1/2)):
    product = (float(f(i)) * float(delta))
    sum += product
    i += delta

print("Midpoint endpoint estimate is : ")
print(sum)
print("end")













