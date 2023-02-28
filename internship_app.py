import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt

st.header('Data Statistics of medical costs and insurance')

df=pd.read_csv('insurance.csv')
st.dataframe(df)

sns.countplot(x='smoker',data=df,hue='sex')
sns.set(style='darkgrid')
plt.title('smokers vs non smokers count')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


st.title('age vs charges')
chart = alt.Chart(df).mark_line().encode(
    x='age',
    y='charges'
)
st.altair_chart(chart, use_container_width=True)


st.title('regions')
data = df['region'].value_counts()
fig, ax = plt.subplots()
ax.pie(data.values, labels=data.index, autopct='%1.1f%%')
ax.set_title('Pie Chart')
st.pyplot(fig)