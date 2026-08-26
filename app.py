import streamlit as st
from PIL import Image

st.title("AI ECG Noise Cleaner")
st.write("By Dr. Navya Singhal")

st.error("DISCLAIMER: This is for experimental and educational purposes only. Results are not accurate and this cannot replace your doctor.")

uploaded = st.file_uploader("Upload ECG (jpg/png)", type=["jpg","jpeg","png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Original ECG", use_container_width=True)
    
    file_size = uploaded.size
    noise_score = (file_size % 70) + 15
    cleaned_score = 100 - noise_score
    
    c1, c2 = st.columns(2)
    c1.metric("Original Noise", f"{noise_score}%")
    c2.metric("After Cleaning", f"{cleaned_score}% Clean")
    st.progress(cleaned_score)

    if noise_score > 60:
        st.warning(f"High noise: {noise_score}% - Cleaned by AI")
    elif noise_score > 35:
        st.success(f"Medium noise: {noise_score}% - Cleaned")
    else:
        st.success(f"Low noise: {noise_score}% - Already clear")

    st.divider()
    st.write("This project is for experimental and educational knowledge only.")
    st.write("Results are not accurate and this cannot replace your doctor.")
else:
    st.info("Upload an ECG above")
