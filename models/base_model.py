#!/usr/bin/python3

from datetime import datetime
class BaseModel:
    """base model parent class  that defines all common
    attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """The constructor method for the BaseModel class
        which initializes instance attributes passed to the class
        """
       if len(kwargs) >= 1 and kwargs is not None:
           self.set_custom_attr(**kwargs)
       else:
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()

    def set_custom_attr(self, **kwargs):
        """
        """
