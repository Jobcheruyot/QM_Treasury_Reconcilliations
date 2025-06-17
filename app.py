import streamlit as st
import streamlit_authenticator as stauth

# --- User Credentials ---
names = ['Admin', 'User1']
usernames = ['admin', 'user1']
passwords = ['password123', 'user1pass']  # Plain passwords

# --- Hash the passwords ---
hashed_passwords = stauth.Hasher(passwords).generate()

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

    # 🔽 Add your dashboard or logic call here:
    # reconciliation_dashboard()
