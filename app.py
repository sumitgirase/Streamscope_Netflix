"""import streamlit as st
import pandas as pd

st.title("📊 Netflix Data Dashboard")

df = pd.read_csv("netflix_modeled_data.csv")

st.write("Dataset Preview")
st.dataframe(df.head())


#Add Filters
st.sidebar.header("Filter Data")

type_filter = st.sidebar.selectbox("Select Type", df['type'].unique())

filtered_df = df[df['type'] == type_filter]

st.write("Filtered Data")
st.dataframe(filtered_df)

#Step 6 — Add Charts
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("Content Type Distribution")

fig, ax = plt.subplots()
sns.countplot(data=df, x='type', ax=ax)

st.pyplot(fig)

#2. Release Year Trend
st.subheader("Content Release Trend")

fig, ax = plt.subplots()
df['release_year'].value_counts().sort_index().plot(ax=ax)

st.pyplot(fig)

#3. Duration vs Year
st.subheader("Duration vs Release Year")

fig, ax = plt.subplots()
ax.scatter(df['release_year'], df['duration_num'])

st.pyplot(fig)

#Step 7 — Show Model Insights
st.subheader("Model Insights")

st.write("Clusters created to group similar content")
st.write("Classification model predicts Movie vs TV Show")

#Step 8 — Make UI Better
st.sidebar.title("🎬 Netflix Dashboard")
st.markdown("### 📊 Data Analysis Project")  

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🎬 Netflix Data Project")

# Load data
df = pd.read_csv("netflix_modeled_data.csv")

# Create Tabs
tab1, tab2 = st.tabs(["📊 Dashboard", "💡 Recommendation App"])

# ------------------ TAB 1 ------------------
with tab1:
    st.header("📊 Netflix Data Dashboard")

    st.write("Analyze Netflix content trends and insights.")

    # Filter
    type_filter = st.selectbox("Select Content Type", df['type'].unique())

    filtered_df = df[df['type'] == type_filter]

    st.dataframe(filtered_df.head())

    # Chart
    st.subheader("Content Distribution")

    fig, ax = plt.subplots()
    sns.countplot(data=df, x='type', ax=ax)
    st.pyplot(fig)

    # Insight
    st.subheader("📌 Insight")
    st.write("This dashboard helps users understand content trends on Netflix.")


# ------------------ TAB 2 ------------------
with tab2:
    st.header("🎯 Movie Recommendation System")

    movie_list = df['title'].dropna().unique()

    selected_movie = st.selectbox("Choose a Movie", movie_list)

    if st.button("Recommend"):
        movie_data = df[df['title'] == selected_movie]

        if not movie_data.empty:
            movie_type = movie_data.iloc[0]['type']
            movie_year = movie_data.iloc[0]['release_year']

            recommendations = df[
                (df['type'] == movie_type) &
                (df['release_year'].between(movie_year-2, movie_year+2))
            ]

            st.write("Recommended Content:")
            st.dataframe(recommendations[['title','type','release_year']].head(10))"""


#Step 1 — Add Sidebar Filters
import streamlit as st
import pandas as pd

st.title("📊 Netflix Data Dashboard")

df = pd.read_csv("netflix_modeled_data.csv")

st.write("Dataset Preview")
st.dataframe(df.head())
st.sidebar.header("Filter Data")

selected_type = st.sidebar.selectbox(
    "Select Type",
    options=df['type'].unique()
)

selected_year = st.sidebar.slider(
    "Select Year",
    int(df['release_year'].min()),
    int(df['release_year'].max()),
    2020
)

# Apply filter
filtered_df = df[
    (df['type'] == selected_type) &
    (df['release_year'] <= selected_year)
]


#Step 2 — Add KPI Metrics (Looks Professional)
st.title("Netflix Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Content", len(filtered_df))
col2.metric("Movies", len(filtered_df[filtered_df['type'] == 'Movie']))
col3.metric("TV Shows", len(filtered_df[filtered_df['type'] == 'TV Show']))

#Step 3 — Interactive Charts
import matplotlib.pyplot as plt

# Content by Year
year_counts = filtered_df['release_year'].value_counts().sort_index()

st.subheader("Content by Year")
st.line_chart(year_counts)

# Type Distribution
type_counts = filtered_df['type'].value_counts()

st.subheader("Content Type Distribution")
st.bar_chart(type_counts)

#Step 4 — Country Filter (Extra Powerful)
selected_country = st.sidebar.selectbox(
    "Select Country",
    options=df['country'].dropna().unique()
)

filtered_df = filtered_df[
    filtered_df['country'] == selected_country
]

#Step 5 — Improve Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Year Trend")
    st.line_chart(year_counts)

with col2:
    st.subheader("Type Distribution")
    st.bar_chart(type_counts)

#Step 6 — Add Tabs (VERY IMPORTANT FOR JUDGES)
tab1, tab2 = st.tabs(["📊 Dashboard", "🎬 Recommendation"])

with tab1:
    st.write("Dashboard content here")

with tab2:
    st.write("Recommendation system here")