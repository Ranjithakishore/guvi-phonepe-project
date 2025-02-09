import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector as sql
import plotly.express as px
import requests
import json


# Dataframe Creation

#sql connection
mydb = sql.connect(host="127.0.0.1",
                    user="root",
                    password="root",
                    database="phonepe_data",
                    port="3306")
cursor = mydb.cursor()

#aggre_insurance_df
cursor.execute("SELECT * FROM aggregated_insurance")
table1=cursor.fetchall()

Aggre_insurance=pd.DataFrame(table1,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#aggre_transaction_df
cursor.execute("SELECT * FROM aggregated_transaction")
table2=cursor.fetchall()

Aggre_transaction=pd.DataFrame(table2,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))


#aggre_user_df
cursor.execute("SELECT * FROM aggregated_user")
table3=cursor.fetchall()

Aggre_user=pd.DataFrame(table3,columns=("States","Years","Quarter","Brands","Transaction_count","Percentage"))


#map_insurance_df
cursor.execute("SELECT * FROM map_insurance")
table4=cursor.fetchall()

Map_insurance=pd.DataFrame(table4,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))


#map_transaction_df
cursor.execute("SELECT * FROM map_transaction")
table5=cursor.fetchall()

Map_transaction=pd.DataFrame(table5,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))


#map_user_df
cursor.execute("SELECT * FROM map_user")
table6=cursor.fetchall()

Map_user=pd.DataFrame(table6,columns=("States","Years","Quarter","Districts","RegisteredUsers","AppOpens"))


#top_insurance_df
cursor.execute("SELECT * FROM top_insurance")
table7=cursor.fetchall()

top_insurance=pd.DataFrame(table7,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))


#top_transaction_df
cursor.execute("SELECT * FROM top_transaction")
table8=cursor.fetchall()

top_transaction=pd.DataFrame(table8,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))


#top_user_df
cursor.execute("SELECT * FROM top_user")
table9=cursor.fetchall()

top_user=pd.DataFrame(table9,columns=("States","Years","Quarter","Pincodes","RegisteredUsers"))



def Transaction_amount_count_Y(df,year):

    tacy=df[df["Years"]==year]
    tacy.reset_index(drop=True, inplace=True)

    tacyg= tacy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar (tacyg, x="States", y = "Transaction_amount", title=f"{year} TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.BuGn_r, height = 650, width = 600)
        st.plotly_chart(fig_amount)

    with col2: 
        fig_count = px.bar (tacyg, x="States", y = "Transaction_count", title=f"{year} TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Darkmint_r, height = 650, width = 600)
        st.plotly_chart(fig_count)

    col1,col2 = st.columns(2)
    with col1:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])
        states_name.sort()

        fig_india_1=px.choropleth(tacyg, geojson=data1, locations="States", featureidkey="properties.ST_NM", color="Transaction_amount",color_continuous_scale="Rainbow",
                                    range_color=(tacyg["Transaction_amount"].min(),tacyg["Transaction_amount"].max()),
                                    hover_name="States", title=f"{year} TRANSACTION AMOUNT", fitbounds="locations",
                                    height=650, width=600)     
        
        fig_india_1.update_geos(visible= False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2=px.choropleth(tacyg, geojson=data1, locations="States", featureidkey="properties.ST_NM", color="Transaction_count",color_continuous_scale="Rainbow",
                                    range_color=(tacyg["Transaction_count"].min(),tacyg["Transaction_count"].max()),
                                    hover_name="States", title=f"{year} TRANSACTION COUNT", fitbounds="locations",
                                    height=650, width=600)     
        
        fig_india_2.update_geos(visible= False)
        st.plotly_chart(fig_india_2)  

    return tacy              

def Transaction_amount_count_Y_Q (df,quarter):
    tacy=df[df["Quarter"]==quarter]
    tacy.reset_index(drop=True, inplace=True)

    tacyg= tacy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar (tacyg, x="States", y = "Transaction_amount", title=f"{tacy['Years'].unique()} YEAR {quarter} QUARTER TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.BuGn_r,height=650, width=600)
        st.plotly_chart(fig_amount)
    with col2:
        fig_count = px.bar (tacyg, x="States", y = "Transaction_count", title=f"{tacy['Years'].unique()} YEAR {quarter} QUARTER TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Darkmint_r,height=650, width=600)
        st.plotly_chart(fig_count)

    col1,col2 = st.columns(2)
    with col1:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])
        states_name.sort()

        fig_india_1=px.choropleth(tacyg, geojson=data1, locations="States", featureidkey="properties.ST_NM",
                                color="Transaction_amount",color_continuous_scale="Rainbow",
                                range_color=(tacyg["Transaction_amount"].min(),tacyg["Transaction_amount"].max()),
                                hover_name="States", title=f"{tacy['Years'].unique()} YEAR {quarter} TRANSACTION AMOUNT", fitbounds="locations",
                                height=650, width=600)     
        
        fig_india_1.update_geos(visible= False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2=px.choropleth(tacyg, geojson=data1, locations="States", featureidkey="properties.ST_NM", 
                                color="Transaction_count",color_continuous_scale="Rainbow",
                                range_color=(tacyg["Transaction_count"].min(),tacyg["Transaction_count"].max()),
                                hover_name="States", title=f"{tacy['Years'].unique()} YEAR {quarter} TRANSACTION COUNT", fitbounds="locations",
                                height=650, width=600)     
        
        fig_india_2.update_geos(visible= False)
        st.plotly_chart(fig_india_2)
    
    return tacy

def Aggre_tran_transaction_type(df,states):

    tacy=df[df["States"]==states]
    tacy.reset_index(drop=True, inplace=True)

    tacyg= tacy.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        fig_pie_1=px.pie (data_frame=tacyg, names= "Transaction_type", values="Transaction_amount",
                        width=600, title=f"{states.upper()} TRANSACTION AMOUNT")

        st.plotly_chart(fig_pie_1)

    with col2:
        fig_pie_2=px.pie (data_frame=tacyg, names= "Transaction_type", values="Transaction_count",
                        width=600, title=f"{states.upper()} TRANSACTION COUNT")

        st.plotly_chart(fig_pie_2)

#Aggre_user analysis 1
def Aggre_user_plot_1(df,year):
    aguy= df[df["Years"]== year]
    aguy.reset_index(drop= True, inplace= True)
    aguyg=aguy.groupby("Brands")[["Transaction_count"]].sum()
    aguyg.reset_index(inplace=True)

    fig_bar_1=px.bar(aguyg, x="Brands", y= "Transaction_count", title=f"{year} BRANDS AND TRANSACTION COUNT",
                    width= 800, color_discrete_sequence=px.colors.sequential.Purples_r, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aguy

#Aggre_user analysis 2
def Aggre_user_plot_2(df, quarter):
    aguyq= df[df["Quarter"]== quarter]
    aguyq.reset_index(drop= True, inplace= True)
    aguyqg=aguyq.groupby("Brands")[["Transaction_count"]].sum()
    aguyqg.reset_index(inplace=True)

    fig_bar_1=px.bar(aguyqg, x="Brands", y= "Transaction_count", title= f"{quarter} QUARTER, BRANDS AND TRANSACTION COUNT",
                    width= 800, color_discrete_sequence=px.colors.sequential.Purples_r, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aguyq

#Aggre_user analysis 3
def Aggre_user_plot_3(df, state):
    auyqs=df[df["States"] == state]
    auyqs.reset_index(drop= True, inplace= True)

    fig_line_1=px.line(auyqs, x = "Brands", y="Transaction_count", hover_data="Percentage",
                    title= f"{state.upper()} BRANDS, TRANSACTION COUNT, PERCENTAGE", width=1000, markers=True)

    st.plotly_chart(fig_line_1)

#Map_insurance_districts
def Map_insur_Districts(df,states):

    tacy=df[df["States"]==states]
    tacy.reset_index(drop=True, inplace=True)

    tacyg= tacy.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_bar_1=px.bar(tacyg, x= "Transaction_amount", y= "Districts", orientation= "h",height= 600,
                        title= f"{states.upper()} DISTRICTS AND TRANSACTION AMOUNT",
                        color_discrete_sequence=px.colors.sequential.Purples_r, hover_name="Districts")

        st.plotly_chart(fig_bar_1)
    with col2:
        fig_bar_2=px.bar(tacyg, x= "Transaction_count", y= "Districts", orientation= "h",height= 600,
                        title= f"{states.upper()} DISTRICTS AND TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Purples_r, hover_name="Districts")

        st.plotly_chart(fig_bar_2)

    return tacy

#map_user_plot_1
def map_user_plot_1(df,year):
    muy= df[df["Years"]== year]
    muy.reset_index(drop= True, inplace= True)
    muyg=muy.groupby("States")[["RegisteredUsers","AppOpens"]].sum()
    muyg.reset_index(inplace=True)

    fig_bar_1=px.line(muyg, x="States", y= ["RegisteredUsers","AppOpens"], title=f"{year} REGISTEREDUSERS AND APPOPENS",
                    width= 1000,height=800,color_discrete_map={"RegisteredUsers": "purple",
                    "AppOpens": "green"},markers=True)
    st.plotly_chart(fig_bar_1)

    return muy

#map_user_plot_2
def map_user_plot_2(df,quarter):
    muyq= df[df["Quarter"]== quarter]
    muyq.reset_index(drop= True, inplace= True)
    muyqg=muyq.groupby("States")[["RegisteredUsers","AppOpens"]].sum()
    muyqg.reset_index(inplace=True)

    fig_bar_1=px.line(muyqg, x="States", y= ["RegisteredUsers","AppOpens"], title=f"{df["Years"].min()} [{quarter}] QUARTER - REGISTEREDUSERS AND APPOPENS",
                    width= 1000,height=800,color_discrete_map={"RegisteredUsers": "red",
                    "AppOpens": "blue"},markers=True)
    st.plotly_chart(fig_bar_1)

    return muyq

#map_user_plot_3
def map_user_plot_3(df,states):   
    muyqs= df[df["States"]==states]
    muyqs.reset_index(drop= True, inplace= True)

    col1,col2 = st.columns(2)
    with col1:
        fig_map_user_bar_1= px.bar(muyqs, x="RegisteredUsers", y= "Districts", orientation="h", title= "REGISTERED USERS",
                                height=800,color_discrete_sequence= px.colors.sequential.Burg_r)

        st.plotly_chart(fig_map_user_bar_1)
    
    with col2:
        fig_map_user_bar_2= px.bar(muyqs, x="AppOpens", y= "Districts", orientation="h", title= "APPOPENS",
                                height=800,color_discrete_sequence= px.colors.sequential.Blues_r)

        st.plotly_chart(fig_map_user_bar_2)


# top_insurance_plot1
def Top_inurance_plot_1(df,state):
    tiy= df[df["States"]==state]
    tiy.reset_index(drop= True, inplace= True)

    col1,col2 = st.columns(2)
    with col1:
        fig_top_insur_bar_1= px.bar(tiy, x="Quarter", y= "Transaction_amount", hover_data="Pincodes", title= "TRANSACTION AMOUNT",
                                    height=800,color_discrete_sequence= px.colors.sequential.Greens_r)

        st.plotly_chart(fig_top_insur_bar_1)

    with col2:
        fig_top_insur_bar_2= px.bar(tiy, x="Quarter", y= "Transaction_count", hover_data="Pincodes", title= "TRANSACTION COUNT",
                                    height=800,color_discrete_sequence= px.colors.sequential.Turbo_r)

        st.plotly_chart(fig_top_insur_bar_2)

# top_user_plot_1
def top_user_plot_1(df,year):
    tuy= df[df["Years"]== year]
    tuy.reset_index(drop= True, inplace= True)

    tuyg=pd.DataFrame(tuy.groupby(["States","Quarter"])["RegisteredUsers"].sum())
    tuyg.reset_index(inplace=True)

    fig_top_user_bar_1= px.bar(tuyg, x="States", y= "RegisteredUsers", color="Quarter",title= f"{year} REGISTERED USERS",
                                    width=1000,height=800,color_discrete_sequence= px.colors.sequential.Rainbow_r)

    st.plotly_chart(fig_top_user_bar_1)

    return tuy

# top_user_plot_2
def top_user_plot_2(df, state):
    tuys= df[df["States"]== state]
    tuys.reset_index(drop= True, inplace= True)

    fig_top_plot_2= px.bar(tuys, x="Quarter",y="RegisteredUsers", title="REGISTERED USERS, PINCODES, QUARTER",
                        width=1000,height=800, color="RegisteredUsers", hover_data= "Pincodes",
                        color_continuous_scale= px.colors.sequential.Cividis_r)

    st.plotly_chart(fig_top_plot_2)


# top_chart_transaction_amount
def top_chart_transaction_amount(table_name):
    mydb = sql.connect(host="127.0.0.1",
                        user="root",
                        password="root",
                        database="phonepe_data",
                        port="3306")
    cursor = mydb.cursor()

    #plot1
    query1= f'''SELECT states, SUM(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_amount DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1=cursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1, columns=("States","Transaction_amount"))

    col1,col2= st.columns(2)
    with col1:
        fig_amount1= px.bar (df_1, x="States", y = "Transaction_amount", title=f"TOP 10 OF TRANSACTION AMOUNT",
                                color_discrete_sequence=px.colors.sequential.Darkmint,height=650, width=650)
        st.plotly_chart(fig_amount1) 

    #plot2
    query2= f'''SELECT states, SUM(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_amount ASC
                LIMIT 10;'''

    cursor.execute(query2)
    table_2=cursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2, columns=("States","Transaction_amount"))

    with col2:
        fig_amount2 = px.bar (df_2, x="States", y = "Transaction_amount", title=f"LAST 10 OF TRANSACTION AMOUNT",
                                color_discrete_sequence=px.colors.sequential.Magenta_r,height=650, width=650)
        st.plotly_chart(fig_amount2) 

    #plot3
    query3= f'''SELECT states, AVG(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_amount ASC; '''

    cursor.execute(query3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3, columns=("States","Transaction_amount"))

    fig_amount3= px.bar (df_3, x="Transaction_amount", y = "States", title=f"AVERAGE OF TRANSACTION AMOUNT",orientation = "h",
                            color_discrete_sequence=px.colors.sequential.OrRd_r,height=800, width=800)
    st.plotly_chart(fig_amount3) 

# top_chart_transaction_count
def top_chart_transaction_count(table_name):
    mydb = sql.connect(host="127.0.0.1",
                        user="root",
                        password="root",
                        database="phonepe_data",
                        port="3306")
    cursor = mydb.cursor()

    #plot1
    query1= f'''SELECT states, SUM(Transaction_count) AS Transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_count DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1=cursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1, columns=("States","Transaction_count"))

    col1,col2= st.columns(2)
    with col1:
        fig_amount1= px.bar (df_1, x="States", y = "Transaction_count", title=f"TOP 10 OF TRANSACTION COUNT",
                                color_discrete_sequence=px.colors.sequential.Peach,height=650, width=650)
        st.plotly_chart(fig_amount1) 

    #plot2
    query2= f'''SELECT states, SUM(Transaction_count) AS Transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_count ASC
                LIMIT 10;'''

    cursor.execute(query2)
    table_2=cursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2, columns=("States","Transaction_count"))

    with col2:
        fig_amount2 = px.bar (df_2, x="States", y = "Transaction_count", title=f"LAST 10 OF TRANSACTION COUNT",
                                color_discrete_sequence=px.colors.sequential.Rainbow_r,height=650, width=650)
        st.plotly_chart(fig_amount2) 

    #plot3
    query3= f'''SELECT states, AVG(Transaction_count) AS Transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY Transaction_count ASC; '''

    cursor.execute(query3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3, columns=("States","Transaction_count"))

    fig_amount3= px.bar (df_3, x="Transaction_count", y = "States", title=f"AVERAGE OF TRANSACTION COUNT",orientation = "h",
                            color_discrete_sequence=px.colors.sequential.Blues_r,height=800, width=800)
    st.plotly_chart(fig_amount3) 


# top_chart_registered_user
def top_chart_registered_user(table_name, state):
    mydb = sql.connect(host="127.0.0.1",
                        user="root",
                        password="root",
                        database="phonepe_data",
                        port="3306")
    cursor = mydb.cursor()

    #plot1
    query1= f'''SELECT districts, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1=cursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1, columns=("districts","RegisteredUsers"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount1= px.bar (df_1, x="districts", y = "RegisteredUsers", title=f"TOP 10 OF REGISTERED USER", hover_name="districts",
                                color_discrete_sequence=px.colors.sequential.Oranges_r,height=600, width=600)
        st.plotly_chart(fig_amount1) 

    #plot2
    query2= f'''SELECT districts, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers 
                LIMIT 10;'''

    cursor.execute(query2)
    table_2=cursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2, columns=("districts","RegisteredUsers"))

    with col2:
        fig_amount2 = px.bar (df_2, x="districts", y = "RegisteredUsers", title=f"LAST 10 OF REGISTERED USER",hover_name="districts",
                                color_discrete_sequence=px.colors.sequential.Pinkyl_r,height=600, width=600)
        st.plotly_chart(fig_amount2) 

    #plot3
    query3= f'''SELECT districts, AVG(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers ASC;'''

    cursor.execute(query3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3, columns=("districts","RegisteredUsers"))

    fig_amount3= px.bar (df_3, x="RegisteredUsers", y = "districts", title=f"AVERAGE OF REGISTERED USER",hover_name="districts",orientation = "h",
                            color_discrete_sequence=px.colors.sequential.Mint_r,height=600, width=600)
    st.plotly_chart(fig_amount3) 

#top_chart_AppOpens
def top_chart_AppOpens(table_name, state):
    mydb = sql.connect(host="127.0.0.1",
                        user="root",
                        password="root",
                        database="phonepe_data",
                        port="3306")
    cursor = mydb.cursor()

    #plot1
    query1= f'''SELECT districts, SUM(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY AppOpens DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1=cursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1, columns=("districts","AppOpens"))

    col1,col2=st.columns(2)
    with col1:
        fig_amount1= px.bar (df_1, x="districts", y = "AppOpens", title=f"TOP 10 OF APPOPENS", hover_name="districts",
                                color_discrete_sequence=px.colors.sequential.BuGn_r,height=600, width=600)
        st.plotly_chart(fig_amount1) 

    #plot2
    query2= f'''SELECT districts, SUM(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY AppOpens 
                LIMIT 10;'''

    cursor.execute(query2)
    table_2=cursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2, columns=("districts","AppOpens"))

    with col2:
        fig_amount2 = px.bar (df_2, x="districts", y = "AppOpens", title=f"LAST 10 OF APPOPENS",hover_name="districts",
                                color_discrete_sequence=px.colors.sequential.Magenta_r,height=600, width=600)
        st.plotly_chart(fig_amount2) 

    #plot3
    query3= f'''SELECT districts, AVG(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY AppOpens ASC;'''

    cursor.execute(query3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3, columns=("districts","AppOpens"))

    fig_amount3= px.bar (df_3, x="AppOpens", y = "districts", title=f"AVERAGE OF APPOPENS",hover_name="districts",orientation = "h",
                            color_discrete_sequence=px.colors.sequential.Bluyl_r,height=800, width=1000)
    st.plotly_chart(fig_amount3) 

# top_chart_registered_users
def top_chart_registered_users(table_name):
    mydb = sql.connect(host="127.0.0.1",
                        user="root",
                        password="root",
                        database="phonepe_data",
                        port="3306")
    cursor = mydb.cursor()

    #plot1
    query1= f'''SELECT states, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name} 
                GROUP BY states
                ORDER BY RegisteredUsers DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1=cursor.fetchall()
    mydb.commit()

    df_1=pd.DataFrame(table_1, columns=("States","RegisteredUsers"))

    col1,col2=st.columns(2)
    with col1:
        fig_amount1= px.bar (df_1, x="States", y = "RegisteredUsers", title=f"TOP 10 OF REGISTERED USERS",hover_name="States",
                                color_discrete_sequence=px.colors.sequential.BuGn_r,height=600, width=600)
        st.plotly_chart(fig_amount1) 

    #plot2
    query2= f'''SELECT states, SUM(RegisteredUsers) AS RegisteredUsers
            FROM {table_name} 
            GROUP BY states
            ORDER BY RegisteredUsers
            LIMIT 10;'''

    cursor.execute(query2)
    table_2=cursor.fetchall()
    mydb.commit()

    df_2=pd.DataFrame(table_2, columns=("States","RegisteredUsers"))

    with col2:
        fig_amount2 = px.bar (df_2, x="States", y = "RegisteredUsers", title=f"LAST 10 OF REGISTERED USERS",hover_name="States",
                                color_discrete_sequence=px.colors.sequential.Blues_r,height=600, width=600)
        st.plotly_chart(fig_amount2)

    #plot3
    query3= f'''SELECT states, AVG(RegisteredUsers) AS RegisteredUsers
                FROM {table_name} 
                GROUP BY states
                ORDER BY RegisteredUsers DESC;
                '''

    cursor.execute(query3)
    table_3=cursor.fetchall()
    mydb.commit()

    df_3=pd.DataFrame(table_3, columns=("States","RegisteredUsers"))

    fig_amount3= px.bar (df_3, x="RegisteredUsers", y = "States", title=f"AVERAGE OF REGISTERED USERS",orientation = "h",
                        hover_name="States",color_discrete_sequence=px.colors.sequential.RdBu_r,height=600, width=600)
    st.plotly_chart(fig_amount3) 


#streamli part

st.set_page_config(layout="wide")
st.title('PHONEPE DATA VISUALIZATION AND EXPLORATION')


with st.sidebar:
    select= option_menu("Main Menu",["HOME", "DATA EXPLORATION", "TOP CHARTS"])

if select == "HOME":
    col1,col2=st.columns(2)
    with col1:
        st.image("https://www.retail4growth.com/public/thumbs/news/2020/04/4960/Phonepe_Thumnail_440_851.jpg")
    with col2:
        st.video("https://youtu.be/aXnNA4mv1dU?t=14")
elif select == "DATA EXPLORATION":
    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:
         
        method = st.radio("select the method",["Insurance Analysis","Transaction Analysis","User Analysis"])

        if method == "Insurance Analysis":

            col1,col2 = st.columns(2)
            with col1:
                years=st.slider("Select the year_ai",Aggre_insurance["Years"].min(),Aggre_insurance["Years"].max(),Aggre_insurance["Years"].min())
            tac_Y=Transaction_amount_count_Y(Aggre_insurance, years)

            col1,col2 = st.columns(2)
            with col1:
                if tac_Y["Quarter"].min() < tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_ai",
                        min_value=tac_Y["Quarter"].min(),
                        max_value=tac_Y["Quarter"].max(),
                        value=tac_Y["Quarter"].max())
                else:
                    quarter = tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
                
            Transaction_amount_count_Y_Q (tac_Y,quarter)

        elif method == "Transaction Analysis":
            
            col1,col2 = st.columns(2)
            with col1:
                
                years=st.slider("Select the year_at",Aggre_transaction["Years"].min(),Aggre_transaction["Years"].max(),Aggre_transaction["Years"].min())
            Aggre_tran_tac_Y = Transaction_amount_count_Y(Aggre_transaction,years) 

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_at",Aggre_tran_tac_Y["States"].unique())

            Aggre_tran_transaction_type(Aggre_tran_tac_Y,states)

            col1,col2 = st.columns(2)
            with col1:
                if Aggre_tran_tac_Y["Quarter"].min() < Aggre_tran_tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_at",
                        min_value=Aggre_tran_tac_Y["Quarter"].min(),
                        max_value=Aggre_tran_tac_Y["Quarter"].max(),
                        value=Aggre_tran_tac_Y["Quarter"].max())
                else:
                    quarter = Aggre_tran_tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
                
            Aggre_tran_tac_Y_Q= Transaction_amount_count_Y_Q (Aggre_tran_tac_Y,quarter)
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_att",Aggre_tran_tac_Y_Q["States"].unique())

            Aggre_tran_transaction_type(Aggre_tran_tac_Y_Q,states)


        elif method == "User Analysis":
            
            col1,col2 = st.columns(2)
            with col1:
                
                year=st.slider("Select the year_au",Aggre_user["Years"].min(),Aggre_user["Years"].max(),Aggre_user["Years"].min())
            Aggre_user_Y = Aggre_user_plot_1(Aggre_user,year)

            col1,col2 = st.columns(2)
            with col1:
                if Aggre_user_Y["Quarter"].min() < Aggre_user_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_au",
                        min_value=Aggre_user_Y["Quarter"].min(),
                        max_value=Aggre_user_Y["Quarter"].max(),
                        value=Aggre_user_Y["Quarter"].max())
                else:
                    quarter = Aggre_user_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
                
            Aggre_user_Y_Q= Aggre_user_plot_2(Aggre_user_Y,quarter)
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_au",Aggre_user_Y_Q["States"].unique())

            Aggre_user_Y_Q_S=Aggre_user_plot_3(Aggre_user_Y_Q,states)

    with tab2:
         
        method2 = st.radio("select the method",["Map Insurance","Map Transaction","Map User"])

        if method2 == "Map Insurance":
            
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_mi",Map_insurance["Years"].min(),Map_insurance["Years"].max(),Map_insurance["Years"].min())
            Map_insur_tac_Y = Transaction_amount_count_Y(Map_insurance,year)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_mi",Map_insur_tac_Y["States"].unique())

            Map_insur_Districts(Map_insur_tac_Y,states)

            col1,col2 = st.columns(2)
            with col1:
                if Map_insur_tac_Y["Quarter"].min() < Map_insur_tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_mi",
                        min_value=Map_insur_tac_Y["Quarter"].min(),
                        max_value=Map_insur_tac_Y["Quarter"].max(),
                        value=Map_insur_tac_Y["Quarter"].max())
                else:
                    quarter = Map_insur_tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
                
            Map_insur_tac_Y_Q=Transaction_amount_count_Y_Q(Map_insur_tac_Y,quarter)
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_mi",Map_insur_tac_Y_Q["States"].unique())

            Map_insur_Districts(Map_insur_tac_Y_Q,states)

        elif method2 == "Map Transaction":
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_mt",Map_transaction["Years"].min(),Map_transaction["Years"].max(),Map_transaction["Years"].min())
            Map_tran_tac_Y = Transaction_amount_count_Y(Map_transaction,year)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_mt",Map_tran_tac_Y["States"].unique())

            Map_insur_Districts(Map_tran_tac_Y,states)

            col1,col2 = st.columns(2)
            with col1:
                if Map_tran_tac_Y["Quarter"].min() < Map_tran_tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_mt",
                        min_value=Map_tran_tac_Y["Quarter"].min(),
                        max_value=Map_tran_tac_Y["Quarter"].max(),
                        value=Map_tran_tac_Y["Quarter"].max())
                else:
                    quarter = Map_tran_tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
                
            Map_tran_tac_Y_Q=Transaction_amount_count_Y_Q(Map_tran_tac_Y,quarter)
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_mtt",Map_tran_tac_Y_Q["States"].unique())

            Map_insur_Districts(Map_tran_tac_Y_Q,states)


        elif method2 == "Map User":
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_mu",Map_user["Years"].min(),Map_user["Years"].max(),Map_user["Years"].min())
            map_user_Y = map_user_plot_1(Map_user,year)

            col1,col2 = st.columns(2)
            with col1:
                if map_user_Y["Quarter"].min() < map_user_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_mu",
                        min_value=map_user_Y["Quarter"].min(),
                        max_value=map_user_Y["Quarter"].max(),
                        value=map_user_Y["Quarter"].max())
                else:
                    quarter = map_user_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
            
            map_user_Y_Q= map_user_plot_2(map_user_Y,quarter)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_mu",map_user_Y_Q["States"].unique())

            map_user_plot_3(map_user_Y_Q,states)

    with tab3:
         
        method3 = st.radio("select the method_",["Top Insurance","Top Transaction","Top User"])

        if method3 == "Top Insurance":
            
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_ti",top_insurance["Years"].min(),top_insurance["Years"].max(),top_insurance["Years"].min())
            top_insur_tac_Y = Transaction_amount_count_Y(top_insurance,year) 
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_ti",top_insur_tac_Y["States"].unique())

            Top_inurance_plot_1(top_insur_tac_Y,states)

            col1,col2 = st.columns(2)
            with col1:
                if top_insur_tac_Y["Quarter"].min() < top_insur_tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_ti",
                        min_value=top_insur_tac_Y["Quarter"].min(),
                        max_value=top_insur_tac_Y["Quarter"].max(),
                        value=top_insur_tac_Y["Quarter"].max())
                else:
                    quarter = top_insur_tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")

            top_insur_tac_Y_Q = Transaction_amount_count_Y_Q(top_insur_tac_Y,3)

        elif method3 == "Top Transaction":
             
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_tt",top_transaction["Years"].min(),top_transaction["Years"].max(),top_transaction["Years"].min())
            top_tran_tac_Y = Transaction_amount_count_Y(top_transaction,year)  
            
            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_tt",top_tran_tac_Y["States"].unique())

            Top_inurance_plot_1(top_tran_tac_Y,states)

            col1,col2 = st.columns(2)
            with col1:
                if top_tran_tac_Y["Quarter"].min() < top_tran_tac_Y["Quarter"].max():
                    quarter = st.slider("Select the Quarter_tt",
                        min_value=top_tran_tac_Y["Quarter"].min(),
                        max_value=top_tran_tac_Y["Quarter"].max(),
                        value=top_tran_tac_Y["Quarter"].max())
                else:
                    quarter = top_tran_tac_Y["Quarter"].max()
                    st.write(f"No of Quarter available : {quarter}")
            
            top_tran_tac_Y_Q = Transaction_amount_count_Y_Q(top_tran_tac_Y,3)


        elif method3 == "Top User":
            col1,col2 = st.columns(2)
            with col1:
                year=st.slider("Select the year_tu",top_user["Years"].min(),top_user["Years"].max(),top_user["Years"].min())
            top_user_Y = top_user_plot_1(top_user,year)  

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_tu",top_user_Y["States"].unique())

            top_user_plot_2(top_user_Y,states)

elif select == "TOP CHARTS":
    question= st.selectbox("Select the Question",["1. Transaction Amount and Count of Aggregated Insurance",
                                                    "2. Transaction Amount and Count of Map Insurance",
                                                    "3. Transaction Amount and Count of Top Insurance",
                                                    "4. Transaction Amount and Count of Aggregated Transaction",
                                                    "5. Transaction Amount and Count of Map Transaction",
                                                    "6. Transaction Amount and Count of Top Transaction",
                                                    "7. Transaction Count of Aggregated User",
                                                    "8. Registered users of Map User",
                                                    "9. App opens of Map User",
                                                    "10. Registered users of Top User" 
                                                    ])
    
    if question == "1. Transaction Amount and Count of Aggregated Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.aggregated_insurance")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.aggregated_insurance")

    elif question == "2. Transaction Amount and Count of Map Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.map_insurance")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.map_insurance")

    elif question == "3. Transaction Amount and Count of Top Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.top_insurance")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.top_insurance")

    elif question == "4. Transaction Amount and Count of Aggregated Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.aggregated_transaction")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.aggregated_transaction")

    elif question == "5. Transaction Amount and Count of Map Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.map_transaction")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.map_transaction")

    elif question == "6. Transaction Amount and Count of Top Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("phonepe_data.top_transaction")
        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.top_transaction")

    elif question == "7. Transaction Count of Aggregated User":

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("phonepe_data.aggregated_user")

    elif question == "8. Registered users of Map User":
        states= st.selectbox("Select the state", Map_user["States"].unique())
        
        st.subheader("REGISTERED USER")
        top_chart_registered_user("phonepe_data.map_user",states) 

    elif question == "9. App opens of Map User":
        states= st.selectbox("Select the state", Map_user["States"].unique())
        
        st.subheader("APPOPENS")
        top_chart_AppOpens("phonepe_data.map_user",states)
    
    elif question == "10. Registered users of Top User":
        
        st.subheader("REGISTERED USERS")
        top_chart_registered_users("phonepe_data.top_user")