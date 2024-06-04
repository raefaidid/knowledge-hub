import streamlit as st
import pandas as pd
from Main_Page import get_data


SUBJECT_NAME = "Calculus 1"
CHAPTER_1 = "Functions, Limit and Continuity"


# def get_data():
#     df = pd.read_csv(
#         "https://docs.google.com/spreadsheets/d/103ztYxOweNu5qL0zXwpAEbQ2zhtd5CacOzHaF5lEP5g/export?gid=0&format=csv",
#         encoding="unicode_escape",
#     )
#     return df


def chapter_1(subchapter:str) ->str:

    if subchapter == "Limits":
        with st.expander("Watch videos"):
            st.video("https://www.youtube.com/watch?v=H-WXUXJ6b14")
            st.video("https://www.youtube.com/watch?v=TeYK7z27RXA")
            st.video("https://www.youtube.com/watch?v=_3mChjYvc00")
            st.video("https://www.youtube.com/watch?v=sda7QUfuVls")

    if subchapter == "Continuity":
        with st.expander("Watch videos"):
            st.video("https://www.youtube.com/watch?v=YhoyAhUosmw")
            st.video("https://www.youtube.com/watch?v=1pt4mb7qMGU")
            st.video("https://www.youtube.com/watch?v=a8k8GK4-OmQ")


def main():

    df = get_data()

    st.title(f"{SUBJECT_NAME}")
    st.write("test")

    with st.sidebar:
        st.write("test")
        chapter_selection = st.selectbox(
            label="Chapters",
            options=df.loc[df["Subject"] == SUBJECT_NAME].Chapter.unique(),
        )
        subchapter_selection = st.selectbox(
            label="Subchapters",
            options=df.loc[(df["Subject"] == SUBJECT_NAME) & (df["Chapter"] == chapter_selection)].Subchapter.unique(),
        )

    if chapter_selection == CHAPTER_1:
        chapter_1(subchapter_selection)


if __name__ == "__main__":
    main()
