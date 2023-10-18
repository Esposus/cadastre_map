import random
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/result')
def emulate_external_server(cadastre_number: int, latitude: float, longitude: float):
    time.sleep(random.uniform(0, 2))
    response_data = {'response': random.choice([True, False])}
    return response_data


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
