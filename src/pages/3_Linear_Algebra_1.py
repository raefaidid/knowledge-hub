import streamlit as st
import pandas as pd
from Main_Page import get_data


SUBJECT_NAME = "Linear Algebra 1"
CHAPTER_1 = "Matrices"
CHAPTER_2 = "System of Linear Equations"
CHAPTER_3 = "Determinants"
CHAPTER_4 = "Vector Spaces"
CHAPTER_5 = "Linear Transformations"


# def get_data():
#     df = pd.read_csv(
#         "https://docs.google.com/spreadsheets/d/103ztYxOweNu5qL0zXwpAEbQ2zhtd5CacOzHaF5lEP5g/export?gid=0&format=csv",
#         encoding="unicode_escape",
#     )
#     return df


def chapter_3(subchapter:str) ->str:

    st.title(f"{CHAPTER_3}")
    with st.popover("Learning Objectives:"):
        st.markdown("""
                    - evaluate determinants by using formula, cofactor expansion and elementary operation
                    - apply properties of determinant and equivalence conditions for a square matrix
                    - find the inverse of a matrix by using the adjoint formula
                    - use Cramer’s Rule to solve systems of linear equations
                    - form the cofactor matrix and find the adjoint of a matrix
                    """)
    st.header(f"1. Evaluating Determinants")
    # st.subheader(f"There four methods for evaluation")
    with st.expander("Formula"):
        video_file = open('./src/media/LESSON 3.1.1_EVALUATE DETERMINANT USING FORMULA.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with st.expander("Cofactor Expansion"):
        video_file = open('./src/media/LESSON 3.1.2_EVALUATE DETERMINANT USING COFACTOR EXPANSION.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    
    with st.expander("Determinants of certain matrices"):
        video_file = open('./src/media/LESSON 3.1.3_DETERMINANTS OF CERTAIN SPECIAL MATRIX.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with st.expander("Elementary Operations"):
        video_file = open('./src/media/LESSON 3.1.4_EVALUATE DETERMINANT USING ELEMENTARY OPERATIONS.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with st.expander("Properties of determinants"):
        video_file = open('./src/media/MAT423_Lesson 3.2_Properties of Determinant.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    st.divider()

    st.header(f"2. Application of determinants")

    with st.expander("Adjoint Method"):
        video_file = open('./src/media/MAT423_LESSON 3.3_ADJOINT METHOD.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
    with st.expander("Cramer's Rule"):
        video_file = open("./src/media/MAT423_LESSON 3.4_CRAMER'S RULE.mp4", 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)




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

    if chapter_selection == CHAPTER_3:
        chapter_3(subchapter_selection)


if __name__ == "__main__":
    main()
