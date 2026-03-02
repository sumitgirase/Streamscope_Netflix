import pandas as pd
df = pd.read_csv("netflix_titles.csv")

#print(df.head())

#print(df.info())

#print(df.isnull().sum()) #it checks missing values in each columns

# for removing duplicates
#df.drop_duplicates(inplace=True)
#df['director'] = df['director'].fillna("Unknown")
#df['country'] = df['country'].fillna("Unknown")

#df['country'] = df['country'].str.strip().str.title()
#df['rating'] = df['rating'].str.strip()


df.to_csv("netflix_cleaned.csv", index=False)





