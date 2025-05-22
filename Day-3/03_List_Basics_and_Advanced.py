# 1. List Kya Hai? (What is a List?)
# List ek ordered collection hai jisme aap multiple items store kar sakte hain.
# List mutable hoti hai, yaani aap uske elements ko change, add, ya remove kar sakte hain.

my_list = [10, 20, 30, 40]
print("Original List:", my_list)

# 2. List ke Elements Change Karna (Modifying Elements)
my_list[1] = 99
print("After Changing 2nd Element:", my_list)

# 3. List me Element Add Karna (Adding Elements)
my_list.append(50)  # End me add karta hai
print("After Append:", my_list)

my_list.insert(2, 25)  # Kisi bhi position pe add kar sakte hain
print("After Insert at index 2:", my_list)

# 4. List me Element Remove Karna (Removing Elements)
my_list.remove(99)  # Value se remove karta hai
print("After Remove 99:", my_list)

removed = my_list.pop(1)  # Index se remove karta hai, value return bhi karta hai
print("After Pop index 1:", my_list, "| Removed:", removed)

# 5. List Slicing (Sub-list banana)
sub_list = my_list[1:3]
print("Sliced List (index 1 to 2):", sub_list)

# 6. List Comprehension (Advanced Way to Create List)
squares = [x**2 for x in range(5)]
print("Squares using List Comprehension:", squares)

# 7. Nested List (List ke andar List)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix:", matrix)
print("Access 2nd row, 3rd column:", matrix[1][2])

# 8. List Copy vs Reference (Shallow vs Deep Copy)
a = [1, 2, 3]
b = a  # Reference, dono same object ko point karte hain
b[0] = 100
print("a after b[0]=100:", a)

# Proper copy chahiye toh:
c = a.copy()  # Shallow copy
c[0] = 999
print("a after c[0]=999:", a, "| c:", c)

# 9. List Methods (Some Useful Methods)
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print("Sorted List:", numbers)
numbers.reverse()
print("Reversed List:", numbers)

# 10. Advanced: List Unpacking
data = [10, 20, 30]
x, y, z = data
print("Unpacked:", x, y, z)

# 11. Advanced: *args (Function me List Pass Karna)
def add_all(*args):
    return sum(args)

print("Sum using *args:", add_all(1, 2, 3, 4))

# 12. Advanced: Enumerate (Index ke sath Loop)
for idx, val in enumerate(['a', 'b', 'c']):
    print(f"Index {idx} has value {val}")



# List mutable hai, isliye dhyan rakhein ki jab bhi aap kisi list ko dusre variable me assign karte hain,
# toh wo reference hota hai, copy nahi. Agar copy chahiye toh .copy() ya list() ka use karein.

# Yeh the basic se advance list ke concepts with examples!