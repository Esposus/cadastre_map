from fastapi import FastAPI
from sqladmin import Admin

from src.admin import QueryHistoryAdmin
from src.api import router
from src.database import engine
from src.settings import settings


app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(router=router)

admin = Admin(app, engine)
admin.add_view(QueryHistoryAdmin)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
