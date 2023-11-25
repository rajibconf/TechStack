"""python > stack.py
Data structure and algorithem
"""

class Stack():
    """
    @desctiption: This class defines several methods for stack.
    """

    def __init__(self):
        self.mystack = []

    def size(self):
        # returns the size of the stack
        return len(self.mystack)

    def is_empty(self):
        # checks whether the stack is empty or not
        if self.size() > 0:
            return False
        else:
            return True

    def push(self, item):
        # push an item to the defined stack
        return self.mystack.append(item)

    def pop(self):
        # pop an item from defined stack
        if self.is_empty():
            print("Sorry, the stack is empty.")
        else:
            return self.mystack.pop()
    
    def peek(self):
        # peeks an item from the stack means won't remove it
        if self.is_empty():
            print("Sorry, the stack is empty.")
        else:
            return self.mystack[len(self.mystack) - 1]


def main():
    # defining the main function for the stack
    s = Stack() # s is an object of Stack class
    while True:
        print(
            f"""
            1. Push
            2. Pop
            3. Peek
            4. Show
            5. Quit
            """
            )
        case = int(input("What do you wanna do now? "))
        # stating smething, equivelent to Switch statement in C/C++
        if case == 1:
            item = input("Input item, you wanna push to Stack: ")
            s.push(item)
            print(f"Congrats! {item}, has been pushed.")
        elif case == 2:
            print(f"Pop the item: {s.pop()}")
        elif case == 3:
            print(f"{s.peek()}, has been peeked.")
        elif case == 4:
            print(f"The current condition of our stack: {s.mystack}")
        elif case == 5:
            print(f"The script is gonna quit.")
            quit()
        else:
            print("Oops! Wrong choice.")
            main()


if __name__ == "__main__":
    main()

                