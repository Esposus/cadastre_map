from sqladmin import ModelView
from .models import CadastreRequest


class QueryHistoryAdmin(ModelView, model=CadastreRequest):
    column_list = [
        CadastreRequest.cadastre_number,
        CadastreRequest.latitude,
        CadastreRequest.longitude,
        CadastreRequest.result,
        CadastreRequest.timestamp,
        CadastreRequest.id
    ]
    name = 'История запросов'
    name_plural = 'Истории запросов'
    column_labels = {
        CadastreRequest.cadastre_number: 'Кадастровый номер',
        CadastreRequest.latitude: 'Широта',
        CadastreRequest.longitude: 'Долгота',
        CadastreRequest.result: 'Ответ',
        CadastreRequest.timestamp: 'Дата',
        CadastreRequest.id: 'Id',
    }
