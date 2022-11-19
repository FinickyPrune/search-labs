from datetime import datetime


def shift(diff, message, alphabet):
    shifted_message = ""
    for i in message:
        try:
            ind = alphabet.index(i)
            shifted_message += alphabet[(ind + diff) % len(alphabet)]
        except ValueError:
            shifted_message += i
            print("Skipping " + i + " symbol")
    return shifted_message


def input_file_path():
    return input("Enter file path: ")


def input_shift():
    successful_input = False
    while not successful_input:
        try:
            sh = int(input('Enter shift: '))
            successful_input = True
        except ValueError:
            print('Try again.', end=' ')
    return sh


def input_language():
    language = input("Enter language (ru or en): ")
    while language.lower() != 'ru' and language.lower() != 'en':
        language = input("Try again (ru or en): ")
    return language


def cesar():
    file_path = input_file_path()
    diff = input_shift()
    lang = input_language()

    alphabets = {'en': list(map(chr, range(ord('a'), ord('z') + 1))),
                 'ru': list(map(chr, range(ord('а'), ord('я') + 1)))}
    alphabets['ru'].insert(alphabets['ru'].index('е') + 1, 'ё')

    file = open(file_path, "r")
    content = file.read()
    file.close()

    shifted_content = shift(diff, content, alphabets[lang])

    file = open("output/cesar_output_" + datetime.now().strftime("%d-%m-%Y%H:%M:%S") + ".txt", "a")
    file.write(shifted_content)
    file.close()
