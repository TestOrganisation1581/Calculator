class Calculator:
    el1=0
    el2=0
    operation=""
    ans=0
    def SetParams(self):
        print("Введите первый элемент")
        self.el1=int(input())
        print("Введите операцию(+; -;)")
        self.operation=input()
        print("Введите второй элемент")
        self.el2=int(input())
    def Work(self):
        if(self.operation=="+"):
            ans=self.el1+self.el2
        else:
            ans=self.el1-self.el2
        return ans
C=Calculator()
C.SetParams()
print(C.Work())

        