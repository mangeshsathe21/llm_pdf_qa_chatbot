from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    upload_dir : str = 'uploads'
    allowed_filetypes : set = {'application/pdf', 'text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
    max_file_size : int = 40
    
    class Config:
        env_file = ".env"

settings = Settings()