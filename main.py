# from typing import Union

# from fastapi import FastAPI
# from app.item.models.item import Item

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "boo"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

import os

import click
import uvicorn

# from core.config import config


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    uvicorn.run(
        app="app.server:app",
        # host=config.APP_HOST,
        # port=config.APP_PORT,
        # reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()

