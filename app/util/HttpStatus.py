class StatusResponse:
    def __init__(self, statusCode, message, description):
        self.statusCode = statusCode
        self.message = message
        self.description = description

class HttpstatusCode:
    @property
    def OK(self):
        return StatusResponse(200, "OK", "A requisição foi bem-sucedida e a resposta contém os dados solicitados.")
    
    @property
    def Created(self):
        return StatusResponse(201, "Created", "O recurso foi criado com sucesso.")
    
    @property
    def Accepted(self):
        return StatusResponse(202, "Accepted", "A requisição foi aceita para processamento, mas ainda não foi completada.")
    
    @property
    def NoContent(self):
        return StatusResponse(204, "No Content", "A requisição foi bem-sucedida, mas não há conteúdo para retornar.")
    
    @property
    def BadRequest(self):
        return StatusResponse(400, "Bad Request", "A requisição não pôde ser processada devido à sintaxe inválida.")
    
    @property
    def Unauthorized(self):
        return StatusResponse(401, "Unauthorized", "A requisição requer autenticação.")
    
    @property
    def Forbidden(self):
        return StatusResponse(403, "Forbidden", "O servidor compreende a requisição, mas se recusa a autorizá-la.")
    
    @property
    def NotFound(self):
        return StatusResponse(404, "Not Found", "O recurso solicitado não foi encontrado no servidor.")
    
    @property
    def MethodNotAllowed(self):
        return StatusResponse(405, "Method Not Allowed", "O método especificado na requisição não é permitido para o recurso solicitado.")
    
    @property
    def Conflict(self):
        return StatusResponse(409, "Conflict", "A requisição não pôde ser concluída devido a um conflito com o estado atual do recurso.")
    
    @property
    def InternalServerError(self):
        return StatusResponse(500, "Internal Server Error", "O servidor encontrou uma condição inesperada que impediu de atender à requisição.")
    
    @property
    def ServiceUnavailable(self):
        return StatusResponse(503, "Service Unavailable", "O servidor está temporariamente incapaz de processar a requisição devido a manutenção ou sobrecarga.")