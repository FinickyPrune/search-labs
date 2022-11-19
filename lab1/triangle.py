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

