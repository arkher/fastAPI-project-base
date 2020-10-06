from bazinga.infra.handler import Request, Response


async def get_hello_world_message(request: Request, response: Response, handlers):
    '''
    `hello_world` retorna a mensagem "Hello World.
    '''

    message = {'message': f"Hello, {request.body.get('nome', 'World')}"}

    await response.status(200).send(message)