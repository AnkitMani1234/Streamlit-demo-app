import streamlit as st


st.title("Welcome to Web App")

st.header("Machine Learning")

st.subheader("Linear regression")

st.info("Information Details of a user")

st.warning("Come on time or else you will be marked absent")

st.error("Wrong Password")

st.success("Congrats you have got A grade")

st.write("Employee name")

st.write(range(50))

st.markdown("Streamlit")
st.markdown("# Streamlit")
st.markdown('## Streamlit ')
st.markdown(":moon:")

st.text("Learners")

st.caption("Caption is here")

# to display a mathematical expression

st.latex(r''' a+b x^2+c''' )

# Widget

st.checkbox("Login")

st.button("Click")

#Radio

st.radio("Pick your gender",["Male","Female","Other"])

st.selectbox("Pick your course",["ML","cloud","cyber security"])

#MultiSelect

st.multiselect("Choose your dept",["Content","Sales","Marketing"])

# select_Slider()
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

# Slider

st.slider("Enter your number",0,100)

#number_input

st.number_input("Pick a number",0,100)

#text_input

st.text_input("Enter your email address")

#date input

st.date_input("Opening Ceremony")

#time_input

st.time_input("Hey what is time ")

st.text_area("Enter your address")

st.file_uploader("upload your file/folder")

st.color_picker("Color")

st.progress(90)

# ballon
st.balloons()

#sidebar
st.sidebar.title("Welcome to Streamlit")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])
st.sidebar.button("Submit")

#Data Visulization
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)