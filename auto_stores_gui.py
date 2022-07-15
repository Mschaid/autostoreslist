import os
import glob
import shutil
import streamlit as st


# Functions for creating directories and managment


def create_new_dir(file_path, new_dir_ext):
    """ creates new directory from file path and extension"""
    new_directory = os.path.join(file_path, new_dir_ext)
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
        print('directory created')
    else:
        print('directroy already exists')


def list_subdirs(directory):
    """ given directory, returns list of all sub dirs as full path"""
    return [os.path.join(directory, file) for file in os.listdir(directory)]


# User input prompts

path_to_files = st.text_input("Enter path to photometry folder")
master_stores_list = st.text_input("Enter path to master stores list")
file_remove_ext = st.text_input(
    "Enter file name to remove (Enter 'None' to bypass)")


# streamlit waits for submit button to run

with st.form("my_form"):

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:

        print(path_to_files)
        print(master_stores_list)

        sub_dirs = list_subdirs(path_to_files)

        for s in sub_dirs:
            basename = os.path.basename(s)
            create_new_dir(s, f"{basename}_output_1")
        output_dirs = glob.glob(path_to_files + "\**\*output_*")

        for dir in output_dirs:
            shutil.copy(master_stores_list, dir)

        files_to_remove = glob.glob(
            path_to_files + f"\**\{file_remove_ext}*")

        for f in files_to_remove:
            if f is None:
                pass
            elif os.path.exists(f):
                os.remove(f)
                print("file removed")
            else:
                print("file not found")
