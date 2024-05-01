import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import plotly as px
import seaborn as sns
import time
import plotly.express as px

col1,col2,col3=st.columns([0.20,0.6,0.20])
with col1:
   st.image("logo1.jpg")

with col2:
 st.title("Welcome to HIV Testing and Services Data")
 
with col3:
   st.image("logo2.jpg", width=120)

st.markdown ("---")
st.subheader("NB:"); st.write("HTS Data current available is Total Tests for 4th Quarter of 2023. For other Quarters i.e. 1st, 2nd and 3rd  and disaggregates please contact Database System Administrator for help. Thank You!")
st.markdown ("---")
col1,col2,col3=st.columns([0.33,33,0.33])

with col1:
  def OCTD():
    OctoberD="01OCT HTS.csv"
    dtf=pd.read_csv(OctoberD)
    return dtf
data1=OCTD()

with col2:
 import pandas as pd
 def NOVD():
   NovemberD="02NOV HTS.csv"
   dtf=pd.read_csv(NovemberD)
   return dtf
data2=NOVD()

with col3:
 import pandas as pd
 def DECD():
   DecemberD="03DEC HTS.csv"
   dtf=pd.read_csv(DecemberD)
   return dtf
data3=DECD() 

import pandas as pd 
def Quarterly():
  df1=pd.read_csv('./01OCT HTS.csv')
  df2=pd.read_csv('./02NOV HTS.csv')
  df3=pd.read_csv('./03DEC HTS.csv')
  Quarterly_HTS=pd.concat([df1,df2,df3],ignore_index=True)
  Quarterly_HTS.to_csv('Quarterly_HTS.csv', index=False)

#Replacing Facility Codes for Reporting Sites with missing codes
  Quarterly_HTS.loc[Quarterly_HTS['Facility']=='Chinaka Health Post', 'Facility Code']='p.zw.100022'
  Quarterly_HTS.loc[Quarterly_HTS['Facility']=='Tsvingwe Clinic', 'Facility Code']='p.zw.100021'

#Dropping Non Reporting Sites
  column_name='Facility Code'
  values_to_drop=['p.zw.100018','p.zw.100014', 'p.zw.100280', 'p.zw.100426', 'p.zw.100435', 'p.zw.101106']
  Quarterly_HTS= Quarterly_HTS[~Quarterly_HTS[column_name].isin(values_to_drop)]

  Quarterly_HTS= Quarterly_HTS.dropna(subset=[column_name])
#Filling Blanks with Zeros
  Quarterly_HTS=Quarterly_HTS.fillna(0)

  Quarterly_HTS.to_csv("Quarterly_HTS.csv",index=False)
  return Quarterly_HTS
data4=Quarterly()


if st.checkbox("Show October Data"):
   st.subheader("October Data")
   st.dataframe(data1)

if st.checkbox("Show November Data"):
   st.subheader("November Data")
   st.dataframe(data2)

if st.checkbox("Show December Data"):
   st.subheader("December Data")
   st.dataframe(data3)

if st.checkbox('Show All Quarter 4 Data'):
   st.header("Quarterly Data")
   st.dataframe(data4)

st.markdown ("---")
st.sidebar.write("**In HTS Module we explore HIV tests that were done within every quarter of the year within Health Facilities in the District!**")

import streamlit as st
import pandas as pd
import numpy as np
st.subheader('Facility Totals')
Quarterly_HTS=pd.read_csv('Quarterly_HTS.csv')

# Summing up Facility Monthly Totals
Organ= "Facility"
Cols_to_total=['Males','Females']
Filter_Quarterly=Quarterly_HTS[Organ].unique()
select_facility=st.selectbox(f'Select a Facility', Filter_Quarterly)
Filtered_Quarterly= Quarterly_HTS[Quarterly_HTS[Organ]== select_facility]
Totals=Filtered_Quarterly[Cols_to_total].sum()

Period="Period"             
Total_Row=pd.DataFrame({Organ:['Totals'],Period:['Oct-Dec 23']})
for column, total in Totals.items():
 Total_Row[column]=total


Filter_Quarterly_Totals=pd.concat([Filtered_Quarterly ,Total_Row], ignore_index=True)
Cols_to_convert=['Males','Females']
Filter_Quarterly_Totals[Cols_to_convert]=Filter_Quarterly_Totals[Cols_to_convert].round(0).astype(int)
st.write(f'Data and Totals for {select_facility}:')
st.table(Filter_Quarterly_Totals)

st.markdown ('---')
#Adding up Facility Quarterly Totals
st.subheader('Facility Quarterly Totals')
Quarterly_HTS_Totals = Quarterly_HTS.groupby('Facility')[['Facility Code','Males','Females']].sum().reset_index()
Quarterly_HTS_Totals

st.markdown ('---')

st.title('Data Visualiser')
#HIV Total Tests for Males
st.subheader('Male Tests')
import streamlit as st
import pandas as pd
import plotly

print(plotly.__version__)
import plotly.express as px
histog= px.bar(Quarterly_HTS, x=Organ, y= "Males", hover_data=Quarterly_HTS)
st.plotly_chart(histog)

st.markdown ('---')

#HIV Total Tests for Females
st.subheader('Female Tests')
import streamlit as st
import pandas as pd
import plotly

print(plotly.__version__)
import plotly.express as px
histo= px.bar(Quarterly_HTS, x=Organ, y= "Females", hover_data=Quarterly_HTS)
st.plotly_chart(histo)

st.markdown ('---')


# Facility Test by Rank
st.header("Most Male tests by Facility")
Facility_with_most_tests=Quarterly_HTS_Totals.groupby('Males').sum()
Facility_with_most_tests

st.markdown ('---')

# Facility Test by Rank
st.header("Most Female tests by Facility")
Facility_with_most_tests=Quarterly_HTS_Totals.groupby('Females').sum()
Facility_with_most_tests

st.markdown ('---')
st.subheader('Facility Grand Totals')
Quarterly_HTS_Totals=pd.DataFrame(Quarterly_HTS_Totals)
Quarterly_HTS_Totals['Total']=Quarterly_HTS_Totals['Males']+Quarterly_HTS_Totals['Females']
st.dataframe(Quarterly_HTS_Totals)

Quarterly_HTS_Totals.to_csv('Quarterly_HTS_Totals.csv', index=False)

Quarterly_HTS_Totals=pd.read_csv('./Quarterly_HTS_Totals.csv')
st.markdown ('---')
st.subheader('Facility rank by most tests done')
Facility_with_most_tests=Quarterly_HTS_Totals.groupby('Total').sum()
Facility_with_most_tests

st.markdown ('---')

# Bar plot of total number of tests per Facility
print(plotly.__version__)
import plotly.express as px
histo= px.bar(Quarterly_HTS_Totals, x="Facility", y= "Total", hover_data=Quarterly_HTS_Totals)
st.plotly_chart(histo)

st.markdown ('---')
st.markdown('**Thank you for visiting our page. Come back soon for more updates, as the page is still under development**')







