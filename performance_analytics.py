def build_performance_dataframe_from_students(students, pd):
    data = []
    for student in students:
        subject_scores = student["subject_scores"]
        if {"Math", "Science", "English"} <= subject_scores.keys():
            data.append(
                {
                    "Name": student["name"],
                    "Math": subject_scores["Math"],
                    "Science": subject_scores["Science"],
                    "English": subject_scores["English"],
                }
            )
    if not data:
        return None
    return pd.DataFrame(data)


def performance_analytics(students):
    print("\n=== Student Performance Analysis ===")
    try:
        import numpy as np
        import pandas as pd
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Required libraries are not installed: NumPy, Pandas, or Matplotlib.")
        return

    print("1. Analyze data from CSV file")
    print("2. Analyze registered students with subject scores")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            csv_path = input(
                "Enter CSV file path (press Enter for student_performance.csv): "
            ).strip()
            if not csv_path:
                csv_path = "student_performance.csv"
            df = pd.read_csv(csv_path)
        elif choice == "2":
            df = build_performance_dataframe_from_students(students, pd)
            if df is None or df.empty:
                print("No registered students have complete subject scores.")
                return
            csv_path = "student_performance_from_students.csv"
            df.to_csv(csv_path, index=False)
            print(f"Performance data saved to {csv_path}")
        else:
            print("Invalid choice.")
            return

        required_columns = {"Name", "Math", "Science", "English"}
        if not required_columns.issubset(df.columns):
            print("CSV file must contain Name, Math, Science, and English columns.")
            return

        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy(dtype=float)
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)

        print("\n--- NumPy Analysis ---")
        print("Mean Scores (Math, Science, English):", mean_scores)
        print("Median Scores (Math, Science, English):", median_scores)
        print("Standard Deviation (Math, Science, English):", std_dev_scores)

        top_math = df.loc[df["Math"].idxmax(), "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")
        print("Math:", top_math)
        print("Science:", top_science)
        print("English:", top_english)

        subjects = ["Math", "Science", "English"]
        plt.figure(figsize=(8, 5))
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("average_scores.png")
        plt.close()

        ax = df.plot(
            x="Name", y=["Math", "Science", "English"], kind="bar", figsize=(10, 6)
        )
        ax.set_title("Student Performance Comparison")
        ax.set_ylabel("Scores")
        plt.tight_layout()
        plt.savefig("student_performance_comparison.png")
        plt.close()

        print("\nCharts saved as average_scores.png and student_performance_comparison.png")
    except FileNotFoundError:
        print("Error: The CSV file was not found. Please check the file path.")
    except Exception as error:
        print("Unexpected Error:", error)
