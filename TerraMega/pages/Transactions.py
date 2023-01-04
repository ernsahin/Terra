import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from shroomdk import ShroomDK
import json
from pandas import json_normalize
st.set_page_config(layout="wide")
# header = st.container()
dataset= st.container()
# features= st.container()
modelTraining= st.container()
api='53012785-d2f9-49a0-81a9-cdd22bc8a330'
sdk = ShroomDK(api)
st.markdown("<h1 style='text-align: center; color: Green;'> Transactions OF Terra </h1>", unsafe_allow_html=True)
 

# records1=query_result_set1.records
# # records_data1=pd.DataFrame.from_dict(records1)
# Use json_normalize() to convert JSON to DataFrame
a= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6a84def6-f5a8-4bc9-8c7f-4f224e9c5232/data/latest',orient='records')
records_data1=pd.DataFrame.from_records(a)
b= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest',orient='records')
records_data2=pd.DataFrame.from_records(b)
c= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c7fb32ec-b972-4c27-a97b-6fffa3466646/data/latest',orient='records')
records_data3=pd.DataFrame.from_records(c)



# # records_data1=pd.DataFrame.to_json
# records2=query_result_set2.records 
# records_data2=pd.DataFrame.from_dict(records2) 




 


    
 


col3=st.container()

with col3 :
    st.title('Weekly Transactions and Their Status')
    chart_daily = px.area(
        records_data2,
        x='DATE',
        y='TXS',
        color='STATUS'
    )
    st.plotly_chart(chart_daily,use_container_width=True)

col4=st.container()
    
with col4 :
      st.title("Average Fees In Luna")
      chart_daily = px.line(    
            records_data2,
            x='DATE',
            y='AVG_FEE_LUNA'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 

col6=st.container()




    
with col6 :
      st.title("Average GAS Spent")
      chart_daily = px.area(    
            records_data2,
            x='DATE',
            y='AVG_GAS_PRICE'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 




col7,col8 = st.columns([1,1])

with col7 :
    st.title('Average Time Between Blocks')
    chart_daily = px.area(
        records_data3,
        x='DATE',
        y='AVG_TIME_BLOCKS' 
    )
    st.plotly_chart(chart_daily,use_container_width=True)
 
    
with col8 :
      st.title("Max Time Between Blocks")
      chart_daily = px.line(    
            records_data3,
            x='DATE',
            y='MAX_TIME_BLOCKS'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 

 


