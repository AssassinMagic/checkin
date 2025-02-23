import streamlit as st
import pandas as pd
from attendance import AttendanceBackend

# Sample data for reservations
reservations = AttendanceBackend().get_all_users()

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(reservations)

# Streamlit app
st.title("Reservations Page")

# Search bar
search_query = st.text_input("Search reservations")

# Filter reservations based on search query
if search_query:
    filtered_df = df[df.apply(lambda row: search_query.lower() in row.astype(str).str.lower().to_string(), axis=1)]
else:
    filtered_df = df

# Display the reservations
st.dataframe(filtered_df)