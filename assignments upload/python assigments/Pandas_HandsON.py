import pandas as pd
df = pd.read_csv("data/interviews.csv")
print(df.shape)
df.head()
get_ipython().run_line_magic('timeit', '-n1000 df["Date"]')
get_ipython().run_line_magic('timeit', '-n1000 df.iloc[0]')
get_ipython().run_line_magic('timeit', '-n1 df.apply(lambda x: x["Experience"] * x["Upvotes"], axis=1)')
get_ipython().run_line_magic('timeit', '-n1 [row for index, row in df.iterrows()]')
for index, row in df.iterrows():
    print(row)
    break
get_ipython().run_line_magic('timeit', '-n1 [row for row in df.itertuples()]')

for row in df.itertuples():
    print(row)
    break
get_ipython().run_line_magic('timeit', '-n1 df_np = df.to_numpy(); rows = [row for row in df_np]')
df_np = df.to_numpy()
get_ipython().run_line_magic('timeit', '-n1000 df_np[0]')
get_ipython().run_line_magic('timeit', '-n1000 df_np[:,0]')
get_ipython().run_line_magic('timeit', '-n1000 df["Review"][0]')
get_ipython().run_line_magic('timeit', '-n1000 df.iloc[0]["Review"]')
get_ipython().run_line_magic('timeit', '-n1000 df.loc[0, "Review"]')
df.loc[0, "Review"] = "Orange is love. Orange is life."
df.head()
df.loc[df["Company"] == "Apple", "Company"] = "Orange"
df.head()
pd.set_option("mode.chained_assignment", "raise")
df.iloc[3]
df.iloc[-6:]
df.iloc[-6::2]
df.loc[df["Offer"] == "Declined offer"]
def company_type(x):
    hardware_companies = set(["Orange", "Dell", "IBM", "Siemens"])
    return "Hardware" if x["Company"] in hardware_companies else "Software"
df["Type"] = df.apply(lambda x: company_type(x), axis=1)
df = df.set_index("Type")
df
df.loc["Hardware"]
df.reset_index(drop=True, inplace=True)
df
series = df.Company
series[:1000:100]
df["Review"].str.lower()
df.Review.str.len()
df.loc[df["Review"].str.contains("days"), "Process"] = "Short"
df.loc[df["Review"].str.contains("week"), "Process"] = "Average"
df.loc[df["Review"].str.contains("month|[4-9]+[^ ]* weeks|[1-9]\d{1,}[^ ]* weeks"), "Process"] = "Long"
df[~df.Process.isna()][["Review", "Process"]]
pd.set_option('display.max_colwidth', 100)
df[~df.Process.isna()][["Review", "Process"]]
pd.Series.str.__dict__.keys()
pd.Series._accessors
df.tail(8)
df.describe()
df.info()
import sys
df.apply(sys.getsizeof)
df.Company.nunique()
df.Company.value_counts()
