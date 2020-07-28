import sys
print("Enter the tuples(ctrl+d) to stop :- ")
tup_info = tuple(sys.stdin.readlines())
print(sorted(tup_info,key=lambda x:(x[0],x[1],x[2][:len(x[2])-1])))
