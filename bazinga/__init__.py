__version__ = '0.1.0'

from bazinga.infra.app import App

from bazinga.routes import routes

app = App(routes)