
from bazinga.infra import Route
from bazinga.handlers import hello_world

routes = [
    Route(verb='GET', path='/',
          handlers=[hello_world.get_hello_world_message])
]