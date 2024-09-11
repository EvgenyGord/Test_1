from pydantic import BaseModel, StrictStr


class GenerateTokenResponse(BaseModel):
    token: StrictStr
    expires: StrictStr
    status: StrictStr
    result: StrictStr
