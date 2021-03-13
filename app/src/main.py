from datetime import timedelta

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status

app = FastAPI()


@app.get("/", tags=["default"])
def read_root():
    return {"apiStatus": "OK", "apiVersion": "1.0.0"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
