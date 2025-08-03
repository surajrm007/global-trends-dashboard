from src.load_data import load_data
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = load_data("data/world_data.csv")
    print("🔍 Columns in your file:", df.columns)
