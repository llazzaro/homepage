from google.appengine.ext import db

class BaseModel(db.Model):
    """
        All models should extend this class 
    """
    @classmethod
    def get(cls,identifier):
        q = db.Query(cls).filter('name =',identifier)
        return q.get()
