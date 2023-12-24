import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

colors = ["#89CFF0", "#FF69B4", "#FFD700", "#7B68EE", "#FF4500",
          "#9370DB", "#32CD32", "#8A2BE2", "#FF6347", "#20B2AA",
          "#FF69B4", "#00CED1", "#FF7F50", "#7FFF00", "#DA70D6"]

df = pd.read_csv("Thyroid_Diff.csv")

st.title("Feature vs Recurrence Visualization")

feature = st.selectbox(
    "Select feature : ",
    ('Age', 'Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response'),index=None)

if not feature:
    st.info("Please select feature to plot")
    st.stop()

fig, ax = plt.subplots(figsize=(8, 4))

# Plot your data
sns.countplot(x=str(feature), hue='Recurred', data=df, palette='bone')

plt.title('Recurrence Count', fontsize=16, weight='bold')
plt.xlabel(str(feature), fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.legend(title='Recurred', title_fontsize='12', fontsize='10')
plt.xticks(rotation=20)


# Show the plot in Streamlit
st.pyplot(fig)