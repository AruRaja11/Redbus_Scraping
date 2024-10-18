Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

PROBLEM DESCRIPTION
  The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

TECHNOLOGIES USED:
  1. Selenium : Used for scraping data from the Redbus website.
  2. Python : Used as the programing language.
  3. Pandas : A library in pandas used in handling and cleaning data.
  4. Mysql : It is a query language used to store, access and manage the data
  5. Streamlit : It is used to design UI and display the output

STEP 1: Run the "Route_Details_file1.ipynb" file to fetch the routes of 10 states
  * This page contains programs to scrap the routes of 10 states, this runs on a loop where each states are passed as parameters.
  * The datas are fetched continuesly and the data contains state name, route name, and route link.
  * The data is stored in a csv file and further used to fetch the bus details.
    
STEP 2: Run the "Bus_details_file2.ipynb" file to fetch all bus details of all states
  * This page contains program to scrap details of each bus that contains government bus details if possible and also it contains the details of private buses.
  * The program runs independently for each states because it takes quite a lot of time to fetch details.
  * The fetched details are stored in a csv file and used for further cleaning and managing.
    
STEP 3: Run the "MYSQL_file3.ipynb" to clean the fetched datas and store them in mysql database.
  * This file contains program to clean datas and store them in mysql
  * pandas is clean the data
  * mysql connector is used to store the data in the database into mysql database.
    
STEP 4: Run "app.py" file which contains the interface of the project using streamlit.
  * Streamlit is used here to create an UI
  * mysql is used by which the datas are shown as output based on user input
