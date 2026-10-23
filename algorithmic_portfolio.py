def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def bubble_sort(numbers):
    arr = numbers.copy()

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    numbers = [40, 10, 50, 20, 30]

    print("\n=== Algorithmic Problem-Solving Portfolio ===")
    print("Original numbers:", numbers)

    target = int(input("Enter a number to search: "))
    result = linear_search(numbers, target)

    if result != -1:
        print("Number found at index:", result)
    else:
        print("Number not found!")

    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers:", sorted_numbers)


if __name__ == "__main__":
    main()