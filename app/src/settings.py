from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Кадастровигатор'
    description: str = (
        'Этот сервис позволяет увидеть местоположение объекта'
        'с указанным кадастровым номером на карте, зная его широту и долготу'
    )
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
