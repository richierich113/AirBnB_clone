#!/usr/bin/python3
""" module with BaseModel super class which all other class models
in the project inherits from
"""


from datetime import datetime
import models
import uuid


class BaseModel:
    """base model parent class  that defines all common
    attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """The constructor method for the BaseModel class
        which initializes instance attributes passed to the class
        Args:
            args: list of arguments passed
            kwargs: dictionary of key-values arguments passed
        """
        if len(kwargs) >= 1 and kwargs is not None:
            self.set_kwargs_as_attr(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #models.storage.new(self)

    def __str__(self):
        """Returns string in the format
        [<class name>] (<self.id>) <self.__dict__>
        Returns:
            string: string representation of
            [self.__class__.__name__] (self.id) self.__dict__
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        custom_dict = self.__dict__.copy()
        custom_dict['__class__'] = self.__class__.__name__
        custom_dict['created_at'] = self.created_at.isoformat()
        custom_dict['updated_at'] = self.updated_at.isoformat()
        return custom_dict

    def set_kwargs_as_attr(self, **kwargs):
        """This checks the passed keyword arguments from a dictionary
        if it has keys named "created_at" and  "updated_at" to
        convert their time values
        else it sets them passed keyword arguments as instance
        attributes as with their values
        in the BaseModel class
        Args:
            kwargs: dictionary of key-values arguments passed
        """
        for (key, value) in kwargs.items():
            keys = ["created_at", "updated_at"]
            if key in keys[:]:
                self.__dict__[key] = datetime\
                    .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[key] = value
