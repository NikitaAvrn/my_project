import b

print("Hello, Git!")
print("Индексация это важно!\n")

ind = 0
sum = 0

while ind <= 9:
    sum += ind
    print(sum, end = ' ')
    ind += 1

print("\n")

a = int(input())
c = int(input())

print(b.sum_numbers(a, c))