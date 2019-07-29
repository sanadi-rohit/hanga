#python code for the working of a tree
#gives sorted aray as output
class node:
    def __init__(self,data=None,leftnode=None,rightnode=None):
        self.data=data
        self.leftnode=leftnode
        self.rightnode=rightnode
    def addnode(self,data):
        if data<=self.data:
            if self.leftnode==None:
                self.leftnode=node(data)
            else:
                self.leftnode.addnode(data)
        else:
            if self.rightnode==None:
                self.rightnode=node(data)
            else:
                self.rightnode.addnode(data)
    def showtree(self):
        if self.leftnode!=None:
            self.leftnode.showtree()
        print("->",self.data,end="")
        if self.rightnode!=None:
            self.rightnode.showtree()

root=node(int(input("enter root node value\t")))
while 1:
    choice=int(input("1 for adding node and 0 to show tree"))
    if choice==1:
        root.addnode(int(input()))
    elif choice==0:
        print("showing the tree in inorder fashion")
        root.showtree()
        print()
    else:
        break
