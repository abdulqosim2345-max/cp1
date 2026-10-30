def replace_value(values, index, new_value):
    if 0 <= index < len(values):
        values[index] = new_value

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    min_value = min(values)
    max_value = max(values)
    total = sum(values)
    return (min_value, max_value, total)

original = []

number_of_days = int(input("Enter the number of days: "))
for i in range(number_of_days):
    data = int(input("Enter the data use in megabytes: "))
    original.append(data)

updated = original[:]

replace_index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new data to use: "))
replace_value(updated, replace_index, new_value)

target = int(input("Enter the data to search for: "))
found_data = find_first(updated, target)
target_count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_updated = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_updated}")
print(f"Minimum data use: {minimum} MB")
print(f"Maximum data use: {maximum} MB")
print(f"Total data use: {total} MB")
if found_data != -1:
    print(f"First matching index: {found_data}")
else:
    print("Target not found")
print(f"Matching values: {target_count}")
