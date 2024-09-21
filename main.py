import streamlit as st

st.title("welcome to the solution")
st.header("Index")
st.subheader("About")
st.markdown("We are providing a complete solution for your business")
st.code("def index(item);""\n"
        "prodect = iteam" "\n"
        """return "product": product""")

# To how the excel sheet

import pandas as pd

# dataset = pd.read_excel(r"Data Source Gap Analysis.xlsx")
# st.dataframe(dataset)

st.header("Products")

# Create a Form

Name = st.text_input("Enter you name")
Location = st.text_input("Enter your location")
Number = st.text_input("Enter your Number")
Priority = st.selectbox("Enter your Priority to get solution:",(1,2,3,4,5))

# to get the data by button and show it again
button = st.button("Submit")
if button:
        st.markdown(f"""
                Name :{Name}
                Location :{Location}
                Number: {Number}
                Priority: {Priority}""")
