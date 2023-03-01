import os
import time
import streamlit as st
from api_new import save_results, get_information_from_file



sample_path  =os.path.join("sample")


def main():
    st.markdown("""
    <style>
        body {
            background-color: #FFFFF5;
        }
    </style>
    """, unsafe_allow_html=True)
    st.title("FreeState POC Demo")
    folder_path = st.sidebar.text_input("Folder path:", sample_path)
    files = os.listdir(folder_path)
    selected_files = st.sidebar.selectbox("Select files:", files)
    if not selected_files:
        st.warning("Please select a file.")
        return

    start_button = st.sidebar.button("Start")
    

    if start_button:
        with st.spinner("Running..."):
            print(selected_files)
            result=get_information_from_file(os.path.join(sample_path, selected_files))
            result = save_results(selected_files, result)
        st.write("Result:")
        st.json(result)

if __name__ == "__main__":
    main()
    