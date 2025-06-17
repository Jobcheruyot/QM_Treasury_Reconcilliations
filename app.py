import streamlit as st
import streamlit_authenticator as stauth

# --- User Credentials ---
names = ['Admin', 'User1']
usernames = ['admin', 'user1']
passwords = ['password123', 'user1pass']

# --- Hash the passwords (correct syntax for streamlit-authenticator >= 0.4.2) ---
hasher = stauth.Hasher()
hashed_passwords = hasher.generate(passwords)

# --- Authenticator setup ---
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'treasury_dashboard',
    'abcdef',
    cookie_expiry_days=1
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

    # ✅ Your dashboard or reconciliation call goes here
