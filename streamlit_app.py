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

streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit List contains:")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('The user enterd', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from Streamlit')")
