# Type Casting (Type Conversion)

x = "5"
y = int(x)  # "5" string ko integer banaya
print(y + 2)  # Output: 7


# ------------------------------------------
# Type casting ka matlab hai ek data type ko dusre data type me badalna.
# Python me mainly do tarah ki type casting hoti hai:
# 1. Implicit Type Casting (Automatic)
# 2. Explicit Type Casting (Manual)

# 1. Implicit Type Casting (Automatic)
# Python khud hi data type ko convert kar deta hai jab zarurat ho.
a = 5      # int
b = 2.5    # float
c = a + b  # int + float = float (automatic conversion)
print(c)   # Output: 7.5

# 2. Explicit Type Casting (Manual)
# Jab hum khud data type ko convert karte hain.
x = "10"  # ye 10 ek string ke rup me hai ab use ham int  me convert kiya
y = int(x)   # string ko integer me convert kiya or dusre varible me store kiya 
print(y + 5) # Output: 15  isme y=10 tha or hame extra + 5 kiye jisse out put 15 aaya 

# Kuch common type casting functions:
# int(), float(), str(), bool(), list(), tuple(), set()

# Example: float to int
f = 9.99
i = int(f)   # Decimal part hata diya
print(i)     # Output: 9

# Example: int to string
num = 123
s = str(num)
print(s + " is a number")  # Output: 123 is a number

# Example: list to set (duplicates hat jayenge)
l = [1, 2, 2, 3]
s = set(l)
print(s)  # Output: {1, 2, 3}

# Example: bool to int
b = True
print(int(b))  # Output: 1

# Note:
# - Har conversion possible nahi hota. Jaise "abc" ko int me convert nahi kar sakte.
# - Type casting galat ho to error aata hai.

# Mazedaar fact:
# Python me type casting se hum data ko manipulate kar sakte hain, jaise user input (jo string hota hai) ko number me badalna, ya kisi calculation ke liye data type change karna.

# Practice karo, maza aayega!
