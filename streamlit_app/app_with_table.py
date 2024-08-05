# streamlit_app/app.py

import sys
import os
import streamlit as st
from streamlit_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from models.orm_models import Session, RioItems
from crud.update import RioItemsUpdater

# Ensure the models and crud modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Function to fetch data from the database
def fetch_data():
    session = Session()
    try:
        items = session.query(RioItems).all()
        data = [{"id": item.id, "buy_freq": item.buy_freq, "del_time": item.del_time} for item in items]
        return data
    finally:
        session.close()

# Streamlit app
def main():
    st.title("Rio Items Buy Frequency Updater")

    # Fetch data from the database
    data = fetch_data()

    # Display the editable grid
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(editable=True)
    gb.configure_column("id", editable=False)
    gb.configure_selection('single')
    grid_options = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        height=400,
        reload_data=True
    )

    # Check for updates
    if grid_response['data'] != data:
        # Get the updated data
        updated_data = grid_response['data']

        # Find the changes and update the database
        updater = RioItemsUpdater()
        for original_row, updated_row in zip(data, updated_data):
            if original_row['buy_freq'] != updated_row['buy_freq']:
                updater.update_buy_freq(updated_row['id'], updated_row['buy_freq'])
                st.success(f"Updated item ID {updated_row['id']} with new buy frequency: {updated_row['buy_freq']}")

if __name__ == "__main__":
    main()
