#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <regex>

class GameValidator {
private:
    std::vector<std::string> data;
    int max_red = 12;
    int max_green = 13;
    int max_blue = 14;

    std::vector<std::string> split_line(const std::string& line) {
        std::vector<std::string> result;
        std::regex rgx("[;,:]");
        std::sregex_token_iterator iter(line.begin(), line.end(), rgx, -1);
        std::sregex_token_iterator end;

        while (iter != end) {
            result.push_back(*iter);
            ++iter;
        }

        return result;
    }

    std::pair<std::string, int> handle_draw(const std::string& draw) {
        std::string color;
        std::string num_str;

        for (char ch : draw) {
            if (std::isalpha(ch))
                color += ch;
            else if (std::isdigit(ch))
                num_str += ch;
        }
        
        return std::make_pair(color, std::stoi(num_str));
    }

public:
    GameValidator(const std::string& inputfile) {
        std::ifstream file(inputfile);
        std::string line;

        while (std::getline(file, line)) {
            data.push_back(line);
        }
    }

    std::vector<std::string> getData() const {
        return data;
    }

        bool validate_line_p1(const std::string& line) {
        auto parts = split_line(line);

        for (size_t i = 1; i < parts.size(); ++i) {
            const auto [color, num] = handle_draw(parts[i]);
            if ((color == "green" && num > max_green) ||
                (color == "red" && num > max_red) ||
                (color == "blue" && num > max_blue)) {
                return false;
            }
        }
        return true;
    }

    int min_numbers_p2(const std::string& line) {
        auto parts = split_line(line);

        int min_green = 0, min_blue = 0, min_red = 0;

        for (size_t i = 1; i < parts.size(); ++i) {
            const auto [color, num] = handle_draw(parts[i]);

            if (color == "green")
                min_green = std::max(min_green, num);
            if (color == "blue")
                min_blue = std::max(min_blue, num);
            if (color == "red")
                min_red = std::max(min_red, num);
        }

        return min_blue*min_green*min_red;
    }

};

int main() {
    std::string input_file = "input.txt";
    GameValidator game_validator(input_file);
    int total_num_ids = 0;
    int total_power_sum = 0;

    // Part 1 usage
    int i = 0;
    for (const auto& line : game_validator.getData()) {
        if (game_validator.validate_line_p1(line));
        {
            total_num_ids += (1 + i);
        }
        ++i;
    }

    // Part 2 usage
    for (const auto& line : game_validator.getData()) {
        total_power_sum += game_validator.min_numbers_p2(line);
    }

    std::cout << "The total sum of IDs is " << total_num_ids << std::endl;
    std::cout << "The total sum for Part 2 is: " << total_power_sum << std::endl;

    return 0;
}