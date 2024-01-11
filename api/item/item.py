from fastapi import APIRouter

item_router = APIRouter()

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@item_router.get("/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@item_router.put("/{item_id}")
def update_item(item_id: int):
    return {"item_id": item_id}
