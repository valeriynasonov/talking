class Stack():

    def __init__(self):
        self.stack = [ ]

    def isEmpty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, new_element):
        self.stack.insert(0, new_element)

    def pop(self):
        deleted_element = self.stack[0]
        self.stack.remove(self.stack[0])
        return deleted_element

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def index(self):
        return self.stack[0]

stack = Stack()

def control_balance(symbols):
    brackets = ["(", "[", "{", ")", "]", "}"]
    opening, closing = brackets[0:3], brackets[3:]
    for symbol in symbols:
        if symbol in opening:
            stack.push(symbol)
        elif symbol in closing:
            if opening.index(stack.index()) == closing.index(symbol):
                stack.pop()
            else:
                return False
    if stack.size() == 0:
        print("Brackets is Balance")
    else:
        print("Brackets is not balance")

brackets = "{", "{", "[", "(", ")", "]", "}", "}"
control_balance(brackets)

