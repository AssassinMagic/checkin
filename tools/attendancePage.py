import streamlit as st
from attendance import AttendanceBackend

# Initialize backend and session state
if "attendance_backend" not in st.session_state:
    st.session_state.attendance_backend = AttendanceBackend()

if "table_data" not in st.session_state:
    st.session_state.table_data = []

def load_data():
    checked_in = st.session_state.attendance_backend.initalize_attendance()
    st.session_state.table_data = checked_in

def swipe_card(card_id):
    user_data = st.session_state.attendance_backend.swipe_card(card_id)
    st.session_state.table_data.append(user_data)

st.header("Attendance Page")

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Load Data"):
        load_data()
with col2:
    card_id = st.text_input("Swipe Card...")
    if card_id:
        swipe_card(card_id)

# Display the table
st.table(st.session_state.table_data)