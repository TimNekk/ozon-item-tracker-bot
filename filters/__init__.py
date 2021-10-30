from loader import dp
from .allowed import IsAllowed


if __name__ == "filters":
    dp.filters_factory.bind(IsAllowed)
