import requests
import streamlit as st
import json

# Define the URL_checkBalance endpoint
url_checkBalance = "https://dev.neucron.io/v1/wallet/balance"

# Define the query parameters
params = {"walletID": "72d5bc51-bd25-4acc-9042-5e1f54c09131"}

# Define the headers, including the authorization token
headers = {
    "accept": "application/json",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQyODk0MDYsImlhdCI6MTcxMTY5NzQwNiwiaXNzIjoiaHR0cHM6Ly9uZXVjcm9uLmlvIiwianRpIjoiMTc1NzJiMDQtZjYwZi00ZDNhLWE0NTEtN2JkOGEzYTZkNzNhIiwibmJmIjoxNzExNjk3NDA2LCJzdWIiOiI5NzY2MzU2ZC0yN2UxLTRmOGYtYjE3MC1hZjBhNTA0MmMyY2MiLCJ1c2VyX2lkIjoiOTc2NjM1NmQtMjdlMS00ZjhmLWIxNzAtYWYwYTUwNDJjMmNjIn0.J0DV6AnA5MR48jxaYHX8W0Vfp9cRQDOgwrNzT0XGrYg",
}

# Send the GET request
response_checkBalance = requests.get(url_checkBalance, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response_checkBalance.status_code == 200:
    # Print the response_checkBalance content (the balance)
    json_string = response_checkBalance.text
    data = json.loads(json_string)

    # Access the 'summary' value
    summary = data["data"]["balance"]["summary"]

    # Print the 'summary' value
    st.subheader(f"Your balance is: {summary}")
    home = st.button("Home")
    if home:
        st.switch_page("app.py")

else:
    # Print an error message if the request failed
    print("Error:", response_checkBalance.text)
