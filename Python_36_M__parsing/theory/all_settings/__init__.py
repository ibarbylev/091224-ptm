import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Импорт основных настроек
try:
    from .settings import *
    logger.info("Основные настройки загружены из settings.py")
except ImportError as e:
    logger.error(f"Не удалось импортировать основные настройки: {e}")

# Переопределение настроек локальными, если они существуют
# (если и в settings, и в local_settings есть одинаковые имена,
# то последние перезапишут первых)
try:
    from .local_settings import *
    logger.info("Локальные настройки загружены из local_settings.py")
except ImportError as e:
    logger.warning(f"Локальные настройки не найдены: {e}")