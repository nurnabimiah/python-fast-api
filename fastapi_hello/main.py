from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Hello, Nayon!"
    }


@app.get("/user")
async def user():
    return {
        "id": 1,
        "name": "Farhad",
        "Profession": "Farmer",

    }
