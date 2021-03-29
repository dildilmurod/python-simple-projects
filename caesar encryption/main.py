import string


def caesar(text, shift, alphabets):
    def shift_alpha(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alpha = tuple(map(shift_alpha, alphabets))
    final_alpha = ''.join(alphabets)
    final_shifted = ''.join(shifted_alpha)
    table = str.maketrans(final_alpha, final_shifted)
    return text.translate(table)


plaintext = "Lorem ipsum dolor sit amet"
enctext = "Mpsfn jqtvn epmps tju bnfu"

shift = 1
rev = 26 - shift
shift %= 52

# print(len(string.ascii_lowercase))
print(caesar(plaintext, shift, [string.ascii_lowercase, string.ascii_uppercase]))
print(caesar(enctext, rev, [string.ascii_lowercase, string.ascii_uppercase]))

