import pandas as pd
data ={
    "subject":["Applied physics","maths","python"],
    "Marks":[45,67,89]
}
df = pd.DataFrame(data)
print(df)
df.info()
