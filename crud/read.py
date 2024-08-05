from models.orm_models import Session, RioItems

class RioItemsRead:
    def __init__(self):
        # Create a new session
        self.session = Session()

    def get_filtered_items(self):
        query = self.session.query(RioItems).filter(
                RioItems.innkaupum_haett == 0
                )
        
        return query.all()
    

   
   
