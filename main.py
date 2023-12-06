import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# page Configuration:
st.set_page_config(page_title="Tips Daschboard",
                   page_icon=None,
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Tips Daschboard")
st.write("")
# loading data:
df = pd.read_csv("tips.csv")
df.drop_duplicates()

# sidebar:
st.sidebar.header("Tips Daschboard")
st.sidebar.image("tips.png")
st.sidebar.write("This Daschboard is about the tips Dataset from Kaggle.")
st.sidebar.write("")
st.sidebar.write("Filer the Data:")
cat_filter = st.sidebar.selectbox("Categorical Filter: ", [None,"sex", "smoker", "day", "time"])
num_filter = st.sidebar.selectbox("numerical Filter: ", [None,"total_bill", "tip"])
row_filter = st.sidebar.selectbox("Row Filter: ", [None,"sex", "smoker", "day", "time"])
col_filter = st.sidebar.selectbox("Colums Filter: ", [None,"sex", "smoker", "day", "time"])

st.sidebar.write("")
st.sidebar.markdown("Make with :heart_eyes: by [Ahmad](https://github.com/Ahmad1993Aj)")

# Body:
### columns a
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max. total Bill", df["total_bill"].max())
a2.metric("Max. total Tips", df["tip"].max())
a3.metric("Min. total Bill", df["total_bill"].min())
a4.metric("Min.total Tips", df["tip"] .min())

# plot:

st.subheader("Total Bill vs Tips")
fig = px.scatter(data_frame=df,
                 x="total_bill",
                 y="tip",
                 color=cat_filter,
                 size=num_filter,
                 facet_col=col_filter,
                 facet_row=row_filter)

st.plotly_chart(fig, use_container_width=True)

c1, c2, c3 = st.columns((4,3,3))
with c1:
    st.text("Sex vs Total Bills")
    fig = px.bar(data_frame=df,
                 x="sex",
                 y="total_bill",
                 color=cat_filter,
                 )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.text("Smoker/non-Smoker vs Total Bills")
    fig = px.pie(data_frame=df,
                 names="smoker",
                 values="tip",
                 color=cat_filter,
                 hole=0.3
                 )
    st.plotly_chart(fig, use_container_width=True)
with c3:
    st.text("Days vs Tips")
    fig = px.pie(data_frame=df,
                 names="day",
                 values="tip",
                 color=cat_filter,
                 hole=0.3
                 )
    st.plotly_chart(fig, use_container_width=True)