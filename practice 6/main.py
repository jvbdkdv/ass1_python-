import os
import csv
import json


# --- Task 1: Class FileManager ---
class FileManager:
    def __init__(self, filename):
        self.filename = filename  #

    def check_file(self):
        #
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        #
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


# --- Task 2: Class DataLoader ---
class DataLoader:
    def __init__(self, filename):
        self.filename = filename  #
        self.students = []  #

    def load(self):
        #
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print("Error: File not found.")
            return []

    def preview(self, n=5):
        #
        print(f"First {n} rows:")
        for i in range(min(n, len(self.students))):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")


# --- Task 3: Class DataAnalyser (Variant B) ---
class DataAnalyser:
    def __init__(self, students):
        self.students = students  #
        self.result = {}  #

    def analyse(self):
        country_counts = {}
        for s in self.students:
            country = s['country']
            country_counts[country] = country_counts.get(country, 0) + 1

        sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
        top_3 = [{"country": c, "count": count} for c, count in sorted_countries[:3]]

        self.result = {
            "country_counts": country_counts,
            "total_countries": len(country_counts),
            "top_3": top_3
        }
        return self.result

    def print_results(self):
        #
        print("Country Analysis")
        print(f"Total countries: {self.result['total_countries']}")
        print("Top 3 Countries:")
        for i, item in enumerate(self.result['top_3'], 1):
            print(f"{i}. {item['country']}: {item['count']}")


# --- Task 4: Class ResultSaver ---
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result  #
        self.output_path = output_path  #

    def save_json(self):
        #
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving JSON: {e}")


# --- Task 5: Main Program ---
if __name__ == "__main__":
    #
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()