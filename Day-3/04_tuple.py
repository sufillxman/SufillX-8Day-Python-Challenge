#  2.1 Tuple क्या है?

# Tuple भी list की तरह ordered collection है, लेकिन ये immutable होती है — मतलब एक बार बना दी तो change नहीं कर सकते।

# my_tuple = (10, 20, 30)

# Tuples are for fixed data – like days of the week, coordinates, settings, etc.

# | Feature     | Tuple            |    List          |

# | ----------- | ---------------- | ---------------  |
# | Ordered     | ✅                | ✅             |

# | Changeable  | ❌ Immutable      | ✅ Mutable     |

# | Syntax      | `( )`            | `[ ]`            |

# | Performance | Faster than list | Slightly slower  |


# 2.3 Use Case: कब Tuple use करें?
# Data fixed है, change नहीं करना

# Memory-efficient code चाहिए

# Dictionary के keys में complex values डालनी हो

# days = ("Mon", "Tue", "Wed")

# coordinates = (19.07, 72.87)  # latitude, longitude

# 2.4 Tuple Packing & Unpacking

# data = (1, "Sufill", 85.5)  # packing

# # Unpacking
# id, name, marks = data 
# print(name)  # "Sufill"

# 2.5 Trick – Swapping Without Temp Variable

# a, b = 10, 20
# a, b = b, a


# Mini Quiz:

t = (1, 2, [3, 4])
t[2][0] = 99
print(t)  # Output?
# ✅ Tuples are immutable, but अगर अंदर list है, तो वो mutable होती है
