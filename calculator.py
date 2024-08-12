import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input numbers with unique keys
num1 = st.number_input("Enter the first number", value=0.0, step=1.0, key='num1')
num2 = st.number_input("Enter the second number", value=0.0, step=1.0, key='num2')

# Select operation
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"), key='operation')

# Perform the calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Division by zero is not allowed")
        result = None

# Display the result
if result is not None:
    st.write(f"The result is: {result}")
