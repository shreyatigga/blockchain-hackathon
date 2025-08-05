import streamlit as st
import json
import requests





def send_money(address, amount):
    url = "https://dev.neucron.io/v1/tx/spend"
    headers = {
        "accept": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQzNzY2OTcsImlhdCI6MTcxMTc4NDY5NywiaXNzIjoiaHR0cHM6Ly9uZXVjcm9uLmlvIiwianRpIjoiYzljOTE3MjAtMDM4Ny00ODcyLWFkOGItN2RjYjFhNzQ3MjUwIiwibmJmIjoxNzExNzg0Njk3LCJzdWIiOiIwZjMxNDU3ZS04Njk1LTQxYjAtODMyMC1mMDZmODQ3Mzc5OWYiLCJ1c2VyX2lkIjoiMGYzMTQ1N2UtODY5NS00MWIwLTgzMjAtZjA2Zjg0NzM3OTlmIn0._wrjsDHowmniEzxSw1gnIknYzDOPRgvyRxxzpZB1YJ0",
        "Content-Type": "application/json",
    }
    data = {"outputs": [{"address": address, "amount": amount, "note": "string"}]}
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            st.success("Money sent successfully!")
        else:
            st.error(f"Error: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")


# Streamlit web app
def main():
    st.title("Send Money")

    # Text input for address
    address = st.text_input("Enter Address", key="address")

    # Integer input for amount
    money = st.number_input("Enter Amount", min_value=0, step=1)
    amount = round(money)
    # Button to send money
    if st.button("Send Money"):
        if address and amount:
            send_money(address, amount)
        else:
            st.warning("Please enter both address and amount.")
    home = st.button("Home")
    if home:
        st.switch_page("app.py")


if __name__ == "__main__":
    main()

