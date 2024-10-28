from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

def main(): 
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuario.

    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    #Função para armazenar os dados digitado acima
    service.criar_usuario(nome=nome, email=email, senha=senha)

    #Listar todos os usuarios cadastrados
    print("\nListando usuários cadastrados.")
    listar_usuario = service.listar_todos_usuarios()
    for usuario in listar_usuario:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


if __name__ == "__main__":
    main()