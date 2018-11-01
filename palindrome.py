# USER INPUT (TEXT), CLEAN TEXT, INNER FUNCTION COMPARING 1st & LAST 
# CHARACTERS, & THEN WORKING INWARDS:

text = input("Enter text to see if it is a palindrome: ")

def clean_text(text):
    """
    Given text by user, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text.lower()
    for char in text:
        if char.isalpha():
            new_text = new_text + char
    return new_text

print("You entered: " + clean_text(text))

def palindrome_test(text):
    """
    Here is where we loop through the "cleaned text" and compare first character to last character, 
    looping inwards if that's true.
    """

    if clean_text(text) == '':
        print("This is a Palindrome")

    elif clean_text(text)[0] == clean_text(text)[-1]:
        palindrome_test(clean_text(text)[1:-1])

    else:
        print("This is not a Palindrome")
        
palindrome_test(clean_text(text))
    
    

# TRYING THE INNER LOOP ANOTHER WAY, GETTIN ERRORZ

# def inner(new_text):
#     """
#     Compares first and last value of the string, working from the outside in.
#     """
#     new_text = clean_text(new_text)
#     if len(new_text) == 2 and new_text[0] == new_text[-1]:
#         return
#         inner(user_entry[0:-1])

#         if inner(user_entry)[0:-1] == True:
#             inner(user_entry)[0+1:-1-1]

#             if inner(user_entry[0+1:-1-1]) == True:
#                 print("This is a palindrome")



# MANUAL BABYSTEPS FROM BEFORE AFTERNOON LECTURE:

# if user_entry is (" "):
#     print ("This is TECHNICALLY a palindrome, BUT type some text and let`'s DO THIS")
    
# if len(user_entry) == 0:
#     print ("This is a palindrome")

# if len(user_entry) == 1:
#     print ("This is a palindrome")

# if len(user_entry) == 2 and [0==1]:
#     print ("This is a palindrome")

# if len(user_entry) == 3 and [0==2]:
#     print ("This is a palindrome")

# FROM STACK OVERFLOW, BUT NOT THE RECOMMENDED WAY TO SOLVE JUST YET. NEED TO LEARN THE LESSON DAMNIT:
# # if user_entry == user_entry[::-1]:
# #     print ("This is a palindrome")