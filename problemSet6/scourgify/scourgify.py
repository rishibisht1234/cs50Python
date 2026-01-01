import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

source = sys.argv[1]
dest = sys.argv[2]

data = []

try:
    with open(source) as f:
        reader = csv.DictReader(f)
        for row in reader:
            last, first = row["name"].split(", ")
            data.append({
                "first": first,
                "last": last,
                "house": row["house"]
            })

except FileNotFoundError:
    sys.exit(f"Could not read {source}")

with open(dest, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(data)
