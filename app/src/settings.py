from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Кадастровигатор'
    description: str = (
        'Этот сервис позволяет проверить местоположение объекта'
        'с указанным кадастровым номером на карте, зная его широту и долготу'
    )
    database_url: str = 'sqlite:///./cadastre.db'
    model_config = ConfigDict(_env_file='.env')


settings = Settings()
