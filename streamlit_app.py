import streamlit

streamlit.title('My Mom\'s new healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('  🥗 Kale, & Spinach Rocket Smoothie')
streamlit.text(' 🐔 Hard-boiled free-range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_list)
