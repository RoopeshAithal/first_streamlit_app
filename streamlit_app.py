
import streamlit
import pandas
streamlit.title('My new streamlit app')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Omlett')
streamlit.text('🐔 Boiled Egg')
streamlit.text('🥗 Blueberry , Spinach & dates Smoothie')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_lis = my_fruit_lis.set_index('Fruit')
streamlit.multiselect("Pick some Fruite:" ,list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
