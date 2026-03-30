# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    root1= (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    root2= (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    if root1!=root2:
        ro1=str(root1)
        ro2=str(root2)
        if "j" not in ro1 and "j" not in ro2:
            return f"({root1}, {root2})"
        else:
            return f"( )"
    else:
        return f"({root1})"


def value_y(a, b, c, x):
    y= a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a==0:
        if b!=0:
            return f"f(x) = {b} * X + {c}"
        else:
            return f"f(x) = {c}"
    elif b==0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    new_a=2*a
    if new_a==0:
        return f"f'(x) = {b}"
    elif b==0:
        return f"f'(x) = {new_a} * X"
    else:
        return f"f'(x) = {new_a} * X + {b}"

