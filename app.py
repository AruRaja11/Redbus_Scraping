# importing the required packages
import streamlit as st
import mysql.connector as db
import pandas as pd

#redbus image
st.image("redbus_thumbnail.png", width=100)

# title to the project
st.title("Scraping using Selenium, Mysql, Streamlit in Redbus")

# connecting the mysql database to fetch details
conn = db.connect(
    host = 'localhost',
    user ='root',
    password = 'Prototype_15',
    database = 'redbus_project1'
)
# initializing cursor
curr = conn.cursor()

# collecting distinct states from the database
curr.execute("select distinct state from redbus_project1.routes_and_states")
fetched_datas   = curr.fetchall()

datas = pd.DataFrame(fetched_datas) # storing the query result in the dataframe

# creating a selection box to select the state
select_menu = st.selectbox("choose a state:", options=datas)

#selecting the route name based on user input in selection box
query = 'select routes from redbus_project1.routes_and_states where state=%s'
values = (select_menu,)
curr.execute(query, values)
data = curr.fetchall()

options2 = pd.DataFrame(data)# creating the result as dataframe

# create a price range radio button
ranges = st.radio('Choose a price range:' , ['0 - 250', '250 - 500', '500 and above'])
if ranges == '0 - 250':
    min = 0
    max = 250
elif ranges == '250 - 500':
    min=250
    max = 500
elif ranges == '500 and above':
    min = 500
    max = 50000

# creating the selectbox to select the route
select_menu2 = st.selectbox('choose a route: ', options=options2)

#select the bus details based on the user inputs from route name and price range
query = 'select * from redbus_project1.bus_details_redbus where route_name=%s and price between %s and %s'
values = (select_menu2, min, max)

curr.execute(query, values)
fetched_data = curr.fetchall()

# creating the result dataframe 
result_df = pd.DataFrame(fetched_data, columns=['Bus Name', 'Bus Type', 'Departure', 'Arrival', 'Duration', 'Price', 'Ratings', 'Seats Free', 'Route Name'])
# showing the dataframe in the output
st.table(result_df)

