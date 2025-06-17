import streamlit as st
import streamlit_authenticator as stauth

# --- User Credentials ---
names = ['Admin', 'User1', 'User2']
usernames = ['admin', 'user1', 'user2']
passwords = ['admin123', 'user1pass', 'user2pass']  # Use strong passwords!

# --- Hash the passwords (for security) ---
hashed_passwords = stauth.Hasher(passwords).generate()

# --- Set up the authenticator ---
authenticator = stauth.Authenticate(
    names,                # Display names
    usernames,            # Corresponding usernames
    hashed_passwords,     # Hashed passwords
    'treasury_dashboard', # Cookie name (can be any string)
    'abcdef',             # Cookie key (should be random)
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
    # ...rest of your app goes here...import streamlit as st

# -----------------------------
# Dummy credentials dictionary
# Replace with secure storage in production
# -----------------------------
USER_CREDENTIALS = {
    "admin": "admin123",
    "job": "cheruyot2025"
}

# -----------------------------
# Login form UI
# -----------------------------
def login_form():
    st.title("🔐 QM Treasury Reconciliations Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome {username}")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

# -----------------------------
# Logout button in sidebar
# -----------------------------
def logout_button():
    st.sidebar.markdown(f"👤 **User:** `{st.session_state.username}`")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# -----------------------------
# Main Reconciliation App Logic
# -----------------------------
def reconciliation_dashboard():
    st.title("📊 QM Treasury Reconciliations")
    st.markdown("This is the main dashboard. Add your reconciliation logic here.")
    # Example placeholder
    st.info("🔄 Upload reconciliation files and trigger processing.")

# -----------------------------
# Initialize session states
# -----------------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# -----------------------------
# Render app based on session
# -----------------------------
if st.session_state.logged_in:
    logout_button()
    reconciliation_dashboard()
else:
    login_form()
