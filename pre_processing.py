import os
import json
import pandas as pd
import mysql.connector as sql

#aggre_insurance
path1="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/aggregated/insurance/country/india/state/"

agg_insur_list= os.listdir(path1)
columns1= {"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in agg_insur_list:
    cur_states=path1+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            A=json.load(data)

            for i in A ["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))

aggre_insurance = pd.DataFrame(columns1)
aggre_insurance["States"]=aggre_insurance["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
aggre_insurance["States"]=aggre_insurance["States"].str.replace('-',' ')
aggre_insurance["States"]=aggre_insurance["States"].str.title()
aggre_insurance["States"]=aggre_insurance["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#aggre_transaction 

path2="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_tran_list= os.listdir(path2)

columns2= {"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in agg_tran_list:
    cur_states=path2+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            B=json.load(data)

            for i in B ["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns2["Transaction_type"].append(name)
                columns2["Transaction_count"].append(count)
                columns2["Transaction_amount"].append(amount)
                columns2["States"].append(state)
                columns2["Years"].append(year)
                columns2["Quarter"].append(int(file.strip(".json")))
            
aggre_transaction=pd.DataFrame(columns2)
aggre_transaction["States"]=aggre_transaction["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
aggre_transaction["States"]=aggre_transaction["States"].str.replace('-',' ')
aggre_transaction["States"]=aggre_transaction["States"].str.title()
aggre_transaction["States"]=aggre_transaction["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#aggregated user

path3="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_list= os.listdir(path3)

columns3= {"States":[],"Years":[],"Quarter":[],"Brands":[],"Transaction_count":[],"Percentage":[]}

for state in agg_user_list:
    cur_states=path3+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            C=json.load(data)
            
            try:
                for i in C ["data"]["usersByDevice"]:
                    brand=i["brand"]
                    count=i["count"]
                    percentage=i["percentage"]
                    columns3["Brands"].append(brand)
                    columns3["Transaction_count"].append(count)
                    columns3["Percentage"].append(percentage)
                    columns3["States"].append(state)
                    columns3["Years"].append(year)
                    columns3["Quarter"].append(int(file.strip(".json")))
            
            except:
                pass

aggre_user=pd.DataFrame(columns3)
aggre_user["States"]=aggre_user["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
aggre_user["States"]=aggre_user["States"].str.replace('-',' ')
aggre_user["States"]=aggre_user["States"].str.title()
aggre_user["States"]=aggre_user["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#map_insurance
path4="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/map/insurance/hover/country/india/state/"
map_insur_list= os.listdir(path4)

columns4= {"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_insur_list:
    cur_states=path4+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            D=json.load(data)

            for i in D["data"]["hoverDataList"]:
                    name=i["name"]
                    count=i["metric"][0]["count"]
                    amount=i["metric"][0]["amount"]
                    columns4["Districts"].append(name)
                    columns4["Transaction_count"].append(count)
                    columns4["Transaction_amount"].append(amount)
                    columns4["States"].append(state)
                    columns4["Years"].append(year)
                    columns4["Quarter"].append(int(file.strip(".json")))

map_insurance=pd.DataFrame(columns4)
map_insurance["States"]=map_insurance["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
map_insurance["States"]=map_insurance["States"].str.replace('-',' ')
map_insurance["States"]=map_insurance["States"].str.title()
map_insurance["States"]=map_insurance["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')          

#map_transaction
path5="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_tran_list= os.listdir(path5)

columns5= {"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_tran_list:
    cur_states=path5+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            E=json.load(data)
            

            for i in E["data"]["hoverDataList"]:
                    name=i["name"]
                    count=i["metric"][0]["count"]
                    amount=i["metric"][0]["amount"]
                    columns5["Districts"].append(name)
                    columns5["Transaction_count"].append(count)
                    columns5["Transaction_amount"].append(amount)
                    columns5["States"].append(state)
                    columns5["Years"].append(year)
                    columns5["Quarter"].append(int(file.strip(".json")))

map_transaction=pd.DataFrame(columns5)
map_transaction["States"]=map_transaction["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
map_transaction["States"]=map_transaction["States"].str.replace('-',' ')
map_transaction["States"]=map_transaction["States"].str.title()
map_transaction["States"]=map_transaction["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')           

#map_user

path6="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list= os.listdir(path4)

columns6= {"States":[],"Years":[],"Quarter":[],"Districts":[],"RegisteredUsers":[],"AppOpens":[]}

for state in map_user_list:
    cur_states=path6+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            F=json.load(data)
            

            for i in F["data"]["hoverData"].items():
                district=i[0]
                registeredUsers=i[1]["registeredUsers"]
                appOpens=i[1]["appOpens"]
                columns6["Districts"].append(district)
                columns6["RegisteredUsers"].append(registeredUsers)
                columns6["AppOpens"].append(appOpens)
                columns6["States"].append(state)
                columns6["Years"].append(year)
                columns6["Quarter"].append(int(file.strip(".json")))

map_user=pd.DataFrame(columns6)
map_user["States"]=map_user["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
map_user["States"]=map_user["States"].str.replace('-',' ')
map_user["States"]=map_user["States"].str.title()
map_user["States"]=map_user["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')                

#top_insurance

path7="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/top/insurance/country/india/state/"
top_insur_list=os.listdir(path7)

columns7= {"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for state in top_insur_list:
    cur_states=path7+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")
            G=json.load(data)

            for i in G["data"]["pincodes"]:
                    entityname= i["entityName"]
                    count= i["metric"]["count"]
                    amount= i["metric"]["amount"]
                    columns7["Pincodes"].append(entityname)
                    columns7["Transaction_count"].append(count)
                    columns7["Transaction_amount"].append(amount)
                    columns7["States"].append(state)
                    columns7["Years"].append(year)
                    columns7["Quarter"].append(int(file.strip(".json")))

top_insurance=pd.DataFrame(columns7)
top_insurance["States"]=top_insurance["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
top_insurance["States"]=top_insurance["States"].str.replace('-',' ')
top_insurance["States"]=top_insurance["States"].str.title()
top_insurance["States"]=top_insurance["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')      

#top_transaction

path8="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/top/transaction/country/india/state/"
top_tran_list=os.listdir(path8)

columns8= {"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for state in top_tran_list:
    cur_states=path8+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")
            H=json.load(data)

            for i in H["data"]["pincodes"]:
                    entityname= i["entityName"]
                    count= i["metric"]["count"]
                    amount= i["metric"]["amount"]
                    columns8["Pincodes"].append(entityname)
                    columns8["Transaction_count"].append(count)
                    columns8["Transaction_amount"].append(amount)
                    columns8["States"].append(state)
                    columns8["Years"].append(year)
                    columns8["Quarter"].append(int(file.strip(".json")))

top_transaction=pd.DataFrame(columns8)
top_transaction["States"]=top_transaction["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar') 
top_transaction["States"]=top_transaction["States"].str.replace('-',' ')
top_transaction["States"]=top_transaction["States"].str.title()
top_transaction["States"]=top_transaction["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')      

#top_user

path9="C:/Users/ranji/OneDrive/Desktop/datascience/guvi projects/phonepe/pulse/data/top/user/country/india/state/"

top_user_list= os.listdir(path9)

columns9= {"States":[],"Years":[],"Quarter":[],"Pincodes":[],"RegisteredUsers":[]}

for state in top_user_list:
    cur_states=path9+state+"/"
    agg_year_list=os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_year= cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            I=json.load(data)
            

            for i in I["data"]["pincodes"]:
                entityname=i["name"]
                registeredusers=i["registeredUsers"]
                columns9["Pincodes"].append(entityname)
                columns9["RegisteredUsers"].append(registeredusers)
                columns9["States"].append(state)
                columns9["Years"].append(year)
                columns9["Quarter"].append(int(file.strip(".json")))

top_user=pd.DataFrame(columns9)
top_user["States"]=top_user["States"].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
top_user["States"]=top_user["States"].str.replace('-',' ') 
top_user["States"]=top_user["States"].str.title()
top_user["States"]=top_user["States"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')          

#table creation 

#sql connection
mydb = sql.connect(host="127.0.0.1",
                    user="root",
                    password="root",
                    database="phonepe_data",
                    port="3306")
cursor = mydb.cursor()

#aggregated_insurance_table
create_query_1='''CREATE TABLE if not exists aggregated_insurance(States varchar(255),
                                                    Years int,
                                                    Quarter int,
                                                    Transaction_type varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount bigint)'''
cursor.execute(create_query_1)
mydb.commit()

insert_query_1='''INSERT INTO aggregated_insurance(States, Years, Quarter, 
                                                    Transaction_type, 
                                                    Transaction_count,
                                                    Transaction_amount)
                                                    
                                                    values(%s,%s,%s,%s,%s,%s)'''
data=aggre_insurance.values.tolist()
cursor.executemany(insert_query_1,data)
mydb.commit()

#aggregated_transaction_table
create_query_2='''CREATE TABLE if not exists aggregated_transaction(States varchar(255),
                                                    Years int,
                                                    Quarter int,
                                                    Transaction_type varchar(255),
                                                    Transaction_count bigint,
                                                    Transaction_amount bigint)'''
cursor.execute(create_query_2)
mydb.commit()

insert_query_2='''INSERT INTO aggregated_transaction(States, Years, Quarter, Transaction_type, 
                                                    Transaction_count,
                                                    Transaction_amount)
                                                    
                                                    values(%s,%s,%s,%s,%s,%s)'''
data=aggre_transaction.values.tolist()
cursor.executemany(insert_query_2,data)
mydb.commit()

#aggregated_user_table
create_query_3='''CREATE TABLE if not exists aggregated_user(States varchar(255),
                                                    Years int,
                                                    Quarter int,
                                                    Brands varchar(255),
                                                    Transaction_count bigint,
                                                    Percentage float)'''
cursor.execute(create_query_3)
mydb.commit()

insert_query_3='''INSERT INTO aggregated_user(States, Years, Quarter, Brands, 
                                                Transaction_count,
                                                Percentage)
                                                    
                                                values(%s,%s,%s,%s,%s,%s)'''
data=aggre_user.values.tolist()
cursor.executemany(insert_query_3,data)
mydb.commit()

#map_insurance_table
create_query_4='''CREATE TABLE if not exists map_insurance(States varchar(255),
                                                            Years int,
                                                            Quarter int,
                                                            Districts varchar(255),
                                                            Transaction_count bigint,
                                                            Transaction_amount bigint)'''
cursor.execute(create_query_4)
mydb.commit()

insert_query_4='''INSERT INTO map_insurance(States, Years, Quarter, Districts, 
                                                    Transaction_count,
                                                    Transaction_amount)
                                                    
                                                    values(%s,%s,%s,%s,%s,%s)'''
data=map_insurance.values.tolist()
cursor.executemany(insert_query_4,data)
mydb.commit()

#map_transaction_table
create_query_5='''CREATE TABLE if not exists map_transaction(States varchar(255),
                                                            Years int,
                                                            Quarter int,
                                                            Districts varchar(255),
                                                            Transaction_count bigint,
                                                            Transaction_amount bigint)'''
cursor.execute(create_query_5)
mydb.commit()

insert_query_5='''INSERT INTO map_transaction(States, Years, Quarter, Districts, 
                                                Transaction_count,
                                                Transaction_amount)
                                                
                                                values(%s,%s,%s,%s,%s,%s)'''
data=map_transaction.values.tolist()
cursor.executemany(insert_query_5,data)
mydb.commit()

#map_user_table
create_query_6='''CREATE TABLE if not exists map_user(States varchar(255),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(255),
                                                        RegisteredUsers bigint,
                                                        AppOpens bigint)'''
cursor.execute(create_query_6)
mydb.commit()

insert_query_6='''INSERT INTO map_user(States, Years, Quarter, Districts, 
                                        RegisteredUsers,
                                        AppOpens)
                                        
                                        values(%s,%s,%s,%s,%s,%s)'''
data=map_user.values.tolist()
cursor.executemany(insert_query_6,data)
mydb.commit()

#top_insurance_table
create_query_7='''CREATE TABLE if not exists top_insurance(States varchar(255),
                                                            Years int,
                                                            Quarter int,
                                                            Pincodes int,
                                                            Transaction_count bigint,
                                                            Transaction_amount bigint)'''
cursor.execute(create_query_7)
mydb.commit()

insert_query_7='''INSERT INTO top_insurance(States, Years, Quarter, Pincodes, 
                                            Transaction_count,
                                            Transaction_amount)
                                            
                                            values(%s,%s,%s,%s,%s,%s)'''
data=top_insurance.values.tolist()
cursor.executemany(insert_query_7,data)
mydb.commit()

#top_transaction_table
create_query_8='''CREATE TABLE if not exists top_transaction(States varchar(255),
                                                            Years int,
                                                            Quarter int,
                                                            Pincodes int,
                                                            Transaction_count bigint,
                                                            Transaction_amount bigint)'''
cursor.execute(create_query_8)
mydb.commit()

insert_query_8='''INSERT INTO top_transaction(States, Years, Quarter, Pincodes, 
                                                Transaction_count,
                                                Transaction_amount)
                                                
                                                values(%s,%s,%s,%s,%s,%s)'''
data=top_transaction.values.tolist()
cursor.executemany(insert_query_8,data)
mydb.commit()

#top_user_table
create_query_9='''CREATE TABLE if not exists top_user(States varchar(255),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUsers bigint
                                                        )'''
cursor.execute(create_query_9)
mydb.commit()

insert_query_9='''INSERT INTO top_user(States, Years, Quarter, Pincodes, 
                                        RegisteredUsers)
                                        
                                        values(%s,%s,%s,%s,%s)'''
data=top_user.values.tolist()
cursor.executemany(insert_query_9,data)
mydb.commit()

