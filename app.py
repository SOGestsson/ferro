# streamlit_app/app.py

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

from models.orm_models import Session, RioItems
from crud.update import RioItemsUpdater
from crud.read import RioItemsRead




# Streamlit app
def main():
    st.title("Rio Items Buy Frequency Updater")

    alda = RioItemsRead()
    update = RioItemsUpdater()

    result = alda.get_filtered_items()


    data = [{'id': item.id, 
                 'innkaupum_haett': item.innkaupum_haett, 
                 'buy_freq': item.buy_freq,
                 'del_time': item.del_time}
                 for item in result]
    

   

    # Check if data is not empty
    if len(data) > 0 and all(isinstance(item, dict) for item in data):
        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Display the editable grid
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(editable=True)
        gb.configure_column("id", editable=False)
        gb.configure_selection('single')
        grid_options = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=grid_options
        )

        selected_rows = grid_response["selected_rows"]

        if selected_rows is not None:
            st.write(selected_rows.iloc[0,2])
            id = selected_rows.iloc[0, 0]
            buy_freq = selected_rows.iloc[0, 2]
            update.update_buy_freq(id, buy_freq)
            
            




    
if __name__ == "__main__":
    main()
