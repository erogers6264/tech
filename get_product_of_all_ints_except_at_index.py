import random


int_list = [1, 7, 3, 4]

def get_products_of_all_ints_except_at_index(int_list):
    products = [None] * len(int_list)
    products_of_all_ints_before_index = [None] * len(int_list)
    products_of_all_ints_after_index = [None] * len(int_list)

    # for each integer, find the product of all the integers
    #before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_before_index[i] = product_so_far
        product_so_far *= int_list[i]


    product_so_far = 1
    counter = len(int_list) - 1
    while(counter >= 0):
        products_of_all_ints_after_index[i] = product_so_far
        product_so_far *=
    for i in range(len(int_list)):
        products_of_all_ints_after_index[-i] = product_so_far
        product_so_far *= int_list[-i]

    print products_of_all_ints_before_index
    print products_of_all_ints_after_index





    return products
    # for outer_index in range(len(int_list)):
    #     product = 1
        # for inner_index, inner_integer in enumerate(int_list):
    #         if inner_index == outer_index:
    #             continue
    #         product *= inner_integer
    #     products.append(product)
    # return products

print get_products_of_all_ints_except_at_index(int_list)

