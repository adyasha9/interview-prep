# You are given two strings, P and Q consisting of characters 'a' and 'b'.

# At any given point you can perform two kind of operations on the string P:


# You either append character a to P.
# You append character b to P and then you reverse P.
# You can perform any of these operations any number of times.


# You have to tell me whether it is possible for P to be equal to Q, after performing such operations?


# An example:


# P = "a"
# Q = "baa"
#  this will return true,
# P = "b" 
# Q = "ab"
# , this will return false

def canTransform(P,Q):
    possible_strings = {P}
    seen_strings = set()
    max_length = len(Q) 
    while possible_strings:
        current = possible_strings.pop()
        if current == Q:
            return True
        if current in seen_strings or len(current) > max_length:
            continue
        seen_strings.add(current)
        possible_strings.add(current + 'a')
        possible_strings.add((current + 'b')[::-1])
    return False

print(canTransform("a", "baa"))   # True
print(canTransform("b", "ab"))    # False
print(canTransform("a", "ababa")) # False
print(canTransform("a", "bbb"))   # False
print(canTransform("a", "aab"))   # False
print(canTransform("b", "babb"))  # True
    