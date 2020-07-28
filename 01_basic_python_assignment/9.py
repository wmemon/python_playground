sum = 0
while True:
    num = input("Please enter number(N to stop) :- ")
    if num == 'N':
        break
    num = int(num)
    if not num>100:
        sum += num
print(f"The sum is:- {sum})
