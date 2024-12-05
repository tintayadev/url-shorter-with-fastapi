from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Automatically add 'https://' if no scheme is provided
        if not self.url.startswith(('http://', 'https://')):
            self.url = 'https://' + self.url

    class Config:
        orm_mode = True

class URLResponse(BaseModel):
    short_url: str

    class Config:
        orm_mode = True

class ShortenUrlRequest(BaseModel):
    url: str  # Ensure this is a string, not HttpUrl

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True
