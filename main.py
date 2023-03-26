import os

import streamlit as st
from io import StringIO

import openbabel
from openbabel import pybel


st.title("hello openbabel")
st.text("pybel informats")
st.text(len(pybel.informats))
st.text("pybel outformats")
st.text(len(pybel.outformats))

import subprocess

uploaded_file = st.file_uploader("datファイルをアップロードしてください")

st.text(uploaded_file)
if uploaded_file is not None:
    file_name = os.path.splitext(uploaded_file.name)[0]
    st.text(file_name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # calc_file = st.write(bytes_data)
    with open("test.dat", mode='w') as f:
        f.write(stringio.read())

if st.button('計算開始'):
    file_path = "test.dat"
    # mopacの後にスペースを1つ開ける。
    result = subprocess.run('mopac ' + file_path, shell=True)
    st.text(result)

result_file = file_name + ".arc"
if result_file is not None:
    if st.button('ファイルの読み取り'):
        with open("test.arc", mode='r') as f:
            lines = f.readlines()
            for line in lines:
                st.text(line)




