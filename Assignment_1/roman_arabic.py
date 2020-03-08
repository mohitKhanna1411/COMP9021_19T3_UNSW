import sys
import re
from math import log10
from itertools import permutations
from string import ascii_letters

def invalid_form():
    print("I don't get what you want, sorry mate!")
    sys.exit()

def invalid_value():
    print("Hey, ask me something that's not impossible to do!")
    sys.exit()

def final_valid_output(value,rule = ""):
    if len(rule) != 0:
        print("Sure! It is " + str(value) + " using " + str(rule))
    else:
        print("Sure! It is " + str(value))
    sys.exit()

def validate_arabic_number(arabic_number,rule):
    rule_len = len(rule)
    if rule_len%2 != 0:
        arabic_number_range = 10 ** (rule_len//2) * 4
    else:
        arabic_number_range = 10 ** (rule_len//2 - 1) * 9
    if arabic_number not in range(1,arabic_number_range):
        return False
    return True

def validate_roman_number(roman_number, rule):
    if len(rule)%2 != 0:
        rule_regex = '^' + rule[0] + "{0,3}"
        for i in range(1, len(rule)):
            if i%2 ==0:
                rule_regex += "("
                for j in [2, 1]:
                    rule_regex += rule[i] + rule[i-j] + '|'
                rule_regex += rule[i-1] + '?' + rule[i] + "{0,3}"
                rule_regex += ")"
    else:
        rule_regex =  ''
        for i in range(1, len(rule)):
            if i == 1:
                j_range = [1]
            else:
                j_range = [2, 1]
            if i%2 !=0:
                rule_regex += "("
                for j in j_range:
                    rule_regex += rule[i] + rule[i-j] + '|'
                rule_regex += rule[i-1] + '?' + rule[i] + "{0,3}"
                rule_regex += ")"
    rule_regex += '$'
    roman_match = re.match(rule_regex,roman_number)
    if roman_match:
        return True
    else:
        return False

def roman_to_arabic(roman_number, generic_rule_input="MDCLXVI"):
    generic_rule_input_reversed = generic_rule_input[::-1]
    generic_roman_number = 1
    generic_roman_rule = {}
    for i in range(len(generic_rule_input_reversed)):
        if i != 0:
            if i % 2 == 0:
                generic_roman_number *= 2
            else:
                generic_roman_number *= 5
        generic_roman_rule.setdefault(generic_rule_input_reversed[i], (i,generic_roman_number))

    converted_arabic_number = i = current_rank = next_rank = 0

    while i < len(roman_number):
        if i != len(roman_number) - 1:
            current_rank = generic_roman_rule[roman_number[i]][0]
            next_rank = generic_roman_rule[roman_number[i+1]][0]
        else:
            current_rank = next_rank

        if current_rank >= next_rank:
            converted_arabic_number += generic_roman_rule[roman_number[i]][1]
        else:
            converted_arabic_number += generic_roman_rule[roman_number[i+1]][1] - generic_roman_rule[roman_number[i]][1]
            i += 1
        i += 1
    return converted_arabic_number

def arabic_to_roman(arabic_number, generic_rule_input="MDCLXVI"):
    generic_rule_input_reversed = generic_rule_input[::-1]
    generic_roman_rule = []
    if len( generic_rule_input_reversed) == 1:
        generic_roman_rule.append((1,  generic_rule_input_reversed[0]))
    else:
        generic_roman_number = 1
        for i in range(len( generic_rule_input_reversed)):
            if i != 0:
                if i % 2 == 0:
                    generic_roman_number *= 2
                else:
                    generic_roman_number *= 5
            generic_roman_rule.append((generic_roman_number,  generic_rule_input_reversed[i]))

    generic_roman_rule_reversed = generic_roman_rule[::-1]
    pow_ten = []
    for a, r in generic_roman_rule_reversed:
        if log10(a).is_integer():
            pow_ten.append((a, r))

    for aten, rten in pow_ten:
        for a, r in generic_roman_rule_reversed:
            if 1 < a/aten <= 10:
                generic_roman_rule.append((a - aten, rten + r))
    generic_roman_rule.sort(reverse=True)
    converted_roman = ""
    for i in range(len(generic_roman_rule)):
        occurrence = arabic_number//generic_roman_rule[i][0]
        arabic_number %= generic_roman_rule[i][0]

        for j in range(occurrence):
            converted_roman += generic_roman_rule[i][1]

    if not arabic_number:
        return converted_roman
    else:
        invalid_value()

def case_one(val):
    if type(val) == str:
        converted_arabic_number = roman_to_arabic(val)
        return str(converted_arabic_number)
    else:
        converted_roman = arabic_to_roman(val)
        return str(converted_roman)

def case_two(val,rule):
    if type(val) == str:
        converted_arabic_number = roman_to_arabic(val,rule)
        return str(converted_arabic_number)
    else:
        converted_roman = arabic_to_roman(val,rule)
        return str(converted_roman)

def case_three(val):
    def validate_possible_rule(possible_rule, extra_letters):
        possible_rule_reverse = possible_rule[::-1]
        rule_len = len(possible_rule)
        for i in range(rule_len):
            if possible_rule_reverse[i] in extra_letters and (i % 2 == 0 or i == rule_len - 1):     
                return False                                                                       
            if possible_rule_reverse[i] in repeated_roman and i % 2 == 1:
                return False
        return True
    i = 0
    repeated_roman = []

    while i < len(val):
        j = i + 1
        while j < len(val):
            if val[i] == val[j] and val[i] not in repeated_roman:
                repeated_roman.append(val[i])
                if j - i > 3:
                    invalid_value()
            j += 1
        i += 1
    used_char = list(set(val))
    unused_char = list(set(ascii_letters) - set(val))
    null_char = -1
    smallest_arabic_number = sys.maxsize
    smallest_arabic_rule = []
    extra_letters = []
    converted_arabic_number = sys.maxsize
    while null_char < len(used_char):
        if null_char> -1:
            extra_letters.append(unused_char[null_char])
        all_possible_rules = list(permutations(used_char + extra_letters))
        for possible_rule in all_possible_rules:
            if not validate_possible_rule(possible_rule, extra_letters):
                continue
            if validate_roman_number(val,possible_rule):
                converted_arabic_number = roman_to_arabic(val, possible_rule)
            else:
                continue
            if converted_arabic_number < smallest_arabic_number:
                smallest_arabic_number = converted_arabic_number
                smallest_arabic_rule = possible_rule
        if smallest_arabic_number != sys.maxsize:
            break
        null_char += 1

    smallest_rule = ""
    for letter in smallest_arabic_rule:
        if letter not in used_char:
            smallest_rule += "_"
        else:
            smallest_rule += letter
    if smallest_arabic_number == sys.maxsize:
        invalid_value()
    else:
        return smallest_arabic_number,smallest_rule
    return

def check_input(input_command, rule="MDCLXVI"):
    try:
        if re.match(r'[0]+\d*', input_command):
            invalid_value()
        if not validate_arabic_number(int(input_command), rule):
            invalid_value()
        return int(input_command)
            
    except ValueError:
        if not validate_roman_number(input_command, rule):
            invalid_value()
        return input_command

def check_rule(gen_rule):
    set_gen_rule = set(gen_rule)
    if len(set_gen_rule) != len(gen_rule):
        return False
    if re.search(r'[^a-zA-Z]+', gen_rule): 
        return False
    return True

def main():
    input_command = input('How can I help you? ')
    input_command_list = input_command.split()

    if all(x in input_command_list for x in ['Please', 'convert']):
        if len(input_command_list) == 4 and input_command_list[0] == "Please" and input_command_list[1] == "convert" and input_command_list[3] == "minimally":
            if re.search(r'[^a-zA-Z]+', input_command_list[2]):
                invalid_value()
            output,rule = case_three(input_command_list[2])
            final_valid_output(output,rule)

        elif len(input_command_list) == 5 and input_command_list[0] == "Please" and input_command_list[1] == "convert" and input_command_list[3] == "using":
            if not check_rule(input_command_list[4]):
                invalid_value()
            validated_input_value = check_input(input_command_list[2],input_command_list[4])
            output = case_two(validated_input_value,input_command_list[4])
            final_valid_output(output)

        elif len(input_command_list) == 3 and input_command_list[0] == "Please" and input_command_list[1] == "convert":
            validated_input_value = check_input(input_command_list[2])
            output = case_one(validated_input_value)
            final_valid_output(output)

        else:
            invalid_form()

    else:
        invalid_form()

if __name__ == '__main__':
    main()
