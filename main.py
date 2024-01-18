import streamlit as st
import base64
from service import data_insert, retrieve_data

# To hide the default text by Streamlit Application
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden}
            footer {visibility: hidden}
            header {visibility: hidden} 
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-position : center;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('download.jpg')


def student_details_form():
    st.markdown("<h1 style='text-align: center; position:relative;'> Student Detail Form</h1>", unsafe_allow_html=True)

    # Get user inputs
    Name = st.text_input("First Name:")
    Class = st.text_input("Class:")
    Section = st.selectbox("section:", [" ", "A", "B", "C"])
    Subject = st.selectbox("subject:", [" ", "English", "Tamil", "Maths"])
    Grade = st.text_input("Grade:")

    # Display the submitted details
    st.subheader("Submitted Details:")
    st.write(f"First Name: {Name}")
    st.write(f"Class: {Class}")
    st.write(f"section: {Section}")
    st.write(f"Subject: {Subject}")
    st.write(f"grade: {Grade}")

    # Submit button
    if st.button("Submit"):
        data_insert(Name, Class, Section, Subject, Grade)
        st.success("Details Submitted Successfully!")

    st.title("User Data Retrieval")

    data = retrieve_data()

    # Display the retrieved data in a table
    if data:
        st.write("User Data:")
        st.table(data)
    else:
        st.write("No data available.")


if __name__ == "__main__":
    student_details_form()
