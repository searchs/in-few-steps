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

meaning_grid = {
    1: "Natural leaders",
    2:"Natural peacemakers",
    3: "Creative and optimistic",
    4: "Hard workers",
    5: "Value freedom",
    6: "Carers and providers",
    7: "Thinkers",
    8: "Have diplomatic skills",
    9: 'Selfless and generous',
}

def calculate_name_value(name) -> int:
    total = 0
    for letter in name:
        for key, value in letter_grid.items():
            if letter in value:
                total += key
    print(name.capitalize(), total)
    return total

def calculate_combined(value_to_transform: int) -> int:
    combined_str = str(value_to_transform)
    start_total = 0
    for item in combined_str:
        start_total += int(item)

    if start_total > 9:
        return calculate_combined(start_total)
    return start_total


def add_name_values(first_total, last_total):
    return first_total + last_total

def get_lucky_number_meaning(number) -> str:
    return meaning_grid.get(number, "Value is not included in meanings" )

def main():
    full_name = input("What is your full name please? ")
    first_name, last_name = full_name.upper().split()
    first_total = calculate_name_value(first_name)
    last_total = calculate_name_value(last_name)
    combined = add_name_values(first_total, last_total)
    combined_total = calculate_combined(combined)
    print(f"Lucky Number: {combined_total}")
    print("Meaning: ",get_lucky_number_meaning(combined_total))



if __name__ == "__main__":
    main()
