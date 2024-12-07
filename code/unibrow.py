'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file = st.file_uploader("Upload File:", type=["csv", "xlsx", "json"])
if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select Columns to Display", cols, default=cols)
    if st.toggle("Filter Data"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Select Column to Filter", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select Value to Filter", vals)
            df_show = df[df[filter_col]==val][selected_cols]
    else:
        df_show = df[selected_cols]

    st.dataframe(df_show)
    st.dataframe(df_show.describe())