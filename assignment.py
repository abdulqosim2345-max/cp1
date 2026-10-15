def classify(value):
    if value < 208:
        return "Below range"
    if value <= 212:
        return "In range"
    return "Above range"


def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result


sheet_count = int(input("Enter the number of paper sheets: "))

total_width = 0
below_range_count = 0
in_range_count = 0
above_range_count = 0

for _ in range(sheet_count):
    width = int(input("Enter the paper sheet width: "))
    classification = classify(width)
    print(classification)
    total_width += width

    if classification == "Below range":
        below_range_count += 1
    elif classification == "In range":
        in_range_count += 1
    else:
        above_range_count += 1

average_width = calculate_average(total_width, sheet_count)

print(f"Total width: {total_width} mm")
print(f"Average width: {average_width} mm")
print(f"Below range: {below_range_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_range_count}")