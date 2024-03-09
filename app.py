from fastapi import FastAPI

 

app = FastAPI()

 


@app.get("/")

async def root():

    return {"message": "Hello World"}

 

@app.get("/users")

async def get_users():

    return [

        {

            "firstName": "Fritz",

            "lastName": "Batroni",

            "email": "fritz.g.batroni@gmail.com"

        }

    ]