# Question asked was you are given a map as a template.
# Given Map -> {"X":"123","Y":"456_%X%"}
# And you will be given with input as String
# "%X%_%Y%"
# In the given input you have replace templates with the values.


# Output should be "123_456_123"
hashmap= {"X":"123","Y":"456_%X%"} 
s = "%X%_%Y%"
def manipulateMap(hashmap,s):
    output = ""
    def replace_placeholders(s):
        while "%" in s:
            start = s.find("%")
            end = s.find("%", start + 1)
            if start == -1 or end == -1:
                break
            key = s[start + 1:end]
            if key in hashmap:
                s = s[:start] + hashmap[key] + s[end + 1:]
            else:
                break
        return s
    output = replace_placeholders(s)
    return output
print(manipulateMap(hashmap,s))