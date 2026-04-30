import os
import csv
import json


# --- Task B1: Basic Functions ---

def check_files():
    print("Checking file...")
    if not os.path.exists('students.csv'):
        print("Error: students.csv not found.")
        return False

    print("Checking output folder...")
    if not os.path.exists('output'):
        os.makedirs('output')
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")
    return True


def load_data(filename):
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        print(f"Data loaded successfully: {len(data)} students")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []


def preview_data(students, n=5):
    print(f"\nFirst {n} rows:")
    for i in range(min(n, len(students))):
        s = students[i]
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")


# --- Task B2: Analysis Function ---

def analyse_countries(students):
    country_counts = {}
    for s in students:
        country = s['country']
        country_counts[country] = country_counts.get(country, 0) + 1


    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    top_3 = [{"country": k, "count": v} for k, v in sorted_countries[:3]]

    return {
        "total_students": len(students),
        "total_countries": len(country_counts),
        "top_3": top_3,
        "all_countries": country_counts
    }


# --- Main Logic ---

def main():
    # B1: Проверка и загрузка
    if not check_files():
        return

    try:
        students = load_data('students.csv')
    except Exception as e:
        print(f"General error: {e}")
        return

    if not students:
        return

    preview_data(students, 5)

    analysis_result = analyse_countries(students)
    print("\n--------------------")
    print("Country Analysis")
    print("--------------------")
    print(f"Total students: {analysis_result['total_students']}")
    print(f"Total countries: {analysis_result['total_countries']}")
    print("\nTop 3 Countries:")
    for i, item in enumerate(analysis_result['top_3'], 1):
        print(f"{i}. {item['country']} : {item['count']}")

    print("\n--------------------")
    print("Lambda / Map / Filter")

    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, students))
    print(f"Students with GPA > 3.5 : {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")

    good_attendance = []
    for s in students:
        try:
            if float(s['class_attendance_percent']) > 90:
                good_attendance.append(s)
        except ValueError:
            print(f"Warning: could not convert value for student {s['student_id']} - skipping row.")
            continue

    print(f"class_attendance_percent > 90 : {len(good_attendance)}")

    # B4: Тест ошибки
    print("\nTesting error handling:")
    load_data("wrong_file.csv")


if __name__ == "__main__":
    main()