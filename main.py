class Stack:
    def __init__(self, st=[]):
        self.st = st

    def isEmpty(self):
        if self.st:
            return False
        else:
            return True

    def push(self, new_elem):
        self.st.append(new_elem)

    def pop(self):
        return self.st.pop()

    def peek(self):
        return self.st[-1]

    def size(self):
        return len(self.st)

    def __str__(self):
        return f'{self.st}'


def balance(hooks: str) -> Stack:
    dict_hooks = {'(': ')', '{': '}', '[': ']'}
    s = Stack()
    for h in hooks:
        if h in dict_hooks.keys():
            s.push(h)
        elif not s.isEmpty() and dict_hooks.get(s.peek(), '') == h:
            s.pop()
        else:
            s.push(h)
            break
    return s


def main():
    enter = input('Введите скобочную последовательность: ')
    print()
    result = balance(enter)
    if result.isEmpty():
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    main()

