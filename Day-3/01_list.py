# 1.1 List क्या है?
# List Python की सबसे flexible और commonly used data structure है। ये एक ordered, mutable (changeable) collection है जिसमें अलग-अलग types के items रख सकते हो।

# my_list = [10, 20, "hello", True, 3.14]

# ✅ Ordered: Items की position matter करती है (index से access करते हैं)


# ✅ Mutable: तुम items को बदल सकते हो
# ✅ Heterogeneous: किसी भी type के items रख सकते हो (int, str, bool, float)

# my_list=["sufill", 10, 20.43, True]

# print(my_list)


# items = [42, "apple", [1, 2], False, (3, 4)]

# print(type(items[0]))
# print(type(items[1]))
# print(type(items[2]))
# print(type(items[3]))
# print(type(items[4]))


# numbers = [10, 20, 30, 40, 50]

# print(numbers[0])      # First item
# print(numbers[-1])     # Last item
# print(numbers[1:4])    # Slice: 20 to 40


# fruits = ["apple", "banana", "cherry", "date", "fig"]
# # Find the third fruit using negative index
# # Slice first three fruits

# thred_fruits=fruits[-3]
# print(thred_fruits)

# print(fruits[0:3])