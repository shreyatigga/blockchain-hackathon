import requests
import json
import streamlit as st

# Define the URL endpoint
url = 'https://dev.neucron.io/v1/wallet/list'

# Define the headers, including the authorization token
headers = {
    'accept': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQzNzkwNzQsImlhdCI6MTcxMTc4NzA3NCwiaXNzIjoiaHR0cHM6Ly9uZXVjcm9uLmlvIiwianRpIjoiYzBhYjI2NmQtMmMyNy00MTQ3LThkNjctZGQ0YWFmMTVjNGNiIiwibmJmIjoxNzExNzg3MDc0LCJzdWIiOiI5NzY2MzU2ZC0yN2UxLTRmOGYtYjE3MC1hZjBhNTA0MmMyY2MiLCJ1c2VyX2lkIjoiOTc2NjM1NmQtMjdlMS00ZjhmLWIxNzAtYWYwYTUwNDJjMmNjIn0.RQtQV9BHtRv-lo7LXv58aP5Rew6E7m7gLNO3B1THyLk'
}

try:
    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the list of wallets
        wallets = response.text
        st.header("Paymails")
        st.subheader("Paymails for your wallet ")
        # st.write the list of wallets
        data = json.loads(wallets)
        wallets = data['data']['Wallets']
        for wallet_id, wallet_info in wallets.items():
            wallet_name = wallet_info['wallet_name']
            paymails = wallet_info['paymails']
            
            st.write("Paymails:", str(paymails))

        
        # st.write an error message if the request failed
        st.write("Error:", response.text)

except requests.exceptions.RequestException as e:
    # st.write an error message if the request encountered an exception
    st.write("Request failed:", e)
