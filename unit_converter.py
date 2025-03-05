import streamlit as st
from pint import UnitRegistry

st.title("Complex unit convertor"); # this is the title of our app

unit_registery = UnitRegistry(); #it will store all the units name like kilometers,centimeters,celsius etc

numeric_val = st.number_input("Please enter the numeric value to be converted"); # it will take tha numeric value from the user and stotre it in a numeric_value
converted_from = st.text_input("Converted from (e.g., km, m, lb, kg, Celsius):"); #it will ask the user from which unit the conversion has to be
converted_to = st.text_input("Converted to  (e.g., mile, cm, g, Fahrenheit):"); #it will ask the user in which nits he want value

if st.button("Converted"): #the s.button() will run when user click the button
    try:
        val_in_units = numeric_val * unit_registery(converted_from)  #it will make the numeric value to the unit value lik 10 kilometers
        result = val_in_units.to(converted_to) #it will cnvert that in another unit
        st.success(f"your unit have beeen converted successfully and {numeric_val} {converted_from} is = {result}") #st.success just print our result
    except:
        st.error("Invalid Conversion.Please check your values"); # if user enter any wrong value or unit thiss error will run