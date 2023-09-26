"""
Little online shop app
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {"table": 5, "pen": 4, "mouse": 1}


@app.get("/")
async def root():
    """
    Entry point of application
    :return: says hello
    """
    return {"message": "Hello World"}


# ENTRY POINTS
## Path parameter
@app.get("/items/get/{name}")
async def get_item(name: str):
    """
    Look up through available items
    :param name: Name of item
    :return: Number of items
    """
    if name not in items:
        raise HTTPException(status_code=404, detail="Good is not found")
    return {"message": f"We have {items[name]} of {name}"}


## Query parameter
@app.get("/items/{item}")
def buy_item(item: str, query: str | None = None):
    """
    Buy given number of items
    :param item: name of item
    :param query: number of item to buy
    :return: message about successful purchase
    or 404 if something wrong in query or item is not found
    """
    if item not in items:
        raise HTTPException(status_code=404, detail="Good is not found")

    if query:
        if query.isnumeric():
            cur_amount = items[item]
            query = int(query)
            if cur_amount >= query:
                cur_amount -= query
            else:
                raise HTTPException(
                    status_code=404, detail=f"Currently we have {cur_amount} of {item}"
                )
            return {"message": f"Bought {query} of {item}, {cur_amount} is left"}

    return {"message": "Choose amount of item!"}


## Request body
class Good(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Sample model for item to add a new item
    """

    name: str
    amount: int


@app.put("/items/add")
async def add_item(item: Good):
    """
    Add new item
    :param item: Name of item and its amount
    :return: Success message
    """
    items[item.name] = item.amount
    return {"message": f"{item.name} is added"}
