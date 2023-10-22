from fastapi import FastAPI
# from sqladmin import Admin as AdminSQL
from starlette_admin.contrib.sqla import Admin, ModelView

# from src.admin import QueryHistoryAdmin
from src.api import router
from src.database import engine
from src.settings import settings
from src.models import CadastreRequest


app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(router=router)

# admin_sql = AdminSQL(app, engine, title='Админка SQLAdmin')
# admin_sql.add_view(QueryHistoryAdmin)
admin = Admin(engine, title='Панель администратора')
admin.add_view(ModelView(CadastreRequest))
admin.mount_to(app)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
