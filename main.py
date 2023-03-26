import streamlit as st

import openbabel
from openbabel import pybel


st.title("hello openbabel")
st.text("pybel informats")
st.text(len(pybel.informats))
st.text("pybel outformats")
st.text(len(pybel.outformats))

import subprocess

if st.button('計算開始'):
    file_path = "phenol.dat"
    # mopacの後にスペースを1つ開ける。
    result = subprocess.run('mopac ' + file_path, shell=True)
    st.text(result)

if st.button('ファイルの読み取り'):
    with open('phenol.arc', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            st.text(line)




