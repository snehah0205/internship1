
    class Demo:
        def add(self,*args):
            total=0
            for i in args:
                total=total+1
            return total

    d=Demo()
    print(d.add(2,3))
    print(d.add(18,20,30))