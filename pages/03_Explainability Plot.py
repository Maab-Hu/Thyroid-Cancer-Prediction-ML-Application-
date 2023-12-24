import streamlit as st

st.title("Explaining the Predictions made by models")

st.image("RF_SHAP.png")

st.subheader("Alligning the model results with medical intuition")

st.write("**1**. We can see that a higher value of **Response** (higher values imply more incomplete response to treatment), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
st.write("**2**. We can see that a higher value of **Risk** (higher values imply patient is more at risk of recurrence), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
st.write("**3**. We can see that a higher value of **N** (higher values imply more advanced N stage , meaning more extensive spread of cancer), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
st.write("**4**. We can see that a higher value of **Age** (higher values mean older patient), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
st.write("**5**. We can see that a higher value of **Smoking** (higher values mean patient smokes), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
st.write("**6**. We can see that a higher value of **Multi Nodular Goiter** (higher values imply more nodules or lumps), result in model outputting **higher** values, closer to 1 , where **1 means cancer will recur**")
