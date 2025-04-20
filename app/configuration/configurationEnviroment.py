from dotenv import load_dotenv
def gerar_env_automatico(config_class):
    load_dotenv()
    
    env_lines = []

    # Iterar sobre os atributos da classe
    for chave, valor in config_class.items():
            env_lines.append(f"{chave}={valor}")
    # Escrever no arquivo .env
    with open(".env", "w") as env_file:
        env_file.write("\n".join(env_lines))

