class Node:
    def __init__(self,key,value):
        self.key = [key]
        self.value = [value]
        self.right = None
        self.left = None
        self.down = None
    
class Tree2_3:
    def __init__(self,key=None,value=None):
        self.root = Node(key,value)
    
    def __insert__(self,key,value=None):
        #Check key
        a = self.root
        for x in a.key:
            if x == key:
                raise KeyError('The key is already in the tree')
        #Remove Nones
        cont = 0
        flag = False
        for x in a.key:
            if x == None:
                a.key.pop(cont)
                a.value.pop(cont)
                flag = True
            cont += 1
        if flag == True:
            return self.__insert__(key,value)
        if len(a.key) == 1:
            if key > a.key[0]:
                a.key.append(key)
                a.value.append(value)
                a.right = Tree2_3()
                a.left = Tree2_3()
                a.down = Tree2_3()
            else:
                a.key.insert(0,key)
                a.value.insert(0,value)
                a.right = Tree2_3()
                a.left = Tree2_3()
                a.down = Tree2_3()
        elif len(a.key) == 2:
            if key < a.key[0]:
                return a.left.__insert__(key,value)
            if key > a.key[0] and key < a.key[1]:
                return a.down.__insert__(key,value)
            if key > a.key[1]:
                return a.right.__insert__(key,value)
        else:
            a.key.append(key)
            a.value.append(value)
            a.right = Tree2_3()
            a.left = Tree2_3()
            a.down = Tree2_3()
    
    def preOrder(self):
        l = []
        for i in self.root.key:
            if i is not None:
                l.append(i)
        return l


    def __str__(self):
        string = self.str()
        return string[:len(string)-1]

    def str(self):
        string = ''
        if self.root.left:
            l = self.root.left.str()
            string += l
        if self.root.down:
            l = self.root.down.str()
            string += l
        l = self.preOrder()
        for i in l:
            print(i)
            string += str(i) + ','
        if self.root.right:
            l = self.root.right.str()
            string += l
        return string
         

if __name__ == "__main__":
    a = Tree2_3(3,'zasdasdas')
    a.__insert__(4,'asdasdadssd')
    a.__insert__(5,'asdasdasd')
    a.__insert__(17,'asdasdasd')
    a.__insert__(24,'asdasdasd')
    a.__insert__(1,'asdasdasd')
    a.__insert__(2,'asdasdasd')
    a.__insert__(54,'asdasdasd')
    a.__insert__(37,'asdasdasd')
    a.__insert__(23,'asdasdasd')
    a.__insert__(87,'asdasdasd')
    print(a)
