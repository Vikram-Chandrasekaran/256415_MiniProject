import stack_prog
print("___________________________")
print("Welcome to Data Structures")
print("___________________________")
while(true)
{
    print("Please select a data structure")
    print(" 1. Stack \n 2.Queue \n 3. Linked List \n 4. Exit")
    option = int(input())
    if(op==1)
    {
        s=Stack()
        while(True)
        {
            print(" 1. Push \n 2. Pop \n 3. Check size \n 4. Clear the stack 5. Exit\n")
            in_op = int(input())
            if(in_op==1):
                print("Enter the number to be pushed")
                s.push(int(input()))
            elif(in_op==2):
                s.pop()
            elif(in_op==3):
                s.size()
            elif(in_op==4):
                s.clear()
            elif(in_op==5):
                break
        }
    }
    if(op==2)
    {

    }
    if(op==3)
    {

    }
    if(op==4)
    {
        break;
    }
}
print("Thanks for using this application!")