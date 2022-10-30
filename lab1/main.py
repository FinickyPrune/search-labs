
def triangle():
    def row(list0):
        list1 = []
        for i in range(len(list0)):
            list1.append(list0[i - 1] + list0[i])
        return list1 + [0]

    successful_input = False
    while not successful_input:
        try:
            n = int(input('Enter level: '))
            successful_input = True
        except ValueError:
            print('Try again.', end=' ')
    row_list = [0, 1, 0]
    row_str = str(n * [0] + row_list).replace("0", "").replace(",", "")
    print((n - 1) * ' ' + row_str[1:(len(row_str) - 2)])
    for i in range(n - 1):
        row_list = row(row_list)
        row_str = (n - i) * [0] + row_list
        zeros = str(row_str[:(n - i)]).replace("0", "").replace(",", " ")
        row_str = str(row_str[n - i + 1:]).replace(",", " ")
        print(zeros[1:len(zeros) - 1] + row_str[1:(len(row_str) - 2)])


def braces():
    sequence = input("Enter braces sequence:")
    allowed = "()"
    if not all(ch in allowed for ch in sequence):
        print("String contains not allowed characters.")
        return
    pairs = 0
    for ch in sequence:
        if ch == "(": pairs += 1
        if ch == ")": pairs -= 1

        if pairs < 0:
            print("Sequence is invalid.")
            return

    if pairs == 0:
        print("Sequence is valid.")
    else:
        print("Sequence is invalid.")


def cesar():

    en_alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    ru_alphabet = list(map(chr, range(ord('а'), ord('я') + 1)))
    index = ru_alphabet.index('е') + 1
    ru_alphabet.insert(index, 'ё')

    def shift(diff, message, alphabet):
        shifted_message = ""
        for i in message:
            index = alphabet.index(message[i])
            shifted_message += alphabet[len(alphabet) % (index + diff)]
        return shifted_message


if __name__ == '__main__':
    # triangle()
    # braces()
    cesar()
