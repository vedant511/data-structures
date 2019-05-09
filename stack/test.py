from stack.Stack import Stack

s = Stack()

print(s.get_size())
print(s.is_empty())
print(s.peek())
s.print_stack()
s.push(5)
s.push(2)
s.push(28)
s.push(11)
s.push(18)
print(s.get_size())
print(s.is_empty())
print(s.peek())
s.print_stack()

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.print_stack()
