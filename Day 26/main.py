import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# for key, value in student_dict.items():
#     print(key)
#     print(value)

# student_data_frame = pandas.DataFrame(student_dict)

# for key, value in student_data_frame.items():
#     print(key)
#     print(value)

# for key, row in student_data_frame.iterrows():
#     print(row)
#     # if row.student == "Angela":
#     #     print(row.score)

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for _, row in nato_alphabets.iterrows()}
user_word = input("Enter a word: ").upper()
print([alpha_dict[letter] for letter in user_word])
