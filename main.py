class Stack:
    def __init__(self, st):
        self.st = st

    def isEmpty(self):
        if self.st:
            return True
        else:
            return False

    def push(self, new_elem):
        if isinstance(self.st, str):
            self.st += new_elem
        elif isinstance(self.st, list):
            self.st.append(new_elem)

    def pop(self):
        last_elem = self.st[-1]
        self.st = self.st[:-1]
        return last_elem

    def peek(self):
        last_elem = self.st[-1]
        return last_elem

    def size(self):
        return len(self.st)

    def __str__(self):
        return f'{self.st}'


def parity(s: Stack) -> bool:
    if s.size() % 2 == 0:
        return True
    return False


def balance(s: Stack) -> bool:
    skobki = {}
    for _ in range(s.size()):
        skobki[s.pop()] = skobki.get(s.peek(), 0) + 1
    if all([skobki.get('(', 0) == skobki.get(')', 0),
            skobki.get('[', 0) == skobki.get(']', 0),
            skobki.get('{', 0) == skobki.get('}', 0)]):
        return True
    return False


def main():
    enter = input('Введите скобочную последовательность: ')
    print()
    str_hooks = Stack(enter)
    if parity(str_hooks):
        result = balance(str_hooks)
    else:
        result = False
    if result:
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    main()
