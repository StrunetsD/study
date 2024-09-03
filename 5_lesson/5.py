def unique_checks(numbers):
    dict_count = {}
    duplicate = []

    for num in numbers:
        if num not in dict_count:
            dict_count[num] = 1
        else:
            dict_count[num] += 1

    for num in dict_count:
        if dict_count[num] > 1:
            duplicate.append((num, dict_count[num]))

    return duplicate


numbers = [1, 2, 2]
duplicates = unique_checks(numbers)

if not duplicates:
    print("numbers are unique")
else:
    print("duplicates:")
    for num, times in duplicates:
        print(f"number {num}, {times} times.")

