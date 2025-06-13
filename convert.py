import pandas as pd

# Read train.txt with correct separator and column names
df = pd.read_csv("train.txt", sep=";", header=None, names=["text", "emotion"])

# Drop empty rows (some rows may cause NaN errors)
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("emotions.csv", index=False)
print("✅ emotions.csv created successfully.")
