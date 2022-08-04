from fastapi import FastAPI 

app = FastAPI() #Objeto asignado a FastAPI

@app.get("/") #Decorador
async def root(): #Función asíncrona
    return {"message":"Hello World!"}

@app.get("/myname/{name}") #Decorador
async def myName(name: str): #Función asíncrona
    return {"message": f"Hello {name} this is my new API!"}