from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl

    class Config:
        orm_mode = True

class URLResponse(BaseModel):
    short_url: str

    class Config:
        orm_mode = True
