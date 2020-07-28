num_list = [35,34,33,31,32,9,86,5]

def check_odd(num):
    if num%2!=0:
        return num

#filter is a function from functional programming.
print(list(filter(check_odd,num_list)))

sum =0
for num in num_list:
    if num%2==0:
        sum += num
print(f"The sum of even numbers is:- {sum}")