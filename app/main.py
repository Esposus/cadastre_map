from fastapi import FastAPI
from sqladmin import Admin, ModelView

from src.api import router
from src.database import engine
from src.models import Request


app = FastAPI()

app.include_router(router=router)

admin = Admin(app, engine)


class QueryHistoryAdmin(ModelView, model=Request):
    column_list = [
        Request.cadastre_number, Request.latitude, Request.longitude
    ]
    name = 'История запросов'
    name_plural = 'Истории запросов'
    column_labels = {
        Request.cadastre_number: 'Кадастровый номер',
        Request.latitude: 'Широта',
        Request.longitude: 'Долгота',
    }


admin.add_view(QueryHistoryAdmin)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
