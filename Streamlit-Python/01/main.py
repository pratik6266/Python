import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your favourite of chai")

chai = st.selectbox("Your favourite chai: ", ["Masala Chai", "Lemon Chai", "Adrak Chai"])
st.write(f"Your choice {chai}. Excellent Choice")

st.success("Your chai has been brewed")