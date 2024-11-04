# importing the required packages
import streamlit as st
import mysql.connector as db
import pandas as pd
import datetime as dt

#creating a fixed heading 
st.markdown(
    """
    <style>
    .fixed-header {
        max-height:250px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #4CAF50; 
        color: white; 
        text-align: center;
        padding: 50px;
        padding-bottom: 20px;
        font-size: 20px;
        z-index: 9999;
        border-bottom: 2px solid #ccc;
        display: flex;
        align-items: center;
        justify-content: center;
         
    }
    
    .fixed-header img {
        height: 90px;
        width: 90px;
    }
    
    .main-content {
        margin-top: 120px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fixed Header Content with Image and Title
st.markdown(
    '''
    <div class="fixed-header">
    <img src="https://i.pinimg.com/originals/58/91/2b/58912b2e3ad6a279347eebb47751a9c1.png" >
        <h1> Scraping using selenium, Mysql and streamlit</h1>
    </div>
    ''', 
    unsafe_allow_html=True
)


# Main content starts here
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.write("## Showing Bus Operations")
st.write("Use filters and search options below to find the best bus for your journey.")

# Add your interactive components here...

# Closing the main content div
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .stExpander .streamlit-expanderIcon {
        display: "Filters";
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar.expander("Filters and Options", expanded=False):
    ranges = st.slider("Price", min_value=100, max_value=2000, value=(100, 2000))
    # displaying the price range
    st.write("Price Ranges : Rs", str(ranges[0]), " to Rs", str(ranges[1]))
    st.markdown("---")
    start_time, end_time = st.slider("Departure",value=(dt.time(0,0), dt.time(23, 59)))
    st.write("Departure Time :", start_time.strftime("%H:%M"), " to ", end_time.strftime("%H:%M"))
    st.markdown("---")
    ratings = st.slider("Ratings", min_value=0.0, max_value=5.0, value=(0.0, 5.0))
    st.write("Ratings: ", str(ratings[0]), "to ",str(ratings[1]))
    st.markdown("---")
    bus_types = [
    "ALL",
    'A/C SEATER', 
    'A/C SLEEPER SEATER', 
    'A/C OTHER THAN 2+2', 
    'DELUXE 3X2', 
    'NON A/C SEATER', 
    'NON A/C SLEEPER'
    ]
    selected_bus_type = st.selectbox("Bus Type", options=bus_types)


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

col1, col2 = st.columns(2)
# creating a selection box to select the state
with col1:
    select_menu = st.selectbox("choose a state:", options=datas)

#selecting the route name based on user input in selection box
query = 'select routes from redbus_project1.routes_and_states where state=%s'
values = (select_menu,)
curr.execute(query, values)
data = curr.fetchall()

options2 = pd.DataFrame(data)# creating the result as dataframe

# statement for properly quering the bus type
if selected_bus_type == "ALL":
    bus_type1 = "% %"
    not_like = "sample" 
elif selected_bus_type == "A/C SEATER":
    bus_type1 = "%A/C Seater%"
    not_like = "%Sleeper%"
elif selected_bus_type == 'A/C SLEEPER SEATER':
    bus_type1 = "%A/C Seater / Sleeper%"
    not_like = "%Non%"
elif selected_bus_type == 'A/C OTHER THAN 2+2':
    bus_type1 = "%A/C Seater / Sleeper%"
    not_like = "%2+2%"
elif selected_bus_type == 'DELUXE 3X2':
    bus_type1 = "%Deluxe%"
    not_like = "%Ultra%"
elif selected_bus_type == 'NON A/C SEATER':
    bus_type1 = "%Non A/C Seater%"
    not_like = "%Sleeper%"
elif selected_bus_type == 'NON A/C SLEEPER':
    bus_type1 = "%Non A/C Seater%"
    not_like = "%sample%"


# creating the selectbox to select the route
with col2:
    select_menu2 = st.selectbox('choose a route: ', options=options2)

st.write(f"**Showing Results for {select_menu} ➡ {select_menu2}**")
#select the bus details based on the user inputs from route name and price range
query = 'select * from redbus_project1.bus_details_redbus where route_name=%s and price between %s and %s and departure between %s and %s and bus_type like %s and bus_type not like %s and ratings between %s and %s'
values = (select_menu2, ranges[0], ranges[1], start_time, end_time, bus_type1, not_like, ratings[0], ratings[1])

curr.execute(query, values)
fetched_data = curr.fetchall()

# creating the result dataframe 
result_df = pd.DataFrame(fetched_data, columns=['Bus Name', 'Bus Type', 'Departure', 'Arrival', 'Duration', 'Price', 'Ratings', 'Seats Free', 'Route Name'])
# showing the dataframe in the output

styled_data = result_df.style.applymap(lambda x: 'background-color: lightgreen' if isinstance(x, int) and x > 85 else '')

st.write(styled_data)

