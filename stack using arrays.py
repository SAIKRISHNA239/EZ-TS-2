stack =[]
def push():
    element=int(input("enter the elements"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
while True:
    print("select operation 1.push 2.pop 3.display 4.quit")
    choice=int(input("enter yr choice"))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter the correct operation")