# I used Copilot to generate this list because I was NOT doing this by hand I'm sorry.

number_to_char_count = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety")
}

letters_sum = 0

for n in range(0,1001):
    number = n
    if number <= 20:
        letters_sum += number_to_char_count[number]
    elif number < 100:
        if number in number_to_char_count:
            letters_sum += number_to_char_count[number]
        else:
            letters_sum += number_to_char_count[(number//10) * 10]
            number -= (number//10 * 10)
            letters_sum += number_to_char_count[number]
    elif number < 1000:
        if number == 100:
            letters_sum += number_to_char_count[number] + 3
        else:
            letters_sum += number_to_char_count[(number//100)] + 10
            number -= (number//100 * 100)
            letters_sum += number_to_char_count[(number//10) * 10] 
            number -= (number//10 * 10)
            letters_sum += number_to_char_count[number]
    else:
        letters_sum += 8
print(letters_sum)