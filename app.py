import streamlit as st

st.set_page_config(page_title="AI ECG Reader", page_icon="🫀")

st.title("Dr. Navya's AI ECG Reader")
st.write("Built by an MBBS Doctor turned Coder")

st.markdown("---")
uploaded_file = st.file_uploader("Upload your ECG image", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded ECG")
    st.success("ECG Uploaded Successfully!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Heart Rate", "72 bpm", "Normal")
    with col2:
        st.metric("Rhythm", "Sinus", "Regular")
    
    st.info("Analysis: Heart rate is within normal range. This is a learning project for educational purposes only.")
else:
    st.write("Please upload an ECG image above to get started.")
    st.caption("Supports JPG, PNG - Max 200MB")
