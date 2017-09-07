def cleaner(func):
    def inner(data):
        print "cleaning data"
        func(data.strip())
    return inner

@cleaner
def set_data(data):
    return data

print set_data(raw_input("enter:"))
