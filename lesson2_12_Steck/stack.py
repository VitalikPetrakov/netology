class Stack:
    my_stack = []

    def __init__(self):
        pass

    def isEmpty(self):
        if len(self.my_stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        if self.my_stack:
            temp = self.my_stack[-1]
            self.my_stack.pop()
            return temp
        else:
            print('Stack is empty')

    def size(self):
        my_len = len(self.my_stack)
        return my_len

    def peek(self):
        my_len = len(self.my_stack)
        my_value = self.my_stack[my_len - 1]
        return my_value


def find_balance(value):
    my_stack = Stack()
    for item in value:
        if item in ['{', '[', '(']:
            my_stack.push(item)
        elif item == '}' and my_stack.size() > 0:
            if my_stack.peek() == '{':
                my_stack.pop()
            else:
                return False
        elif item == ']' and my_stack.size() > 0:
            if my_stack.peek() == '[':
                my_stack.pop()
            else:
                return False
        elif item == ')' and my_stack.size() > 0:
            if my_stack.peek() == '(':
                my_stack.pop()
            else:
                return False
        else:
            return False
    if my_stack.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    my_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]]']
    for item in my_list:
        if find_balance(item):
            print(item + ' - ' + "Сбалансированно")
        else:
            print(item + ' - ' + "Небалансированно")
