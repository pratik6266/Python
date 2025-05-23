import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
  st.header("Masala Chai")
  st.image("https://images.pexels.com/photos/5946612/pexels-photo-5946612.jpeg?auto=compress&cs=tinysrgb&w=600", width=200)
  vote1 = st.button("Vote Masala Chai")

with col2:
  st.header("Lemon Chai")
  st.image("https://images.pexels.com/photos/792613/pexels-photo-792613.jpeg?auto=compress&cs=tinysrgb&w=600", width=200)
  vote2 = st.button("Vote Lemon Chai")


if vote1:
  st.success("Thanks for voting Masala Chai")
elif vote2:
  st.success("Thanks for voting Lemon Chai")