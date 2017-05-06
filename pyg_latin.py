"""
PygLatin
"""
def pyglatin():
    """
    Solution for PygLatin
    """
    name = raw_input("Enter a word:")
    first_letter = name[0]
    name = name[1:len(name)] + first_letter + "ay"
    return name
print pyglatin()
