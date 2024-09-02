letter_grid = {
    1: ["A", "J", "S"],
    2: ["B", "K", "T"],
    3: ["C", "L", "U"],
    4: ["D", "M", "V"],
    5: ["E", "N", "W"],
    6: ["F", "O", "X"],
    7: ["G", "P", "Y"],
    8: ["H", "Q", "Z"],
    9: ["I", "R"],
}

# Create a reverse mapping of letters to their corresponding values
letter_to_value = {letter: key for key, letters in letter_grid.items() for letter in letters}

meaning_grid = {
    1: "Natural leaders",
    2: "Natural peacemakers",
    3: "Creative and optimistic",
    4: "Hard workers",
    5: "Value freedom",
    6: "Carers and providers",
    7: "Thinkers",
    8: "Have diplomatic skills",
    9: 'Selfless and generous',
}

def calculate_name_value(name: str) -> int:
    # Calculate the total by summing the values of the letters in the name
    total = sum(letter_to_value.get(letter, 0) for letter in name)
    print(name.capitalize(), total)
    return total

def calculate_combined(value_to_transform: int) -> int:
    # Calculate the sum of the digits, repeating if the result is greater than 9
    combined_total = sum(int(digit) for digit in str(value_to_transform))
    return combined_total if combined_total <= 9 else calculate_combined(combined_total)

def add_name_values(first_total: int, last_total: int) -> int:
    return first_total + last_total

def get_lucky_number_meaning(number: int) -> str:
    return meaning_grid.get(number, "Value is not included in meanings")

def main():
    full_name = input("What is your full name please? ")
    first_name, last_name = full_name.upper().split()

    lucky_number = calculate_combined(sum(list(map(calculate_name_value, [first_name, last_name]))))
    print(f"Lucky Number: {lucky_number}")
    print("Meaning: ", get_lucky_number_meaning(lucky_number))

if __name__ == "__main__":
    main()
