# Problem 4 Solution


# more elegant solution via slicing
def is_palindrome_short(n):
    return str(n) == str(n)[::-1]


# explicit check for a palindrome
def is_palindrome_long(n):
    n = str(n)  # convert to string

    i, j = 0, -1

    head = n[i]
    tail = n[j]

    while i < len(n):
        if not head == tail:
            return False

        i += 1
        j -= 1

    return True


print max( a*b for a in range(100, 1000) for b in range(100, 1000) if is_palindrome_short(a*b)  )

# solution is 906609
