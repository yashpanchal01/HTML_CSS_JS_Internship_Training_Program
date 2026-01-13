import streamlit as st 
st.title("make as simple calculator app")
num1 = st.number_input("Enter first number ")
num2 = st.number_input('Enter second number')


operation = st.selectbox("Choose any operation: ", ["add", "subtract", "multiply", "divide"])
result = 0
if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        st.warning("Cannot divide by zero!") # Shows a warning for division by zero
        result = "Undefined"

st.write('result', result)
