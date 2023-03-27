import os

import streamlit as st
from io import StringIO

import openbabel
from openbabel import pybel

## openbabelのテスト
st.title("hello openbabel")
st.text("pybel informats")
st.text(len(pybel.informats))
st.text("pybel outformats")
st.text(len(pybel.outformats))

# mopacファイルのアップロードテスト
import subprocess
result_file = None
uploaded_file = st.file_uploader("datファイルをアップロードしてください")

# アップロードファイルを書き込むテスト
if uploaded_file is not None:
    file_name = os.path.splitext(uploaded_file.name)[0]
    result_file = file_name + ".arc"
    st.text(file_name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # calc_file = st.write(bytes_data)
    with open("test.dat", mode='w') as f:
        f.write(stringio.read())

    # アップロードしたファイルをmopacで計算するテスト
    if st.button('計算開始'):
        file_path = "test.dat"
        # mopacの後にスペースを1つ開ける。
        result = subprocess.run('mopac ' + file_path, shell=True)
        st.text(result)

    # mopacの計算結果のファイルを表示させるテスト
    if result_file is not None:
        if st.button('ファイルの読み取り'):
            with open("test.arc", mode='r') as f:
                lines = f.readlines()
                for line in lines:
                    st.text(line)




