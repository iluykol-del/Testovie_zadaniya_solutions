def delete_dubl(numbers: list[int]) -> list[int]:
    result = []

    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        elif num != numbers[i - 1]:
            result.append(num)

    return result