from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    database_url: SecretStr
    clave_secreta: SecretStr

    title_api:str = 'Mi nueva api'

    class Config:
        env_file = '.env'
    
settings = Settings()
print(settings)
