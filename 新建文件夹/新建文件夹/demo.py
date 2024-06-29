# class Demo:
#     def __init__(self, name, age, gender):
#
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#         print(self.name, self.age, self.gender)
# c=Demo( "John", 25, "Male" )

# def p(x):
#     if x > 0:
#
#         return True
#     else:
#
#         return False
#
# print(p(5))


a=[i for i in range(10)]
b, c, *d = a
print(b, c, d, sep=" ----------")
