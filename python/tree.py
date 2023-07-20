class Treenode:
    def __init__(self, data):
        self.data = data
        self.children=[]
        self.parent=None

    def addchild (self, child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent
        return level
    


    def printtree(self):
        level = self.getlevel()
        print((level*" ")+"|---"+self.data)
        if self.children:
            for child in self.children:
                child.printtree()
    

def makingtree():
    root = Treenode("Electronic")
    laptop = Treenode("laptop")
    tv = Treenode("TV")
    radio = Treenode("Radio")

    laptop.addchild(Treenode("acer"))
    laptop.addchild(Treenode("predator"))
    laptop.addchild(Treenode("Dell"))

    tv.addchild(Treenode("Samsung"))
    tv.addchild(Treenode("sharp"))
    tv.addchild(Treenode("sony"))


    radio.addchild(Treenode("AIR"))
    radio.addchild(Treenode("mirchi"))

    root.addchild(laptop)
    root.addchild(tv)
    root.addchild(radio)

    return root


if __name__ == '__main__':
    x=makingtree()
    x.printtree()
