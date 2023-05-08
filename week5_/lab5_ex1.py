def create_list():
    my_list = ['PlayStation','Xbox','Steam','iOS','Google Play']
    return my_list

def get_info(my_list):
    my_list = create_list()
    my_tuple = (my_list[0], my_list[-2],len(my_list))
    return my_tuple

def get_partial(my_list):
    my_list = create_list()
    my_tuple1 = [my_list[1], my_list[2], my_list[3]]
    return my_tuple1

def get_last_three(my_list):
    # list1 = create_list()
    # list1 = list1[4:1:-1]
    return my_list[4:1:-1]

def double_list(my_list):
    my_list = my_list + my_list
    return my_list

def amend(my_list):
    my_list[1] = "None"
    my_list[-1] = my_list[-1]
    my_list.append("Bye")
    return my_list

if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))