#
# file = open('my_file.txt')
# content = file.read()
# print(content)
# file.close()
#
# with open('my_file.txt') as file:
#     content = file.read()
#     print(content)


# with open('my_file.txt', mode="a") as file:
#     file.write("\nNew text.")

# with open('new_file.txt', mode="w") as file:
#     file.write("New text.")


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        with open("Input/Letters/starting_letter.txt", "r") as letter:
            text = letter.read()
            new_text = text.replace('[name]', name.strip())
        with open(f"Input/Letters/letter_for_{name}.txt", "w") as new_letter:
            new_letter.write(new_text)
