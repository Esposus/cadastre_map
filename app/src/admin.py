from sqladmin import ModelView
from .models import Request


class QueryHistoryAdmin(ModelView, model=Request):
    column_list = [
        Request.cadastre_number,
        Request.latitude,
        Request.longitude,
        Request.response,
        Request.timestamp,
        Request.id
    ]
    name = 'История запросов'
    name_plural = 'Истории запросов'
    column_labels = {
        Request.cadastre_number: 'Кадастровый номер',
        Request.latitude: 'Широта',
        Request.longitude: 'Долгота',
        Request.response: 'Ответ',
        Request.timestamp: 'Дата',
        Request.id: 'Id',
    }
