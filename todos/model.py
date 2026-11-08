from pydantic import BaseModel, ConfigDict

# class Item(BaseModel):
#     item: str
#     status: str

class Todo(BaseModel):
    id: int
    item: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": [
                {
                    "id": 1,
                    "item": "Example Schema!"
                }
            ]
        }
    )

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }