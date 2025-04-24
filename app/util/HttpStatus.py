class StatusResponse:
    def __init__(self, statusCode, message, description):
        self.statusCode = statusCode
        self.message = message
        self.description = description

class HttpstatusCode:
    # 1xx Informational responses
    @property
    def Continue(self):
        return StatusResponse(100, "Continue", "O servidor recebeu os cabeçalhos da requisição e o cliente deve continuar com a requisição.")
    
    @property
    def SwitchingProtocols(self):
        return StatusResponse(101, "Switching Protocols", "O servidor está mudando para o protocolo solicitado pelo cliente.")
    
    @property
    def Processing(self):
        return StatusResponse(102, "Processing", "O servidor recebeu a requisição, mas ainda não foi capaz de completá-la.")
    
    @property
    def EarlyHints(self):
        return StatusResponse(103, "Early Hints", "O servidor está começando a processar a requisição, mas ainda não tem uma resposta final.")
    
    # 2xx Success
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
    def NonAuthoritativeInformation(self):
        return StatusResponse(203, "Non-Authoritative Information", "O servidor retorna a resposta, mas a informação pode ser proveniente de uma fonte não confiável.")
    
    @property
    def NoContent(self):
        return StatusResponse(204, "No Content", "A requisição foi bem-sucedida, mas não há conteúdo para retornar.")
    
    @property
    def ResetContent(self):
        return StatusResponse(205, "Reset Content", "O servidor solicita ao cliente que reenvie a requisição sem qualquer conteúdo.")
    
    @property
    def PartialContent(self):
        return StatusResponse(206, "Partial Content", "O servidor está retornando uma parte do recurso solicitado, conforme solicitado.")
    
    # 3xx Redirection
    @property
    def MultipleChoices(self):
        return StatusResponse(300, "Multiple Choices", "A requisição tem várias respostas possíveis e o servidor não pode escolher uma delas.")
    
    @property
    def MovedPermanently(self):
        return StatusResponse(301, "Moved Permanently", "O recurso foi movido permanentemente para uma nova URL.")
    
    @property
    def Found(self):
        return StatusResponse(302, "Found", "O recurso foi encontrado, mas deve ser acessado por uma URL diferente.")
    
    @property
    def SeeOther(self):
        return StatusResponse(303, "See Other", "O servidor redireciona o cliente para um recurso diferente.")
    
    @property
    def NotModified(self):
        return StatusResponse(304, "Not Modified", "O recurso não foi modificado desde a última requisição.")
    
    @property
    def UseProxy(self):
        return StatusResponse(305, "Use Proxy", "O cliente deve usar um proxy para acessar o recurso.")
    
    @property
    def TemporaryRedirect(self):
        return StatusResponse(307, "Temporary Redirect", "O recurso solicitado foi temporariamente movido para uma nova URL.")
    
    @property
    def PermanentRedirect(self):
        return StatusResponse(308, "Permanent Redirect", "O recurso foi permanentemente movido para uma nova URL.")
    
    # 4xx Client Error
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
    def NotAcceptable(self):
        return StatusResponse(406, "Not Acceptable", "O servidor não pode gerar uma resposta que seja aceitável para o cliente.")
    
    @property
    def ProxyAuthenticationRequired(self):
        return StatusResponse(407, "Proxy Authentication Required", "O cliente deve se autenticar com o proxy.")
    
    @property
    def RequestTimeout(self):
        return StatusResponse(408, "Request Timeout", "O servidor não recebeu uma requisição completa dentro do tempo limite.")
    
    @property
    def Conflict(self):
        return StatusResponse(409, "Conflict", "A requisição não pôde ser concluída devido a um conflito com o estado atual do recurso.")
    
    @property
    def Gone(self):
        return StatusResponse(410, "Gone", "O recurso solicitado não está mais disponível e não há um novo endereço.")
    
    @property
    def LengthRequired(self):
        return StatusResponse(411, "Length Required", "O servidor exige que a requisição tenha um campo Content-Length.")
    
    @property
    def PreconditionFailed(self):
        return StatusResponse(412, "Precondition Failed", "A condição especificada na requisição foi avaliada como falsa pelo servidor.")
    
    @property
    def PayloadTooLarge(self):
        return StatusResponse(413, "Payload Too Large", "O corpo da requisição é maior do que o servidor está disposto ou pode processar.")
    
    @property
    def URITooLong(self):
        return StatusResponse(414, "URI Too Long", "A URI fornecida pela requisição é muito longa para ser processada pelo servidor.")
    
    @property
    def UnsupportedMediaType(self):
        return StatusResponse(415, "Unsupported Media Type", "O servidor não suporta o tipo de mídia da requisição.")
    
    @property
    def RangeNotSatisfiable(self):
        return StatusResponse(416, "Range Not Satisfiable", "O servidor não pode atender ao intervalo especificado no cabeçalho Range da requisição.")
    
    @property
    def ExpectationFailed(self):
        return StatusResponse(417, "Expectation Failed", "O servidor não pode atender à expectativa informada no cabeçalho Expect da requisição.")
    
    @property
    def IAmATeapot(self):
        return StatusResponse(418, "I'm a teapot", "O servidor é uma chaleira e se recusa a preparar café, conforme o protocolo de teapot.")
    
    @property
    def MisdirectedRequest(self):
        return StatusResponse(421, "Misdirected Request", "A requisição foi direcionada para um servidor que não pode processá-la.")
    
    @property
    def UnprocessableEntity(self):
        return StatusResponse(422, "Unprocessable Entity", "A requisição está bem formada, mas o servidor não pode processá-la.")
    
    @property
    def Locked(self):
        return StatusResponse(423, "Locked", "O recurso solicitado está bloqueado.")
    
    @property
    def FailedDependency(self):
        return StatusResponse(424, "Failed Dependency", "A requisição falhou devido a uma falha de dependência em outro recurso.")
    
    @property
    def TooEarly(self):
        return StatusResponse(425, "Too Early", "O servidor não está disposto a processar a requisição devido a uma condição antecipada.")
    
    @property
    def UpgradeRequired(self):
        return StatusResponse(426, "Upgrade Required", "O servidor exige que o cliente atualize o protocolo.")
    
    @property
    def PreconditionRequired(self):
        return StatusResponse(428, "Precondition Required", "O servidor exige que as condições sejam atendidas antes de processar a requisição.")
    
    @property
    def TooManyRequests(self):
        return StatusResponse(429, "Too Many Requests", "O cliente enviou muitas requisições em um dado período.")
    
    @property
    def RequestHeaderFieldsTooLarge(self):
        return StatusResponse(431, "Request Header Fields Too Large", "O servidor não pode processar a requisição devido aos cabeçalhos serem muito grandes.")
    
    @property
    def UnavailableForLegalReasons(self):
        return StatusResponse(451, "Unavailable For Legal Reasons", "O recurso solicitado não está disponível devido a razões legais.")
    
    # 5xx Server Error
    @property
    def InternalServerError(self):
        return StatusResponse(500, "Internal Server Error", "O servidor encontrou uma condição inesperada que impediu de atender à requisição.")
    
    @property
    def NotImplemented(self):
        return StatusResponse(501, "Not Implemented", "O servidor não suporta o método da requisição.")
    
    @property
    def BadGateway(self):
        return StatusResponse(502, "Bad Gateway", "O servidor, ao atuar como gateway, recebeu uma resposta inválida de um servidor upstream.")
    
    @property
    def ServiceUnavailable(self):
        return StatusResponse(503, "Service Unavailable", "O servidor está temporariamente incapaz de processar a requisição devido a manutenção ou sobrecarga.")
    
    @property
    def GatewayTimeout(self):
        return StatusResponse(504, "Gateway Timeout", "O servidor, ao atuar como gateway, não recebeu uma resposta a tempo de um servidor upstream.")
    
    @property
    def HTTPVersionNotSupported(self):
        return StatusResponse(505, "HTTP Version Not Supported", "O servidor não suporta a versão HTTP da requisição.")
    
    @property
    def VariantAlsoNegotiates(self):
        return StatusResponse(506, "Variant Also Negotiates", "O servidor tem um erro de configuração interna onde a negociação de conteúdo falhou.")
    
    @property
    def InsufficientStorage(self):
        return StatusResponse(507, "Insufficient Storage", "O servidor não tem espaço suficiente para completar a requisição.")
    
    @property
    def LoopDetected(self):
        return StatusResponse(508, "Loop Detected", "O servidor detectou um loop infinito ao processar a requisição.")
    
    @property
    def NotExtended(self):
        return StatusResponse(510, "Not Extended", "A requisição precisa de mais extensões para ser processada.")
    
    @property
    def NetworkAuthenticationRequired(self):
        return StatusResponse(511, "Network Authentication Required", "O cliente precisa se autenticar para obter acesso à rede.")
