import re


def regexCheckPattern(number):
    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", number))


def convert(arabic):
    if arabic.isdigit():
        arabic = int(arabic)
        if arabic > 3999:
            return "Liczba powinna byc w zakresie 1 - 3999"
        return ATR(arabic)
    else:
        if regexCheckPattern(arabic):
            return RTA(arabic)

    return "niepoprawna liczba"


def ATR(number):
    arabic_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    if number == 0:
        return ""
    else:
        for arabic in arabic_dict:
            if number >= arabic:
                return arabic_dict[arabic] + str(ATR(number - arabic))
    return ""


def RTA(number):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    outp = 0

    for i in range(0, len(number)):
        if (i + 1) < len(number) and roman_dict[number[i]] < roman_dict[number[i + 1]]:
            outp -= roman_dict[number[i]]
            continue
        outp += roman_dict[number[i]]
    return outp


userInput = input("wpisz liczbe rzymska lub arabska:")
print(convert(userInput))