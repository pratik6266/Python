import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
  st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")
if add_masala: 
  st.text("Masala added")

base = st.radio("Select the base of chai", ["Milk", "Water"])
st.text(f"Your base is: {base}")

flavour = st.selectbox("Select the flavour: ", ["Adrak", "Kesar", "Tulshi"])
st.text(f"Your flavour: {flavour}")

sugar = st.slider("Sugar Spoons", 0, 5, 2)
st.text(f"Your sugar: {sugar}")

cups = st.number_input("No of cups", min_value=1, max_value=10, step=1)
st.text(f"Your cups: {cups}")

name = st.text_input("Enter Your Name: ")
if name:
  st.write(f"Your name: {name}")

dob = st.date_input("Select Your DOB")
st.write(f"Your DOB: {dob}")