
import streamlit
import pandas
streamlit.title('My new streamlit app')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Omlett')
streamlit.text('🐔 Boiled Egg')
streamlit.text('🥗 Blueberry , Spinach & dates Smoothie')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some Fruite:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_display = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_display)


streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user enterd', fruit_choice)
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
furityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(furityvice_normalized )

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
