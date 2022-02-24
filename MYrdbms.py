import pandas as pd
#r stands for "raw" and will cause backslashes in the string
#to be interpreted as actual backslashes rather than special characters.
df = pd.read_csv(r"C:\Users\idris\OneDrive\Bureau\Study\s6\yellow_tripdata_2009-01.csv")
print(df.info())

