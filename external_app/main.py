import random
import time
from fastapi import FastAPI


app = FastAPI()



@app.get('/result')
def emulate_external_server(cadastre_number: int,
                            latitude: float,
                            longitude: float):
    time.sleep(random.uniform(0, 2))
    response_data = {'response': random.choice([True, False])}
    return response_data


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8003)
