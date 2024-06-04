import streamlit as st
import pandas as pd


def get_data():
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/103ztYxOweNu5qL0zXwpAEbQ2zhtd5CacOzHaF5lEP5g/export?gid=0&format=csv",
                     encoding='unicode_escape')
    return df  



def main():
    st.header("Knowledge Hub CS230 🧠")
    st.write("test")

    df = get_data()

    st.dataframe(df)

    st.video("https://www.youtube.com/watch?v=H-WXUXJ6b14")

    with st.sidebar:
        st.write("test")
        st.selectbox(label="Subject", options=df.Subject.unique())

if __name__ == "__main__":
    main()