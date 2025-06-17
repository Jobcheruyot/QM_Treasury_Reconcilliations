import streamlit as st
import streamlit_authenticator as stauth
from reconciliations.mpesa import run_mpesa_reconciliation  # Make sure this exists and is correct

st.set_page_config(page_title="QM Treasury Reconciliations", layout="wide")

# --- User Credentials ---
names = ['Admin', 'User1']
usernames = ['admin', 'user1']
passwords = ['password123', 'user1pass']  # Change for production

# --- Hash the passwords ---
hashed_passwords = stauth.Hasher(passwords).generate()

# --- Set up the authenticator ---
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'treasury_dashboard',  # Cookie name
    'abcdef',              # Key for extra security (change for production)
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
elif authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f'Logged in as {name}')
    st.sidebar.title("Reconciliation Options")
    menu = st.sidebar.radio(
        "Select Reconciliation:",
        ("Mpesa Reconciliation", "Other Reconciliation (coming soon)")
    )
    if menu == "Mpesa Reconciliation":
        run_mpesa_reconciliation()
    elif menu == "Other Reconciliation (coming soon)":
        st.info("Other reconciliation modules will appear here.")
