import streamlit as st 

st.title("Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection - Matches the IF statements below
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

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
        st.error("Cannot divide by zero!") 
        result = "Undefined"

# Display the result formatted nicely
st.subheader(f"Result: {result}")