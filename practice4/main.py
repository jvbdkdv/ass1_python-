import csv
import json
import os
import csv
import json

# --- Task B1: Check File and Create Output Folder ---
print("Checking file...")
if not os.path.exists('students.csv'):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()
else:
    print("File found: students.csv")

print("\nChecking output folder...")
if not os.path.exists('output'):
    os.makedirs('output')
    print("Output folder created: output/")

# --- Task B2: Read CSV and Preview Data ---
students = []
with open('students.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

print(f"\nTotal students: {len(students)}")
print("\nFirst 5 rows:")
for i in range(5):
    s = students[i]
    # Форматирование вывода согласно примеру
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

# --- Task B3: Country Analysis ---
country_counts = {}
for s in students:
    country = s['country']
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

print("\nStudents by Country")
print("--------------------")
for country, count in sorted_countries:
    print(f"{country} : {count}")

print("\nTop 3 Countries:")
top_3 = sorted_countries[:3]
for i, (country, count) in enumerate(top_3, 1):
    print(f"{i}. {country} : {count}")

# --- Task B4: Save Results to JSON ---
result = {
    "analysis": "Country Analysis",
    "total_students": len(students),
    "top_3_countries": [{"country": c, "count": count} for c, count in top_3],
    "all_countries": country_counts
}

output_path = os.path.join('output', 'result.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

print("\n================================")
print("ANALYSIS RESULT")
print("================================")
print(f"Analysis : Country Analysis")
print(f"Total students : {len(students)}")
print(f"Total countries : {len(country_counts)}")
print("--------------------")
print("Top 3 Countries:")
for i, (country, count) in enumerate(top_3, 1):
    print(f"{i}. {country} : {count}")
print("================================")
print(f"Result saved to output/result.json")