alphabets = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]


def cipher():
    again = 'yes'
    while again == 'yes':
        request = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(encode(message, shift) if request == 'encode' else decode(message, shift))
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")


def encode(message, shift):
    return ''.join([alphabets[alphabets.index(letter) + shift] for letter in message])


def decode(message, shift):
    return ''.join([alphabets[alphabets.index(letter, 26) - shift] for letter in message])


if __name__ == '__main__':
    cipher()
