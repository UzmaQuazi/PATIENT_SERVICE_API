from fastapi import FastAPI

 

app = FastAPI()

 


@app.get("/")

async def root():

    return {"message": "Hello World"}

 

@app.get("/users")

async def get_users():

    return [

        {

            "firstName": "Quazi",

            "lastName": "Uzma",

            "email": "quaziuzma@gmail.com"

        }

    ]