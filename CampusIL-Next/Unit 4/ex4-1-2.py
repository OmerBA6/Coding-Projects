




def main():
    print (translate("el gato esta en la casa"))


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sentence_generator = (word for word in sentence.split(' '))
    translated_sentence = ""

    for word in sentence_generator:
        translated_sentence += words[word] + " "

    return translated_sentence

if __name__ == "__main__":
    main()