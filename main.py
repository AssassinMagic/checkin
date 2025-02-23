import sys
from attendance import AttendanceBackend
import time
import streamlit as st


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

attendance = st.Page("tools/attendancePage.py", title="Attendance", icon=":material/check:")
reservations = st.Page("tools/reservationsPage.py", title="Reservations", icon=":material/dashboard:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Tools": [attendance, reservations],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()