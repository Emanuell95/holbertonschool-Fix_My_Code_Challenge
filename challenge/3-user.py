#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid

class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """
    def __init__(self):
        """Initialize a new user with a unique ID"""
        self.id = str(uuid.uuid4())
        self.__password: str | None = None

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - Set to None if input is None or not a string
        - Otherwise hash with MD5 and store as lowercase
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Validate password:
        - Returns False if pwd is None, not a string, or no password set
        - Otherwise compare MD5 hash
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password