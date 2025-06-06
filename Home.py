import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")

content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
st.write(content)
st.subheader("Our Team")

df = pd.read_csv('F:\Company_Website\data.csv', sep=",")

#col1, empty_space, col2, empty_space2, col3 = st.columns([1, 0.5, 1, 0.5, 1])

col1, col2, col3 = st.columns(3)


with col1:
    for index, row in df[0:4].iterrows():

        st.markdown(f"**{row['first name'].title()} {row['last name'].title()}**")
        #or for bold
        # st.subheader(f'{row["first name"].title()} {row['last name'].title()}')
        st.write(row["role"])
        st.image("F:/Company_Website/images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.markdown(f"**{row['first name'].title()} {row['last name'].title()}**")
        st.text(row["role"])
        st.image("F:/Company_Website/images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.markdown(f"**{row['first name'].title()} {row['last name'].title()}**")
        st.text(row["role"])
        st.image("F:/Company_Website/images/" + row["image"])