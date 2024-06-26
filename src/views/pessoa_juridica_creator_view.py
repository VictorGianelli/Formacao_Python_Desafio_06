
from src.controllers.interfaces.pessoa_juridica_creator_controller import PessoaJuridicaCreatorControllerInterface
from src.validators.pessoa_juridica_validator import pessoa_juridica_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaJuridicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_validator(http_request)
        
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
    