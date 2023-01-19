from flask import Flask, render_template, request
from utils import *
from api.api import api_
from logger import get_logger

app = Flask(__name__, template_folder="templates")
app.register_blueprint(api_)
app.config['JSON_AS_ASCII'] = False
log = get_logger(__name__)

@app.route("/")
def main_page():
    """
        Отображение всех маршрутов электричек

                    Parameters:
                            -
                    Returns:
                            Response: html код
    """
    # логирование
    log.info("Загрузка главной страницы")
    return render_template("index.html", m=load_by_day())

@app.route("/search/")
def search_page():
    """
        Отображение маршрутов электричек по заданому номеру

                        Parameters:
                                s (str): номер электрички
                        Returns:
                                Response: html код
    """
    # Получение аргументов из адресной строки
    query = request.args.get('s')
    # логирование
    log.info(f"Загрузка страницы с маршрутами электрчки под номеров {query}")
    # Проверка данных которые мы получили не являются ли они строкой
    if type(load_by_number(query)) == str:
        return load_by_number(query)
    return render_template("search.html", m=load_by_number(query), number=query)

@app.errorhandler(404)
def error_404(e):
    """ Обработчик ошибки 404 """
    # логирование
    log.info("ошибка 404")
    return "<h2>Такой страницы не существуют</h2>", 404

@app.errorhandler(500)
def error_500(e):
    """ Обработчик ошибки 500 """
    # логирование
    log.info("ошибка 500")
    return "<h2>Произошла ошибка на сервере</h2>", 500

if __name__ == "__main__":
    app.run()