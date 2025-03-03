import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            if(cipher_direction == "encode"):
                end_text += alphabet[(alphabet.index(letter) + shift_amount) % 26]
            elif(cipher_direction == "decode"):
                end_text += alphabet[(alphabet.index(letter) - shift_amount) % 26]
        else:
            end_text += letter

    print (f"Here is your {cipher_direction}d result: {end_text}")


print (art.logo)
to_continue = "yes"

while to_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caser(start_text=text, shift_amount=shift, cipher_direction=direction)

    to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print ("Goodbye!")