from fastapi import FastAPI

app = FastAPI(title="Hello DevOps")


@app.get("/")
def root():
    return {"message": "Hello, DevOps!"}


@app.get("/health")
def health():
    return {"status": "ok"}


def add(a: int, b: int) -> int:
    return a - b
