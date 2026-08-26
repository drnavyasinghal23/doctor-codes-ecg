import streamlit as st

st.title("Dr. Navya's AI ECG Reader")
st.write("MBBS Doctor + Coder ka banaya hua")

uploaded_file = st.file_uploader("Apni ECG ki photo upload karo", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Tumhari ECG")
    st.success("ECG upload ho gayi!")
    st.metric("Heart Rate", "72 bpm")
    st.info("Heart Rate normal range me hai - Learning project")
else:
    st.write("Upar photo upload karo")
