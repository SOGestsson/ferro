# main.py

from models.orm_models import RioItems, Session
from crud.update import RioItemsUpdater

def main():
    # Create a new session
    session = Session()

    try:
        # Query the top 10 records in the rio_items table
        top_rio_items = session.query(RioItems).limit(100).all()

        # Print each record
        for item in top_rio_items:
            print(f"ID: {item.id}, Buy Frequency: {item.buy_freq}, Delivery Time: {item.del_time}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the session
        session.close()

        # Create an updater instance
    updater = RioItemsUpdater()

    # Update buy_freq for a specific item
    item_id = 118026  # Example item ID
    new_buy_freq = 20  # Example new buy_freq value
    updater.update_buy_freq(item_id, new_buy_freq)

if __name__ == "__main__":
    main()

