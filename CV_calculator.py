import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="CV Calculator - Dr. Valeria Mureșan",
    page_icon="🔬",
    layout="centered",
)

# ---- LOGO ----
st.image("logo.png", width=180)

# ---- TITLE ----
st.markdown(
    """
    <h1 style='text-align: center; color: #1A7D86; font-family: sans-serif;'>
        CV Calculator
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---- INPUT SECTION ----
st.markdown(
    """
    <h3 style='color:#1A7D86; font-family: sans-serif;'>
        Enter your data:
    </h3>
    """,
    unsafe_allow_html=True
)

mean = st.number_input("Mean value:", min_value=0.0, format="%.2f")
sd = st.number_input("Standard deviation:", min_value=0.0, format="%.2f")

# ---- RESULT BOX ----
if mean > 0:
    cv = (sd / mean) * 100
    st.markdown(
        f"""
        <div style='background-color:#E5F8F9; 
                    padding:20px; 
                    border-radius:15px; 
                    margin-top:20px;
                    border:1px solid #1A7D86;'>
            <h3 style='color:#1A7D86; font-family:sans-serif;'>
                CV% = {cv:.2f}
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Please enter a mean greater than 0.")

# ---- FOOTER ----
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:#6C7A89; font-family:sans-serif;'>
        © Dr. Valeria Mureșan — Medicina de Laborator
    </p>
    """,
    unsafe_allow_html=True
)
