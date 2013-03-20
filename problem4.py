# Problem 4 Solution

def is_palindrome(n):
    n = str(n)  # convert to string

    i, j = 0, -1

    head = n[i]
    tail = n[j]

    while i < len(n):

        if not iterate_letters(head, tail):
            return False

        i += 1
        j -= 1

    return True


def iterate_letters(head, tail):
    return head == tail


print is_palindrome(9009) # test even case
print is_palindrome(50) # test false case
print is_palindrome(5) # test edge case
print is_palindrome(91019) # test odd case



