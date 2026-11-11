def parse_plate(plate):
    if not isinstance(plate, str):
        raise ValueError("Plate must be a string")
    parts = plate.split('-')
    if len(parts) != 4:
        raise ValueError("Plate must be in format: STATE-DISTRICT-SERIES-NUMBER")
    state, district, series, number = parts
    if not state or not district or not series or not number:
        raise ValueError("All plate fields must be non-empty")
    return state.upper(), int(district), int(number)


def trip_cost(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    text = text.strip().lower()
    if 'x' not in text:
        raise ValueError("Input must be in format: COUNTxRATE")
    count_str, rate_str = text.split('x', 1)
    if not count_str or not rate_str:
        raise ValueError("Count and rate must be non-empty")
    return int(count_str) * int(rate_str)


def axle_class(axles):
    if axles is None:
        raise ValueError("Axle count cannot be None")
    try:
        n = int(axles)
    except (ValueError, TypeError):
        raise ValueError("Axle count must be a valid integer")
    if n < 0:
        raise ValueError("Axle count cannot be negative")
    if n == 2:
        return 'car'
    if n <= 4:
        return 'truck'
    return 'heavy'


def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result)

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result)

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result)


if __name__ == "__main__":
    main()