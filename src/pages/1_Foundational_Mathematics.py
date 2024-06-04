import streamlit as st
import pandas as pd
from Main_Page import get_data


SUBJECT_NAME = "Foundational Mathematics"
CHAPTER_1 = "Functions"
CHAPTER_4 = "System of Equations and Inequalities"


# def get_data():
#     df = pd.read_csv(
#         "https://docs.google.com/spreadsheets/d/103ztYxOweNu5qL0zXwpAEbQ2zhtd5CacOzHaF5lEP5g/export?gid=0&format=csv",
#         encoding="unicode_escape",
#     )
#     return df


def chapter_4(subchapter:str) ->str:

    st.title(f"{CHAPTER_4}")
    st.header(f"1. System of linear equations")
    st.subheader(f"Solving simultaneous equations with two variables for linear equation")
    st.markdown("""
                We can use either the :orange-background[substitution method] or
                the :orange-background[elimination method] to solve simultaneous equations with 2 variables
                """)
    with st.expander("Substitution video"):
        st.video("https://www.youtube.com/watch?v=Q1L8bUDvzXw")
        st.caption("*substitution method")

    with st.expander("Watch video"):
        st.video("https://www.youtube.com/watch?v=HL2fDIOMLJ0")
        st.caption("*elimination method")

    st.divider()

    st.header(f"2. System of non-linear equations")
    st.subheader(f"Solving simultaneous equations with two variables: One linear equation and one non-linear equation")
    st.divider()

    st.header(f"3. System of inequalities")
    st.subheader(f"Definition")
    st.subheader(f"Inequalities of 2 variables")
    st.subheader(f"Graphing techniques")


def main():

    df = get_data()


    with st.sidebar:
        chapter_selection = st.selectbox(
            label="Chapters",
            options=df.loc[df["Subject"] == SUBJECT_NAME].Chapter.unique(),
        )
        subchapter_selection = st.selectbox(
            label="Subchapters",
            options=df.loc[(df["Subject"] == SUBJECT_NAME) & (df["Chapter"] == chapter_selection)].Subchapter.unique(),
        )

    if chapter_selection == CHAPTER_4:
        chapter_4(subchapter_selection)


if __name__ == "__main__":
    main()
