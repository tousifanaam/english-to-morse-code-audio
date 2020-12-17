def alphabet_counter(word):
    import string
    alphabet_list = list(string.ascii_lowercase)
    vowel = ['a', 'e', 'i', 'o', 'u']
    alphabet_dict = {}
    for i in alphabet_list:
        alphabet_dict[i] = 0
    base_10_numbers = []
    for i in range(0,10):
        i = str(i)
        base_10_numbers.append(i)

    non_alphabet = 0
    vowels = 0
    numbers = 0
    word = list(word.lower())
    for i in word:
        if i in alphabet_list:
             alphabet_dict[i] += 1
        else:
            non_alphabet += 1
        if i in vowel:
            vowels += 1
        if i in base_10_numbers:
            numbers += 1

    print("\n🔵 Total characters:  " + str(len(word)) + "\n")
    for key, value in alphabet_dict.items():
        if value != 0:
            print("❍ " + key + " = " + str(value))

    if vowels != 0:
        print("\n🔘 Vowels = " + str(vowels))

    if numbers != 0:
        print("\n⭕ Numbers = " + str(numbers))

    if non_alphabet != 0:
        print("\n⭕ Not an alphabet = " + str(non_alphabet))

def main():
    x = input("Throw in some characters:  ")
    print("\n░░░ Results ░░░\n\nShowing Results for:  '" + x + "'")
    alphabet_counter(x)

if __name__ == "__main__":
    main()