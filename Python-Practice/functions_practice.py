def hello():
    print("Hello")


hello()


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


print(pack("pants", "socks", "shirts"))


def eat_lunch(lst):
    if len(lst) == 0:
        print("My lunchbox is empty!")
    elif len(lst) == 1:
        print("I only eat", lst[0])
    else:
        print("First I eat", lst[0])
        for i in range(1, len(lst)):
            print("Then I eat", lst[i])


eat_lunch(["pizza", "waffles"])
