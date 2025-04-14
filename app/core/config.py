import secrets
from typing import Any, List, Optional, Union  # Dict

from pydantic import AnyHttpUrl, ValidationInfo  # field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API相关设置
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str = "NodePanel"

    # CORS设置
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # 数据库设置
    MYSQL_SERVER: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "your_password"
    MYSQL_DB: str = "node_panel"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # @field_validator("SQLALCHEMY_DATABASE_URI", mode='before')
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        # 在V2中使用info.data而不是values
        data = info.data
        return f"mysql+aiomysql://{data.get('MYSQL_USER')}:{data.get('MYSQL_PASSWORD')}@{data.get('MYSQL_SERVER')}:{data.get('MYSQL_PORT')}/{data.get('MYSQL_DB')}"

    # @field_validator("BACKEND_CORS_ORIGINS", mode='before')
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # 安全设置
    ALGORITHM: str = "HS256"  # JWT加密算法

    # 应用设置
    DEBUG: bool = False  # 调试模式
    TIMEZONE: str = "Asia/Shanghai"  # 时区

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"  # 忽略未定义的环境变量


# 创建全局设置对象
settings = Settings()
