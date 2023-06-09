import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet

# Retrieve the encryption key from st.secrets
key = st.secrets["encryption_key"]

# Create a Fernet instance using the key
cipher_suite = Fernet(key)

# Read the encrypted CSV file as binary data
uploaded_file = st.file_uploader("Upload encrypted CSV file", type="csv")
if uploaded_file:
    encrypted_data = uploaded_file.read()

    # Decrypt the data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Convert the decrypted data into a pandas dataframe
    df = pd.read_csv(pd.compat.StringIO(decrypted_data.decode()))

    # Display the dataframe
    st.dataframe(df)
