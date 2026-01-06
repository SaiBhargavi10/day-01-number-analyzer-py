import sys
import statistics


def read_numbers_from_input():
    user_input = input("Enter numbers (space or comma separated): ")
    return user_input.replace(",", " ").split()


def parse_numbers(values):
    numbers = []
    for value in values:
        try:
            numbers.append(float(value))
        except ValueError:
            print(f"Ignoring invalid value: {value}")
    return numbers


def analyze(numbers):
    stats = {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.multimode(numbers),
        "range": max(numbers) - min(numbers),
        "sorted": sorted(numbers),
    }

    # Edge-case safe standard deviation
    if len(numbers) > 1:
        stats["std_dev"] = statistics.stdev(numbers)
    else:
        stats["std_dev"] = 0.0

    return stats


def show_result(stats):
    print("\n Number Analysis")
    print("-" * 40)
    print(f"Count           : {stats['count']}")
    print(f"Minimum         : {stats['min']:.2f}")
    print(f"Maximum         : {stats['max']:.2f}")
    print(f"Sum             : {stats['sum']:.2f}")
    print(f"Average         : {stats['avg']:.2f}")
    print(f"Median          : {stats['median']:.2f}")
    print(f"Mode            : {stats['mode']}")
    print(f"Std Deviation   : {stats['std_dev']:.2f}")
    print(f"Range           : {stats['range']:.2f}")
    print(f"Sorted Numbers  : {stats['sorted']}")
    print("-" * 40)


def main():
    if len(sys.argv) > 1:
        raw_values = sys.argv[1:]
    else:
        raw_values = read_numbers_from_input()

    numbers = parse_numbers(raw_values)

    if not numbers:
        print(" No valid numeric values were provided.")
        return

    stats = analyze(numbers)
    show_result(stats)


if __name__ == "__main__":
    main()
