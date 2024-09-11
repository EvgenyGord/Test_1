from pydantic import BaseModel, StrictStr



class User_Response(BaseModel):
    userID: StrictStr
    username: StrictStr

