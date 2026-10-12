class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = StackNode(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return None

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = QueueNode(value)

        if self.rear is None:
            self.front = node
            self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value


def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    return 0


def infix_to_postfix(expression):
    operators = LinkedStack()
    output = ""
    index = 0

    for character in expression:
        if character == " ":
            index = index + 1
            continue

        if ("a" <= character <= "z") or ("A" <= character <= "Z") or ("0" <= character <= "9"):
            output = output + character
        elif character == "(":
            operators.push(character)
        elif character == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output = output + operators.pop()

            if not operators.is_empty():
                operators.pop()
        else:
            while (
                not operators.is_empty()
                and operators.peek() != "("
                and precedence(operators.peek()) >= precedence(character)
            ):
                output = output + operators.pop()

            operators.push(character)

        index = index + 1

    while not operators.is_empty():
        output = output + operators.pop()

    return output


print("Stack")
stack = LinkedStack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Pop:", stack.pop())
print("Top:", stack.peek())

print("Infix to postfix")
expression = "A + B * (C - D)"
print("Infix:", expression)
print("Postfix:", infix_to_postfix(expression))

print("Queue simulation")
customers = LinkedQueue()
customers.enqueue("Customer 1")
customers.enqueue("Customer 2")
customers.enqueue("Customer 3")

print("Serving:", customers.dequeue())
print("Serving:", customers.dequeue())

customers.enqueue("Customer 4")
print("Serving:", customers.dequeue())
print("Serving:", customers.dequeue())

# Performance comparison:
# Linked-stack push, pop, and peek take O(1) time.
# Linked-queue enqueue and dequeue take O(1) time.
# Infix-to-postfix conversion takes O(n) time and O(n) extra space,
# where n is the number of characters in the expression.
# Linked structures use extra memory for node references, but do not
# require shifting elements when adding or removing items.

