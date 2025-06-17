import streamlit as st
from reconciliations.mpesa import run_mpesa_reconciliation
# If you add more reconciliations, import them here

st.set_page_config(page_title="QM Treasury Reconciliations", layout="wide")

st.sidebar.title("Reconciliation Options")
menu = st.sidebar.radio(
    "Select Reconciliation:",
    ("Mpesa Reconciliation", "Other Reconciliation (coming soon)")
)

if menu == "Mpesa Reconciliation":
    run_mpesa_reconciliation()
elif menu == "Other Reconciliation (coming soon)":
    st.info("Other reconciliation modules will appear here.")
