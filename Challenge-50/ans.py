import csv

def calculate_column_averages(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        totals = {}
        counts = {}

        for row in reader:
            for key, value in row.items():
                if key == "Name":
                    continue
                num = float(value)
                totals[key] = totals.get(key, 0) + num
                counts[key] = counts.get(key, 0) + 1

        averages = {subject: totals[subject] / counts[subject] for subject in totals}
        return averages

# Example usage
averages = calculate_column_averages("data.csv")
for subject, avg in averages.items():
    print(f"Average for {subject}: {avg:.2f}")
