from datetime import date

class Task():
    def __init__(self, category:str="category", description:str="description", date:date="date"):
        self.category = category
        self.description = description
        self.date = date

    def __str__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    
    def __repr__(self) -> str:
        return f"{ self.category }:{ self.description }:{ self.date }"
    
        