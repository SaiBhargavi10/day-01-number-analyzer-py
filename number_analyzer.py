import statistics

def read_numbers():
    raw_input = input("Enter numbers (separated by space or comma): ")
    parts = raw_input.replace(",", " ").split()

    numbers = []
    for part in parts:
        try:
            numbers.append(float(part))
        except ValueError:
            print(f"Ignoring invalid value: {part}")

    return numbers

def analyze(numbers):
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "median": statistics.median(numbers),
        "range": max(numbers) - min(numbers),
    }


def show_result(stats):
    print("\nNumber Analysis")
    print("-" * 25)
    print(f"Count   : {stats['count']}")
    print(f"Min     : {stats['min']}")
    print(f"Max     : {stats['max']}")
    print(f"Sum     : {stats['sum']}")
    print(f"Average : {stats['avg']:.2f}")
    print(f"Median  : {stats['median']}")
    print(f"Range   : {stats['range']}")
    print("-" * 25)


def main():
    numbers = read_numbers()
    if not numbers:
        print("No valid numbers provided.")
        return

    stats = analyze(numbers)
    show_result(stats)


if __name__ == "__main__":
    main()
