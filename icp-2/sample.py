print("Enter Elements of stack: ")
stack = [int(x) for x in input().split()]
con ="yes"
while con[0]=="y":
    ans = input("Enter 0 for push\n1 for pop\n2 to print stack\n3 for Top most element : ")
    while ans == "0":
        a = int(input("Enter the element to append"))
        stack.append(a)
        print(stack)
        con =input("Do you want to continue y or n")
        break
    while ans == "1":
        print("Stack element poped is:")
        print(stack.pop())
        con = input("Do you want to continue y or n")
        break
    while ans == "2":
        print("Stack elements are:")
        print(stack)
        con = input("Do you want to continue y or n")
        break
    while ans == "3":
        print("The stop of the stack is: ")
        print(stack[-1])
        con = input("Do you want to continue y or n")
        break