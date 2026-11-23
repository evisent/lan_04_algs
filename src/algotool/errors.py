class AlgoError(Exception):
    """Базовое исключение пакета"""


class QueueEmptyError(AlgoError, IndexError):
    """Операция над пустой очередью"""