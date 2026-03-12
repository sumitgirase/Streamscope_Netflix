import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())


#Select useful features like country ,release_year,type
data = df[['type','release_year','rating','duration','country']]
data = data.dropna()

#Step 2 — Convert Duration to Numeric
def extract_duration(x):
    return int(x.split()[0])

data['duration_num'] = data['duration'].apply(extract_duration)


#Step 3 — Encode Categorical Features
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

data['type_encoded'] = le.fit_transform(data['type'])
data['rating_encoded'] = le.fit_transform(data['rating'])
data['country_encoded'] = le.fit_transform(data['country'])



# Step 4 — Prepare Features for Clustering
from sklearn.cluster import KMeans

features = data[['release_year','duration_num','rating_encoded']]

kmeans = KMeans(n_clusters=4, random_state=42)

data['cluster'] = kmeans.fit_predict(features)

print(data[['release_year','duration_num','rating','cluster']].head())


#Step 5 — Visualize Clusters
import matplotlib.pyplot as plt

plt.scatter(data['release_year'], data['duration_num'], c=data['cluster'])
plt.xlabel("Release Year")
plt.ylabel("Duration")
plt.title("Netflix Content Clustering")
plt.show()
print("Clustering completed. Starting model training...")


#Step 6 — Build Classification Model
from sklearn.model_selection import train_test_split

X = data[['release_year','duration_num','rating_encoded']]
y = data['type_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#Step 7 — Train Model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)


#Step 8 — Check Model Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


#Step 9 — Feature Importance (Very Important for Project)
importance = model.feature_importances_

for i,v in enumerate(importance):
    print(X.columns[i], ":", v)

#Step 10 — Save Processed Data
data.to_csv("netflix_modeled_data.csv", index=False)