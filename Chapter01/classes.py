class namakelas:
    common = 10
    def __init__ (self): #memanggil constructor
        self.myvariable = 3
    def myfunction (self, arg1, arg2):  #instance method
        return self.myvariable

instance = namakelas()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2)) #memanggil instance method

instance2 = namakelas()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)

namakelas.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)

instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
namakelas.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)

class AnotherClass (namakelas):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2)) #memanggil instance method

instance.test = 10
print("instance.test " , instance.test) #memanggil instance method






