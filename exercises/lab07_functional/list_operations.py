"""
Lab 07 – Functional Programming
Program B: Add two lists [1,2,3,4,5,6] and [4,6,12,3,2,1] using map/lambda,
then multiply the result with [4,2,8,3,2,1].
"""


def add_and_multiply(list1, list2, list3):
    summed  = list(map(lambda x, y: x + y, list1, list2))
    product = list(map(lambda x, y: x * y, summed, list3))
    return summed, product


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 6, 12, 3, 2, 1]
    list3 = [4, 2, 8, 3, 2, 1]

    summed, product = add_and_multiply(list1, list2, list3)
    print(f"List 1:  {list1}")
    print(f"List 2:  {list2}")
    print(f"Sum:     {summed}")
    print(f"List 3:  {list3}")
    print(f"Product: {product}")
