# crud/update.py

from models.orm_models import Session, RioItems

class RioItemsUpdater:
    def __init__(self):
        # Create a new session
        self.session = Session()

    def update_buy_freq(self, item_id, new_buy_freq):
        try:
            # Find the item by id
            item = self.session.query(RioItems).filter(RioItems.id == item_id).first()
            if item:
                # Update the buy_freq
                item.buy_freq = new_buy_freq
                # Commit the transaction
                self.session.commit()
                print(f"Updated item ID {item_id} with new buy_freq {new_buy_freq}")
            else:
                print(f"No item found with ID {item_id}")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.session.rollback()
        finally:
            # Close the session
            self.session.close()


