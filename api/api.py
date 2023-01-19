from flask import jsonify, Blueprint
from utils import *
from logger import get_logger

api_ = Blueprint("api", __name__, url_prefix="/api/")
log = get_logger(__name__)


@api_.route("routes/")
@api_.route("routes")
def all_routes():
    """
        Возвращает все маршруты электрички в формате json

                        Parameters:
                                -
                        Returns:
                                result (json): список всех маршрутов в формате json
        """
    # загрузка всех маршрутов
    routes = load_by_day()
    # логирование
    log.info("загрузка api со всеми данными")
    return jsonify(routes)


@api_.route("routes/<int:number>")
@api_.route("routes/<int:number>/")
def exact_route(number):
    """
        Возвращает все маршруты электрички по ее номеру в списке в формате json

                        Parameters:
                                number (int): номер электрички
                        Returns:
                                result (json): маршрут по заданому номер в формате json
        """
    # загрузка маршрута по номеру
    routes = load_by_pk(number)
    # логирование
    log.info(f"загрузка api данными номер {number}")
    return jsonify(routes)
