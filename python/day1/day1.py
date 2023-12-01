from typing import List
import re

def handleInput(inputfile: str) -> List[str]:
    with open(inputfile, 'r') as file:
        return file.read().split('\n')

def findSingleSumPart1(line: str) -> str:

    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    left, right = 0, len(line)-1

    foundLeft, foundRight = False, False

    while left < right:
        

        if line[left] in num_list:
            foundLeft = True

        if line[right] in num_list:
            foundRight = True

        if foundLeft == True and foundRight == True:
            return line[left] + line[right]

        if not foundLeft:
            left += 1
        if not foundRight:
            right -= 1

    if line[left].isdigit():
        return line[left] + line[left]

# modified findSingleSumPart1 function
def map_number_words(input_string: str) -> str:
    number_word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    result, i = '', 0

    while i < len(input_string):
        
        replaced = False
        
        for number_word in sorted(number_word_to_digit, key=len, reverse=True):
            if input_string[i:i+len(number_word)] == number_word:

                result += number_word_to_digit[number_word]
                
                i += len(number_word)-1
                replaced = True
                break

        if not replaced:
            result += input_string[i]
            i += 1

    return result


def findTotalSum(input_list: List[str]) -> int:
    
    total_sum = 0

    for line in input_list:
        if line:
            newLine = map_number_words(line)
            total_sum += int(findSingleSumPart1(newLine))

    return total_sum

data = handleInput('input.txt')
print(findTotalSum(data))


    
        
    

    

