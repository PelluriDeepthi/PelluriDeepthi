def mirrorchars(input, k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictchars = dict(zip(original, reverse))

    # Seperate out string after length k to change chars in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    # Change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictchars[suffix[i]]

    # Concat prefix and mirrored part
    print(prefix + mirror)

    # Driver Program
    if __name__ == "__main__":
        input = 'paradox'
        k = 3
        mirrorchars(input, k)