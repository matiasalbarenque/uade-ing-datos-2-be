import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.routes.api:app", host="localhost", port=8081, reload=True)
