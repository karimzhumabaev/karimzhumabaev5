import pandas as pd

class DataAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def analyze_data(self):
        try:
            data = pd.read_csv(self.data_file)
            summary = data.describe()

            print("Data Analysis Summary:")
            print(summary)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    data_file = "path/to/data.csv"

    analyzer = DataAnalyzer(data_file)
    analyzer.analyze_data()

if __name__ == "__main__":
    main()
