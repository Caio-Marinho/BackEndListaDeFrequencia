from app.globals import  HttpstatusCode,Response,jsonify
from app.models.models import Discentes
from app.models import db
from app.util.Padronizar import padronizarEmail, padronizarNome
from .ValidatesTypes import TipagemEstaticaClasse, TipagemEstaticaFunction  # Tipagem estática personalizada
from .ValidatesData import ValidatesData  # Serviço de validação de dados
import json

http = HttpstatusCode()
@TipagemEstaticaClasse
class AdicionarDiscentes:
    """
    Classe responsável por adicionar novos discentes ao banco de dados.

    Esta classe lida com a validação, padronização e persistência de dados
    de discentes no banco de dados.
    """

    def __init__(self, discente: dict):
        """
        Inicializa a classe com os dados do discente.

        :param discente: Dicionário contendo os dados do discente a ser adicionado.
        """
        self.__discente = discente
        
    def validate(self) -> None:
        """
        Valida os dados do discente usando a classe ValidatesData.

        :raises ValueError: Se os dados do discente não forem válidos.
        """
        validates = ValidatesData(self.__discente)
        validates.validate()
        return validates
    
    def salvar(self) -> Response:
        """
        Salva o discente no banco de dados após validação e padronização.

        :return: Um objeto Response do Flask indicando o sucesso ou falha da operação.
        """
        try:
            # Cria uma instância do modelo Discentes com os dados fornecidos
            discente: Discentes = Discentes(**self.__discente)
            # Padroniza o nome e o email do discente
            discente.setnome(padronizarNome(discente.getnome()))
            discente.setemail(padronizarEmail(discente.getemail()))
            # Valida os dados do discente
            self.validate()
            # Adiciona e comita o discente no banco de dados
            db.session.add(discente)
            db.session.commit()
            # Retorna uma resposta de sucesso
            response: Response = jsonify({"Success": discente.to_json()})
            response.status_code = http.CREATED.statusCode
            return response
        except Exception as e:
            # Realiza rollback em caso de erro
            db.session.rollback()
            # Retorna uma resposta de falha
            response: Response = jsonify({"Fail": json.loads(str(e))})
            response.status_code = http.BadRequest.statusCode
            return response
        finally:
            # Remove a sessão para garantir que ela seja limpa corretamente
            db.session.remove()
