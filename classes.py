from datetime import date
import random

class User():
    def __init__(self, username:str="username", password:str="password"):
        self.user_id = id
        self.username = username   
        self.password = password   
        
    def __str__(self) -> str:
        return f"{ self.user_id }:{ self.username }:{ self.password }"
    
    def __repr__(self) -> str:
        return f"{ self.user_id }:{ self.username }:{ self.password }"


class Task():
    def __init__(self, id = id, user_id:int="user_id", category:str="category", description:str="description", date:date="date",completed=0):
        self.id = id
        self.user_id = user_id
        self.category = category
        self.description = description
        self.date = date
        self.completed = completed



    def __str__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    
    def __repr__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    


    
        