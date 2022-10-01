import typing

from pydantic import BaseSettings

LogLevel = typing.Literal["TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class AppConfig(BaseSettings):
    log_level: LogLevel = "TRACE"
    structured_logging: bool = False


app_config = AppConfig()
print(app_config)


class LogConfig:
    level: LogLevel = app_config.log_level
    structured: bool = app_config.structured_logging
