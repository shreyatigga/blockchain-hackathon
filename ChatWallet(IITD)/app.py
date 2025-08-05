import streamlit as st
import streamlit_authenticator as stauth
import requests
import pickle
from pathlib import Path

st.set_page_config(page_title="ChatWallet 💵")
names = ["Aman Dev"]
usernames = ["amandev2003@gmail.com"]
# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    names, usernames, hashed_passwords, "minor2", "abcdef", cookie_expiry_days=0
)
name, authentication_status, username = authenticator.login("Login", "main")
col1, col2, col3, col4 = st.columns(4)


def createWallet():
    url_create_wallet = "https://dev.neucron.io/v1/wallet/create"

    # Define the headers, including the authorization token
    headers = {
        "accept": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQzNzkwNzQsImlhdCI6MTcxMTc4NzA3NCwiaXNzIjoiaHR0cHM6Ly9uZXVjcm9uLmlvIiwianRpIjoiYzBhYjI2NmQtMmMyNy00MTQ3LThkNjctZGQ0YWFmMTVjNGNiIiwibmJmIjoxNzExNzg3MDc0LCJzdWIiOiI5NzY2MzU2ZC0yN2UxLTRmOGYtYjE3MC1hZjBhNTA0MmMyY2MiLCJ1c2VyX2lkIjoiOTc2NjM1NmQtMjdlMS00ZjhmLWIxNzAtYWYwYTUwNDJjMmNjIn0.RQtQV9BHtRv-lo7LXv58aP5Rew6E7m7gLNO3B1THyLk",
    }

    try:
        # Send the POST request to create a new wallet
        response = requests.post(url_create_wallet, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response data
            st.success("New wallet created successfully.")
            st.write("Response:", response.json())
        else:
            # Print an error message if the request failed
            st.write("Error:", response.text)

    except requests.exceptions.RequestException as e:
        # Print an error message if the request encountered an exception
        print("Request failed:", e)


st.header("ChatWallet 💵")

if authentication_status:
    logout = authenticator.logout
    if username == "amandev2003@gmail.com":
        url = "https://dev.neucron.io/v1/auth/login"
        # Define the request body (data)
        data = {"email": "amandev2003@gmail.com", "password": "Amanbondla2003."}

        # Define the headers
        headers = {"accept": "application/json", "Content-Type": "application/json"}

        # Send the POST request
        response = requests.post(url, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content (authentication token)

            st.success("Login Successful")

        def handle_greeting(prompt):

            st.switch_page("pages/checkBalance.py")

        def handle_weather(prompt):
            # Your weather-related function logic here
            st.switch_page("pages/transaction.py")
            return response

        def handle_news(prompt):
            # Your news-related function logic here
            response = st.write(
                "I'm sorry, I cannot provide news updates at the moment."
            )
            return response

        def chatbot(prompt):
            if "balance" in prompt.lower():
                return handle_greeting(prompt)
            elif "send money" in prompt.lower():
                return handle_weather(prompt)
            elif "news" in prompt.lower():
                return handle_news(prompt)
            else:
                return "I'm sorry, I don't understand. Could you please rephrase your query?"

        key_counter = 0
        input_key = f"user_input_{key_counter}"
        # Main loop
        while True:
            key_counter += 1
            input_key = f"user_input_{key_counter}".replace(".',", "_")
            user_input = st.text_input(
                label="How can I help you?"
            )  # Placeholder text for input
            bot_response = chatbot(user_input)
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
        # with col1:
        #     balance = st.button("Check balance")
        #     if balance:
        #         st.switch_page("pages/checkBalance.py")
        # with col2:
        #     wallet_list = st.button("View Wallets")
        #     if wallet_list:
        #         st.switch_page("pages/walletList.py")
        # with col3:
        #     create_wallet = st.button("Create Wallet")
        #     if create_wallet:
        #         # Define the URL endpoint
        #         createWallet()
        # with col4:
        #     send_money = st.button("Payment")
        #     if send_money:
        #         st.switch_page("pages/transaction.py")

    else:
        st.error("Invalid username or password")
