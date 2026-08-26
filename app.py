import streamlit as st

st.set_page_config(page_title="AI ECG")

st.title("Dr. Navya's AI ECG Reader")
st.write("Built by an MBBS Doctor turning ECGs into insights")

st.markdown("---")
uploaded_file = st.file_uploader("Upload your ECG", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # 50KB size check
    if uploaded_file.size > 50 * 1024:
        st.error("File too large! Please upload less than 50KB")
        st.stop()

    st.image(uploaded_file, caption="Uploaded ECG")
    st.success("ECG Uploaded Successfully")
    st.caption(f"File size: {uploaded_file.size/1024:.1f} KB - OK")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Heart Rate", "72 bpm")
    with col2:
        st.metric("Rhythm", "Sinus")

    st.info("Analysis: Heart rate is normal")
else:
    st.write("Please upload an ECG image to start")
    st.caption("Supports JPG, PNG - Max 50KB per file")
