# import streamlit as st

# def main():
#     # Set page title and configuration
#     st.title('Simple Calculator')
#     st.write('Enter two numbers and select an operation to calculate value.')

#   # Create two columns for number inputs
#     col1, col2 = st.columns(2)

#      # Input fields for numbers
#     with col1:
#         num1 = st.number_input('Enter first number', value=0.0)
#     with col2:
#         num2 = st.number_input('Enter second number', value=0.0)

#  # Operation selection
#     operation = st.selectbox("Select operation", ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (÷)",])

#  # Calculate button
#     if st.button('Calculate'):
#         try:
#             if operation == 'Addition (+)':
#                 result = num1 + num2
#                 symbol = '+'

#             elif operation == 'Subtraction (-)':
#                 result = num1 - num2
#                 symbol = '-'

#             elif operation == 'Multiplication (x)':
#                 result = num1 * num2
#                 symbol = 'x'
#             elif operation == 'Division (÷)':
#                 if num2 == 0:
#                     st.error('Division by zero is not allowed')
#                     return
#                 result = num1 / num2
#                 symbol = '÷'


#                   # Display result with styling
#             st.success(f"Answer: {num1} {symbol} {num2} = {result}") 


#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
            
# # run the main function if the script is executed directly
# if __name__ == '__main__':
#     main()








import streamlit as st

def main():
    # Set page title and configuration
    st.set_page_config(page_title='Simple Calculator', page_icon='➗', layout='centered')
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 38px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stNumberInput>div>div>input {
            font-size: 18px;
        }
        .stSelectbox>div>div {
            font-size: 18px;
        }
        .result-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #333;
            box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Simple Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter two numbers and select an operation to calculate the value.</p>", unsafe_allow_html=True)

    # Create two columns for number inputs
    col1, col2 = st.columns(2)

    # Input fields for numbers
    with col1:
        num1 = st.number_input('Enter first number', value=0.0)
    with col2:
        num2 = st.number_input('Enter second number', value=0.0)

    # Operation selection
    operation = st.selectbox('Select operation', ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (÷)"],)

    # Calculate button
    if st.button('Calculate'):
        try:
            if operation == 'Addition (+)':
                result = num1 + num2
                symbol = '+'

            elif operation == 'Subtraction (-)':
                result = num1 - num2
                symbol = '-'

            elif operation == 'Multiplication (x)':
                result = num1 * num2
                symbol = 'x'
            elif operation == 'Division (÷)':
                if num2 == 0:
                    st.error('Division by zero is not allowed')
                    return
                result = num1 / num2
                symbol = '÷'


            # Display result with styling
            st.markdown(f'<div class="result-box">Answer: {num1} {symbol} {num2} = {result}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
