import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the Excel file
file_path = 'F:\school/JBR BATCH 2023-2024.xlsx'  
data = pd.read_excel(file_path)

# Set the correct headers
data.columns = data.iloc[1]
data = data.drop([0, 1])
data = data.reset_index(drop=True)

st.title('JBR Public School Batch 2023-2024 Data Analysis')

# Gender Distribution
st.subheader('Gender Distribution')
fig, ax = plt.subplots()
sb.countplot(x='Gender', data=data, ax=ax)
ax.set_title('Gender Distribution')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
st.pyplot(fig)

# Social Category Distribution
st.subheader('Social Category Distribution')
fig, ax = plt.subplots()
sb.countplot(x='Social Category', data=data, ax=ax)
ax.set_title('Social Category Distribution')
ax.set_xlabel('Social Category')
ax.set_ylabel('Count')
st.pyplot(fig)

# BPL Beneficiary Status
st.subheader('BPL Beneficiary Status')
fig, ax = plt.subplots()
bpl_status = data['BPL beneficiary'].value_counts()
ax.pie(bpl_status, labels=bpl_status.index, autopct='%1.1f%%', startangle=140)
ax.set_title('BPL Beneficiary Status')
st.pyplot(fig)

# AADHAAR Validation Status
st.subheader('AADHAAR Validation Status')
fig, ax = plt.subplots()
sb.countplot(x='AADHAAR Validation Status', data=data, ax=ax)
ax.set_title('AADHAAR Validation Status')
ax.set_xlabel('Validation Status')
ax.set_ylabel('Count')
st.pyplot(fig)
