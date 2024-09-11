from pydantic import BaseModel, StrictStr


class User_Get_Response(BaseModel):
    userId: StrictStr
    username: StrictStr