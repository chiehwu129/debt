
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(layout="wide")
st.title("Debt to Salary Calculator")
image = Image.open('UNC_Charlotte_Primary_Horiz_Logo.png')
st.sidebar.image(image)
st.sidebar.header('Enter Value')
with st.sidebar:
    with st.form(key= 'my_form'):
        under = st.number_input('Undergraduate Debt', min_value = 0, step = None)

        tuition = st.number_input('Tuition & Fees Per Semester', min_value = 0, step = None)    
 
        living = st.number_input('Living Expense Per Semester', min_value = 0, step = None)

        length = st.selectbox('Number of Semesters', (1,2,3,4,5,6,7,8,9,10))
   
        salary = st.number_input('Expected Salary', min_value = 0, step = None)
    
        repayment = st.selectbox('Repayment Plan*', ('Standard', 'Extended'))
        calculate_but = st.form_submit_button(label='Calculate')
    
st.sidebar.info('*Repayment Plan is the number of months for loan repayment:  \nStandard = 120 Months  \nExtended = 300 Months')
debt = under + ((tuition + living)* length)
spm = salary/12
salary_p10 = salary + 10000
salary_m10 = salary - 10000

if repayment == 'Standard':
    repayment = 120
else:
    repayment = 300

if spm == 0:
    ratio = 0
else:
    ratio = (debt/repayment)/spm

if spm == 0:
    ratio_p10 = 0
else:
    ratio_p10 = (debt/repayment)/(salary_p10/12)
if spm == 0:
    ratio_m10 = 0
else:
    ratio_m10 = (debt/repayment)/(salary_m10/12)
if salary == 0:
        salary_p10 = 0
if salary == 0:
        salary_m10 = 0
Col1, Col2, Col3 = st.columns(3)

with Col1:
    st.subheader('Debt')
    st.write(f'${debt:,}')
    
with Col2:
    st.subheader('Expected Salary')
    st.write(f'${salary:,}')
    st.subheader("+$10,000")
    st.write(f'${salary_p10:,}')
    st.subheader("-$10,000")
    st.write(f'${salary_m10:,}')
with Col3:
    st.subheader('Debt to Salary Ratio*')
    st.write("{:.1%}".format(ratio))
    st.subheader('+$10,000')
    st.write("{:.1%}".format(ratio_p10))
    st.subheader('-$10,000')
    st.write("{:.1%}".format(ratio_m10))
desc = st.container()
with desc:
    st.markdown("***Debt to Salary Ratio Interpretation**")
    st.write('≤10%: Debt is low and will not impair the value of the degree.   \n11%~15%: Debt is high but still within the recommended threshold.  \n15%~20%: Debt is above the recomended threshold but still manageable.  \n≥20%: Debt is high and beyond the debt to salary ratio threshold. Taking on such high debt can diminish the value of a DPT degree.')
    
