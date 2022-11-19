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
