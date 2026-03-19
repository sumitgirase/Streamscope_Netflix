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
st.markdown("### 📊 Data Analysis Project")  """

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
            st.dataframe(recommendations[['title','type','release_year']].head(10))