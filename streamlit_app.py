import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#import pandas
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


#import requests
def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
	furityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	return furityvice_normalized 

streamlit.header('Fruityvice Fruit Advice!')

try:
	fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
	if not fruit_choice:
		streamlit.error("Please Select a Fruit to get Information.")
	else:
		back_from_function = get_fruityvice_data(fruit_choice)
		streamlit.dataframe(back_from_function )

except URLError as e:
	streamlit.error()

#streamlit.stop()
#import snowflake.connector
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("SELECT * FROM fruit_load_list")
		return my_cur.fetchall()
	
if streamlit.button('Get Fruit Load List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	my_cnx.close()
	streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
		return "Thanks for adding "+new_fruit
	


add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	back_from_function = insert_row_snowflake(add_my_fruit)
	my_cnx.close()
	streamlit.text(back_from_function)
