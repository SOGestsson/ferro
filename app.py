# streamlit_app/app.py

import streamlit as st
from crud.update import RioItemsUpdater

def main():
    st.title("Rio Items Buy Frequency Updater")

    # Input for item ID
    item_id = st.number_input("Enter Item ID:", min_value=1, step=1)

    # Input for new buy frequency
    new_buy_freq = st.number_input("Enter New Buy Frequency:", min_value=0, step=1)

    if st.button("Update Buy Frequency"):
        if item_id and new_buy_freq >= 0:
            updater = RioItemsUpdater()
            updater.update_buy_freq(item_id, new_buy_freq)
            st.success(f"Successfully updated item ID {item_id} with new buy frequency: {new_buy_freq}")
        else:
            st.error("Please provide valid inputs.")

if __name__ == "__main__":
    main()
