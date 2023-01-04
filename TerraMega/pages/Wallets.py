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
st.markdown("<h1 style='text-align: center; color: Green;'> Wallets OF Terra </h1>", unsafe_allow_html=True)
 

# records1=query_result_set1.records
# # records_data1=pd.DataFrame.from_dict(records1)
# Use json_normalize() to convert JSON to DataFrame
a= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6a84def6-f5a8-4bc9-8c7f-4f224e9c5232/data/latest',orient='records')
records_data1=pd.DataFrame.from_records(a)
b= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest',orient='records')
records_data2=pd.DataFrame.from_records(b)



# # records_data1=pd.DataFrame.to_json
# records2=query_result_set2.records 
# records_data2=pd.DataFrame.from_dict(records2) 




new1,tx1=st.columns([1,1])
with new1 :
    st.title('New Users Onboarded On Terra')
    chart_daily = px.bar(
        records_data1,
        x='DATE',
        y='NEW_USERS'
    )
    st.plotly_chart(chart_daily,use_container_width=True)


    
with tx1 :
      st.title("Active Walelts OF Terra")
      chart_daily = px.area(
            records_data1,
            x='DATE',
            y='ACTIVE_WALLETS'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 



col1,col2=st.columns([1,1])

with col1 :
    st.title('Average New Users')
    chart_daily = px.bar(
        records_data1,
        x='DATE',
        y='AVERAGE_NEW_USERS'
    )
    st.plotly_chart(chart_daily,use_container_width=True)


    
with col2 :
      st.title("Cumulative New Users")
      chart_daily = px.line(
            records_data1,
            x='DATE',
            y='CUMULATIVE_NEW_USERS'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 


col3,col4=st.columns([1,1])

with col3 :
    st.title('Weekly Transactions and Their Status')
    chart_daily = px.area(
        records_data2,
        x='DATE',
        y='TXS',
        color='STATUS'
    )
    st.plotly_chart(chart_daily,use_container_width=True)


    
with col4 :
      st.title("Average Fees In Luna")
      chart_daily = px.line(    
            records_data2,
            x='DATE',
            y='AVG_FEE_LUNA'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 

col5,col6=st.columns([1,1])

with col5 :
    st.title('Weekly Unique Users')
    chart_daily = px.bar(
        records_data2,
        x='DATE',
        y='UNIQUE_USERS' 
    )
    st.plotly_chart(chart_daily,use_container_width=True)


    
with col6 :
      st.title("Average GAS Price")
      chart_daily = px.area(    
            records_data2,
            x='DATE',
            y='AVG_GAS_PRICE'
        )
      st.plotly_chart(chart_daily,use_container_width=True) 


# plotly= px.line(r
#     records_data1,
#     x='DATE',
#     y='txs'
# )
 
# st.plotly_chart(plotly,theme="streamlit", use_container_width=True)

# daily_txs,fails=st.columns([2,2])
# tps,fees=st.columns([1,1])
# with plotly : 
#     st.title("Plotly Transactions")
#     chart= px.bar(
#         data_transactions,
#         x='week',
#         y='txs'
#     )
# #     st.plotly_chart(chart,theme='streamlit',use_container_width=True)
# daily_txs,fails=st.columns([1,1])

# with fails :
#     st.title('Transactions Succsess  Rate')
#     fail_rate= alt.Chart(data_transactions).mark_area().encode(
#         alt.X('date:T'),
#         alt.Y('volume:Q'),
#         color='marketplace'
#     )
#     st.altair_chart(fail_rate,use_container_width=True)
# # with fees :
# #     st.title('Weekly Average Fees $LUNA')
# #     fee=alt.Chart(data_transactions).mark_line().encode(
# #         alt.X('week:T'),
# #         alt.Y('avg_fee_luna:Q')
# #     )
# #     st.altair_chart(fee,use_container_width=True)
# # with tps:
# #     st.title('Weekly TPS')
# #     tps=alt.Chart(data_transactions).mark_line().encode(
# #         alt.X('week:T'),
# #         alt.Y('avg_tps:Q')
# #     )
# #     #properties(width=800, height=400)
    
# #     st.altair_chart(tps,use_container_width=True)

# # with plotly1 :
# #     st.title('Daily Transactions')
# #     chart_transactions = px.violin(
# #         data_transactions,
# #         x='week',
# #         y='txs'
# #     )
# #     st.plotly_chart(chart_transactions,use_container_width=True)

# # with plotly2 :
# #     st.title('Daily Transactions')
# #     chart_transactions = px.histogram(
# #         data_transactions,
# #         x='week',
# #         y='avg_fee_luna'
# #     )
# #     st.plotly_chart(chart_transactions,use_container_width=True)


# # Parameters can be passed into SQL statements 
# # via native string interpolation
# # my_address = "0x...."
# # sql = f"""
# #      SELECT 
# #      block_timestamp::date as date,
# #      COUNT(*) as txs
# #      FROM   ethereum.core.fact_transactions
# #      WHERE date >= '2022-01-01'
# #      GROUP BY date 
# #      ORDER BY date DESC
     
# # """

# # Run the query against Flipside's query engine 
# # and await the results
# # query_result_set = sdk.query(
# #     sql,
# #     ttl_minutes=60,
# #     cached=True,
# #     timeout_minutes=20,
# #     retry_interval_seconds=1 
# # )
# # records = query_result_set.records
# # eth_txs = f"""
# # SELECT 
# #      block_timestamp::date as date,
# #      COUNT(*) as txs
# #      FROM   ethereum.core.fact_transactions
# #      WHERE date >= '2021-01-01'
# #      GROUP BY date 
# #      ORDER BY date DESC
# #      LIMIT 30
# # """
# eth_records = sdk.query(
#     eth_txs,
#     ttl_minutes=60,
#     cached=True,
#     timeout_minutes=20,
#     retry_interval_seconds=1 
# )
# eth_2=  eth_records.records
# asd,second=st.columns([1,1])

# # Iterate over the results
# with asd : 
#     st.title('Shrooms In API Out')
#     data_shroom=pd.DataFrame.from_dict(records)
#     shro=alt.Chart(data_shroom).mark_bar().encode(   
#         alt.X('date:T'),
#         alt.Y('txs:Q')
#         )
#     st.altair_chart(shro,use_container_width=True)
# with second :
#     st.title('ETH 2021')
#     data=pd.DataFrame.from_dict(eth_2)
#     data2=alt.Chart(data).mark_area().encode(
#         alt.X('date:T'),
#         alt.Y('txs:Q')
#     )
#     st.altair_chart(data2,use_container_width=True)

    
   
    




# with header :
#     st.title('Terra Mega Dashboard')
# df = pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/446958b3-a694-4bb5-98a0-41d556a96c5d/data/latest")
# with dataset : 
#       st.header('Transaction Success Status')
#       df=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest")
#       ye = alt.Chart(df).mark_line().encode(
#       alt.X('DATE_DAY:T',scale=alt.Scale(zero=False)) ,
#       alt.Y('TXS:Q',scale=alt.Scale(zero=False)),
#       alt.StrokeDash('STATUS'),
#       alt.Color('STATUS:N'),
#       alt.OpacityValue(1),
#       tooltip = [
#                alt.Tooltip('DATE_DAY'),
#                alt.Tooltip('TXS'),
#                alt.Tooltip('STATUS')
#               ]
#     )
#       chart= df
#       st.altair_chart(ye,use_container_width=True)
