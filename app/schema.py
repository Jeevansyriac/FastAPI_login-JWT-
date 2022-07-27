from typing import Optional
from pydantic import BaseModel


class Base(BaseModel):

    title   :str
    price   :str

class user(BaseModel):

    fullname  : str
    email     : str
    password  : str

class userlogin(BaseModel):
    email     : str
    password : str
    

       
            
                
            
        

        
            
                          

    
            
            
        
