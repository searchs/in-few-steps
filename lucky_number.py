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
    2: "Natural peacemakers",
    3: "Creative and optimistic",
    4: "Hard workers",
    5: "Value freedom",
    6: "Carers and providers",
    7: "Thinkers",
    8: "Have diplomatic skills",
    9: "Selfless and generous",
}

def calculate_name_value(name: str) -> int:
    """Calculates the numerical value of a given name based on `letter_grid`.

    Each letter in the name corresponds to a specific numerical value.
    The function sums these values to compute the total value of the name.

    Args:
        name (str): The name to calculate the value for.

    Returns:
        int: The total numerical value of the name.
    """
    total = 0
    for letter in name:
        for key, value in letter_grid.items():
            if letter in value:
                total += key
    print(name.capitalize(), total)
    return total

def calculate_combined(value_to_transform: int) -> int:
    """Reduces a given number to a single-digit value by summing its digits.

    If the result is greater than 9, the function recursively reduces the sum
    until a single-digit number is obtained.

    Args:
        value_to_transform (int): The number to be reduced.

    Returns:
        int: A single-digit number obtained by repeatedly summing the digits.
    """
    combined_str = str(value_to_transform)
    start_total = 0
    for item in combined_str:
        start_total += int(item)

    if start_total > 9:
        return calculate_combined(start_total)
    return start_total

def add_name_values(first_total: int, last_total: int) -> int:
    """Adds the numerical values of the first and last names.

    Args:
        first_total (int): The numerical value of the first name.
        last_total (int): The numerical value of the last name.

    Returns:
        int: The sum of the numerical values of the first and last names.
    """
    return first_total + last_total

def get_lucky_number_meaning(number: int) -> str:
    """Retrieves the meaning associated with a given number from `meaning_grid`.

    Args:
        number (int): The number for which the meaning is to be retrieved.

    Returns:
        str: The meaning associated with the number, or a default message if the number
             is not found in `meaning_grid`.
    """
    return meaning_grid.get(number, "Value is not included in meanings")

def main():
    """Main function to execute the lucky number calculation and display the meaning.

    Prompts the user for their full name, calculates the lucky number based on
    the name values, and prints the corresponding meaning.
    """
    full_name = input("What is your full name please? ")
    first_name, last_name = full_name.upper().split()
    first_total = calculate_name_value(first_name)
    last_total = calculate_name_value(last_name)
    combined = add_name_values(first_total, last_total)
    combined_total = calculate_combined(combined)
    print(f"Lucky Number: {combined_total}")
    print("Meaning: ", get_lucky_number_meaning(combined_total))

if __name__ == "__main__":
    main()
