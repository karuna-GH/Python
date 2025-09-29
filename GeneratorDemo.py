class generator_demo:
    def my_generator(self,number):
        for i in number:
            yield i

genobj = generator_demo()
numbers = [10,2,3,3,6,5,6,9]
ob= genobj.my_generator(numbers)

for value in ob:
    print(value)