from datetime import date
import random

class User():
    def __init__(self, username:str="username", password:str="password"):
        self.user_id = id
        if isinstance(username, str) and len(username)>1:
            self.username = username
        else:
            raise TypeError("Username is Not Valid! Please Enter a valid Username.")
        if isinstance(password, str) and len(password)>1:
            self.password = password
        else:
            raise TypeError("Password is Not Valid! Please Enter a valid Password.")
        
        
    def __str__(self) -> str:
        return f"{ self.user_id }:{ self.username }:{ self.password }"
    
    def __repr__(self) -> str:
        return f"{ self.user_id }:{ self.username }:{ self.password }"


class Task():
    def __init__(self, user_id:int="user_id", category:str="category", description:str="description", date:date="date"):
        self.id = id
        self.user_id = user_id
        if isinstance(category, str) and len(category)>1:
            self.category = category
        else:
            raise TypeError("Task's Category is Not Valid! Please Enter Task Category.")
        if isinstance(description, str) and len(description)>1:
            self.description = description
        else:
            raise TypeError("Task's Description is Not Valid! Please Enter Task Description.")
        self.date = date
        
    def __str__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    
    def __repr__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    


    
        