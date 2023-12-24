import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ["#89CFF0", "#FF69B4", "#FFD700", "#7B68EE", "#FF4500",
          "#9370DB", "#32CD32", "#8A2BE2", "#FF6347", "#20B2AA",
          "#FF69B4", "#00CED1", "#FF7F50", "#7FFF00", "#DA70D6"]

df = pd.read_csv("Thyroid_Diff.csv")

st.title("Feature Distribution Visualization")

st.subheader("Data Features")

st.data_editor(df,width=5000,height=200)

feature = st.selectbox(
    "Select feature to plot distribution",
    ('Age', 'Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response'),index=None)

if not feature:
    st.info("Please select feature to plot")
    st.stop()

if feature  == 'Age':

    fig, ax = plt.subplots(figsize = (10, 5),dpi=500)

    ax.hist(df['Age'], bins = 25, edgecolor = 'black', alpha = 0.7, color = 'skyblue', density = True)

    df['Age'].plot(kind = 'kde', color = 'red', ax = ax)

    ax.set_xlabel('Age')
    ax.set_ylabel('Count / Density')
    ax.set_title('Age Distribution Histogram with Density Curve')
    ax.legend(['Density Curve', 'Histogram'])
    st.pyplot(fig)

else :

    fig, ax = plt.subplots(figsize=(8, 6))

# Plot your data
    ax = df[feature].value_counts().plot(kind='bar', color=colors, rot = 90 if feature == "Response" or "Physical Examination" else 0)
    ax.set_xticklabels(df[feature].value_counts().index)

    # Annotate the bars
    for p in ax.patches:
        ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
        ax.tick_params(axis='both', labelsize=15)

    # Set labels and title
    plt.xlabel(str(feature), weight="bold", color="#D71313", fontsize=14, labelpad=20)
    plt.ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)


    # Show the plot in Streamlit
    st.pyplot(fig)
