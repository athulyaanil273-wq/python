from collections import Counter

def analyze_logs(filename):
    counter = Counter()

    with open(filename, "r") as file:
        for line in file:
            if "INFO" in line:
                counter["INFO"] += 1
            elif "WARNING" in line:
                counter["WARNING"] += 1
            elif "ERROR" in line:
                counter["ERROR"] += 1

    return counter


result = analyze_logs("app.log")

print("Log Summary")
print("-" * 20)

for level, count in result.items():
    print(f"{level}: {count}")
