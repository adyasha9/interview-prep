# Given two strings s1 and s2, find out if they only differ by the insertion of a phrase.


# Example:


# The boy goes to the hospital
# The cute little boy goes to the hospital
# 'little boy' is the added phrase everything else is the same so return True

# Example:

# The boy is nice.
# The girl is nice.
# -> Return False

def is_inserted_phrase(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    
    i, j = 0, 0
    inserted = False # check if a phrase is added

    while i < len(words1) and j < len(words2):
        if words1[i] == words2[j]:  # Matching word
            i += 1
            j += 1
        elif not inserted:  # First mismatch (potential phrase insertion)
            while j < len(words2) and (i >= len(words1) or words1[i] != words2[j]):
                j += 1
            if i < len(words1) and words1[i] == words2[j-1]:  # Ensuring only one insertion
                inserted = True
            else:
                return False
        else:  # Second mismatch -> more than one insertion/replacement
            return False

    return True
