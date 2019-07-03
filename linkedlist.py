#a python code showing the working of linked list
class node():
    def __init__(self,data=0,nextnode=0):
        self.data=data
        self.nextnode=nextnode

class list:
    def __init__(self):
        self.top=node()
    def pushnode(self,data):
        newnode=node(data,self.top)
        self.top=newnode
    def popnode(self):
        n=self.top.nextnode
        self.top=n
    def showstack(self):
        temp=self.top
        while temp.nextnode!=0:
            print(temp.data)
            temp=temp.nextnode


stack=list()
while 1:
    choice=int(input("press 1 to push and 0 to pop and 2 to show stack"))
    if choice==1:
        stack.pushnode(input("enter the value to be pushed\t"))
    elif choice==0:
        stack.popnode()
    elif choice==2:
        stack.showstack()
    else:
        break





