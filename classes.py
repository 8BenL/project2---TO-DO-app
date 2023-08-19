from datetime import date

class Task():
    def __init__(self, category:str="category", description:str="description", date:date="date"):
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
    
        