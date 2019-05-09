from stack.Stack import Stack


def check_bal_par(par_str):
    if not len(par_str):
        return True
    if len(par_str) % 2 != 0:
        return False

    s = Stack()
    for item in par_str:
        if s.is_empty():
            s.push(item)
        else:
            if s.peek() == '(' and item == ')':
                s.pop()
            else:
                s.push(item)
    return s.is_empty()


def check_bal_par_2(par_str):
    if not len(par_str):
        return True
    if len(par_str) % 2 != 0:
        return False

    s = Stack()
    for item in par_str:
        if s.is_empty():
            s.push(item)
        else:
            if s.peek() == '(' and item == ')' or \
                s.peek() == '[' and item == ']' or \
                    s.peek() == '{' and item == '}':
                s.pop()
            else:
                s.push(item)
    return s.is_empty()


ex = '(()(()()))'
ex2 = ''
ex3 = ')()()('
print(check_bal_par(ex))
print(check_bal_par(ex2))
print(check_bal_par(ex3))

ex4 = '{{([][])}()}'
ex5 = '((()]))'
print(check_bal_par_2(ex4))
print(check_bal_par_2(ex2))
print(check_bal_par_2(ex5))
