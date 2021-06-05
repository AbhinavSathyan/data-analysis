import streamlit as st
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Data Analysis")
st.header('Dataset : titanic.csv')

st.markdown('The data set contain data of people travelled in titanic ship')
st.markdown("[Source of data](https://github.com/awesomedata/awesome-public-datasets)")
data = pd.read_csv('titanic.csv')
head =data.head(10)
st.table(head)
st.balloons()
st.subheader('survived')
sns.countplot(x='Survived',data=data)

st.pyplot()
st.subheader('Gender Ratio')
sns.countplot(x='Sex',data=data)

st.pyplot()
st.subheader('Plot of data')
sns.pairplot(data)
st.pyplot()