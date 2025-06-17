import streamlit as st
import streamlit_authenticator as stauth

# --- User Credentials ---
names = ['Admin', 'User1']
usernames = ['admin', 'user1']
passwords = ['password123', 'user1pass']  # Replace with your secure passwords

# --- Hash the passwords (for security) ---
hashed_passwords = stauth.Hasher(passwords).generate()

# --- Set up the authenticator ---
authenticator = stauth.Authenticate(
    names,                # Display names
    usernames,            # Corresponding usernames
    hashed_passwords,     # Hashed passwords
    'treasury_dashboard', # Cookie name (any unique string)
    'abcdef',             # Cookie key (any random string)
    cookie_expiry_days=1  # Cookie expiry in days
)

# --- Login Widget ---
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
elif authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f'Logged in as {name}')
    # Your menu and reconciliation code goes here!
