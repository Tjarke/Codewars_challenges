"""
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

"""
def decrypt(encrypted_text, n):
    i = 0
    orig = encrypted_text
    while i<n:
        decr = ""
        first_chars = orig[int(len(orig)/2):]
        scnd_chars = orig[:int(len(orig)/2)]
        decr = "".join([i[0]+i[1] for i in zip(first_chars,scnd_chars)])
        if len(orig)%2 != 0:
            decr += first_chars[-1]
        orig = decr
        i += 1
    return orig


def encrypt(text, n):
    i = 0
    enc = text
    while i < n:
        first_half = ""
        second_half = ""
        for cnt, val in enumerate(enc):
            if cnt%2 == 0:
                second_half += val
            else:
                first_half += val
        enc = first_half + second_half
        i += 1
    return enc


