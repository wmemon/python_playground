"""Please write a program which accepts basic mathematic expression from
console and print the evaluation result. Using eval()  """

def exp_eval(expression):
    if not isinstance(expression,str):
        return f"[!] The expression must be in string format."

    try:
        result = eval(expression)
    except:
        return f"[!] There was some error with the evaluation. (Check your expression)  "

    return result


print(exp_eval('3*11+2-33'))
print(exp_eval('(3*2+3))'))