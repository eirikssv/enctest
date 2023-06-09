import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
import requests
import io

# Retrieve the encryption key from st.secrets
key = st.secrets["encryption_key"]

# Create a Fernet instance using the key
cipher_suite = Fernet(key)

# Google Drive file URL
# file_url = "<your_google_drive_url_here>"
# file_url = ""

url = 'https://drive.google.com/file/d/1Fu9GZAYtAmRumGQpjqJgnXNHnK697RBD/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
# Fetch the encrypted file content
response = requests.get(url)
encrypted_data = response.content

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Convert the decrypted data into a pandas dataframe
df = pd.read_csv(io.StringIO(decrypted_data.decode()))

# Display the dataframe
st.dataframe(df)
