from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.region_route import region_bp
    from .orders.city_route import city_bp

    app.register_blueprint(region_bp)
    app.register_blueprint(city_bp)
