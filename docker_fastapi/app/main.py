from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI() #Objeto asignado a FastAPI

@app.get("/") #Decorador
async def root(): #Función asíncrona
    return {"message":"Hello World!"}

@app.get("/myname/{name}") #Decorador
async def myName(name: str): #Función asíncrona
    return {"message": f"Hello {name}, this is my new API!"}

@app.get("/picture") #Decorador
async def pict(): #Función asíncrona
    return RedirectResponse('https://images.pexels.com/photos/12708081/pexels-photo-12708081.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
