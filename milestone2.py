import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")
"""

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year added
df['year_added'] = df['date_added'].dt.year

# Count content added per year
yearly_growth = df['year_added'].value_counts().sort_index()

plt.figure()
yearly_growth.plot()
plt.title("Netflix Content Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.show() """

#STEP 2:Visualize Distribution of Content Type
"""sns.countplot(data=df, x='type')
plt.title("Movies vs TV Shows Distribution")
plt.show()"""

#STEP 3: Genre Distribution Analysis
# Split genres
"""df['listed_in'] = df['listed_in'].str.split(',')

# Explode rows
genre_df = df.explode('listed_in')

# Clean spaces
genre_df['listed_in'] = genre_df['listed_in'].str.strip()

# Top genres
top_genres = genre_df['listed_in'].value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Netflix Genres")
plt.xticks(rotation=45)
plt.show() """

#STEP 4: Country-Level Contribution
"""df['country'] = df['country'].str.split(',')
country_df = df.explode('country')
country_df['country'] = country_df['country'].str.strip()

top_countries = country_df['country'].value_counts().head(10)

plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xticks(rotation=45)
plt.show() """

#STEP 5: Feature Engineering
"""def categorize_duration(duration):
    if 'min' in str(duration):
        mins = int(duration.split()[0])
        if mins < 90:
            return "Short Movie"
        elif mins < 120:
            return "Medium Movie"
        else:
            return "Long Movie"
    elif 'Season' in str(duration):
        seasons = int(duration.split()[0])
        if seasons == 1:
            return "Single Season Show"
        else:
            return "Multi Season Show"
    return "Unknown"

df['content_length_category'] = df['duration'].apply(categorize_duration)

df['is_original'] = df['title'].str.contains("Netflix", case=False, na=False)"""


#STEP 6: Rating Distribution Analysis
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index)
plt.title("Content Rating Distribution")
plt.show()