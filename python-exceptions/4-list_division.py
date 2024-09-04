#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range, dummy")
            result = 0
        except TypeError:
            print("wrong type, try again")
            result = 0
        except ZeroDivisionError:
            print("division by 0, is not the way")
            result = 0
        finally:
            result_list.append(result)
    return result_list
