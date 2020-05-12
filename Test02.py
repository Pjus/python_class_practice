import filename

# Jane, Jane + fff
a = filename.classname()
print(a.func1()) 
print(a.func2())

# Holy
b = filename.classname('Holy')
print(b.func1())

# None
print(filename.classname.__init__(a,'Holy'))
