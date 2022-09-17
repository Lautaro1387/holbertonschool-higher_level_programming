#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        if my_list_1 / my_list_2 == 0
            return d
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        d = my_list_1 / my_list_2
        print("{}".format(d))
        return d
