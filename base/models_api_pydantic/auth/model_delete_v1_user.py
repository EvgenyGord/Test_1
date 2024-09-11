from pydantic import BaseModel, StrictStr


class User_Delete_Response(BaseModel):
    code: StrictStr
    message: StrictStr