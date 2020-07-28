def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2>v1:
        return "NO"
    elif float.is_integer((x1-x2)/(v2-v1)):
        return "YES"

print(kangaroo(43,2,70,2))