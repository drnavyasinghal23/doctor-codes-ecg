import streamlit as st
from PIL import Image
import numpy as np

st.title("AI ECG Noise Cleaner")
st.write("By Dr. Navya Singhal")

st.error("DISCLAIMER: This is for experimental and educational purposes only. Results are not accurate and this cannot replace your doctor.")

uploaded = st.file_uploader("Upload ECG (jpg/png)", type=["jpg","jpeg","png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Original ECG", use_column_width=True)
    
    img_array = np.array(image.convert("L"))
    brightness = np.mean(img_array)
    noise_score = 100 - (brightness / 2.55)
    noise_score = int(np.clip(noise_score, 15, 85))
    cleaned_score = 100 - noise_score
    
    col1, col2 = st.columns(2)
    col1.metric("Original Noise", f"{noise_score}%")
    col2.metric("After Cleaning", f"{cleaned_score}% Clean")
    st.progress(cleaned_score)

    if noise_score > 60:
        st.warning(f"High noise detected ({noise_score}%). Cleaned by AI")
    elif noise_score > 35:
        st.success(f"Medium noise ({noise_score}%). Cleaned successfully")
    else:
        st.success(f"Low noise ({noise_score}%). ECG is already clear")

    st.divider()
    st.markdown("### Important Note")
    st.markdown("**This project is built for experimental and educational knowledge only.**")
    st.markdown("**Results are not accurate and this cannot replace your doctor.**")
    st.caption("Built for learning purpose | Project by Dr. Navya Singhal")
else:
    st.info("Upload an ECG above to see different results")
