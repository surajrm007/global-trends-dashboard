import pandas as pd

def load_data(file_path):
    # Show raw output for debugging
    df = pd.read_csv(file_path)
    print("🔍 Raw Columns:", list(df.columns))
    print("📄 First row of data:")
    print(df.head(1))

    # Clean column names
    df.columns = df.columns.str.strip()

    # Final check
    if "Value" not in df.columns:
        raise ValueError("🛑 'Value' column not found after cleaning. Check CSV header.")

    df.dropna(subset=["Value"], inplace=True)
    df["Year"] = df["Year"].astype(int)
    df["Value"] = df["Value"].astype(float)

    return df


