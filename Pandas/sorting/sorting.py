import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 22, 30],
    "Salary": [50000, 60000, 45000, 70000],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSorted by Age:")
print(df.sort_values(by="Age"))
