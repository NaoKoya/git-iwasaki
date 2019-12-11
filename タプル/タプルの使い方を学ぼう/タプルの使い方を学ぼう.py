def basic():
    test_tuple = (1,'A',True)
    print(test_tuple)
    print(test_tuple[0])
    print(test_tuple[1])
    print(test_tuple[2])
def error():
    test_tuple = (1,2)
    test_tuple[0] = 100

if __name__ == "__main__":

    basic()
    error()