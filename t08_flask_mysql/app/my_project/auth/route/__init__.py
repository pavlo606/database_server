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
    from .orders.busstops_route import busstops_bp
    from .orders.passangers_route import passangers_bp
    from .orders.drivers_route import drivers_bp
    from .orders.buses_route import buses_bp
    from .orders.routes_route import routes_bp
    from .orders.subroute_route import subroutes_bp
    from .orders.ticket_route import ticket_bp

    app.register_blueprint(region_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(busstops_bp)
    app.register_blueprint(passangers_bp)
    app.register_blueprint(drivers_bp)
    app.register_blueprint(buses_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(subroutes_bp)
    app.register_blueprint(ticket_bp)
