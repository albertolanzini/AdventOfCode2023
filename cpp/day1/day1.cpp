#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

std::vector<std::string> handleInput(const std::string& inputfile) {
    std::vector<std::string> lines;
    std::ifstream file(inputfile);
    std::string line;

    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    return lines;

}


std::string findSingleSumPart1(const std::string& line) {
    int left = 0, right = line.length() - 1;

    while (left < right) {

        if (isdigit(line[left]) && isdigit(line[right])) {
            return std::string() + line[left] + line[right];
        }

        if (!isdigit(line[left])) {
            ++left;
        }

        if (!isdigit(line[right])) {
            --right;
        }
    }

    if (isdigit(line[left])) {
        return std::string() + line[left] + line[left];
    }

    return "00";

}


std::string mapNumberWords(const std::string& input_string) {
    std::unordered_map<std::string, char> number_word_to_digit = {
        {"zero", '0'}, {"one", '1'}, {"two", '2'}, {"three", '3'}, {"four", '4'},
        {"five", '5'}, {"six", '6'}, {"seven", '7'}, {"eight", '8'}, {"nine", '9'}
    };

    std::string result;
    size_t i = 0;

    while (i < input_string.length()) {
        bool replaced = false;

        for (const auto& pair : number_word_to_digit) {
            const std::string& number_word = pair.first;

            if (input_string.substr(i, number_word.length()) == number_word) {
                result += pair.second;
                i += number_word.length();
                replaced = true;
                break;
            }
        }

        if (!replaced) {
            result += input_string[i++];
        }

    }
    
    return result;

}

int findTotalSum(const std::vector<std::string>& input_list) {
    int total_sum = 0;

    for (const std::string& line : input_list) {
        if (!line.empty()) {
            std::string newLine = mapNumberWords(line);
            total_sum += std::stoi(findSingleSumPart1(newLine));
        }
    }

    return total_sum;
}

int main() {
    std::vector<std::string> data = handleInput("input.txt");
    std::cout << findTotalSum(data) << std::endl;
    return 0;
}