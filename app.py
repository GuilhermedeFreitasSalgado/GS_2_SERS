from stages import Profile
import repo

def input_int_in_range(prompt, min_val=0, max_val=5):
    while True:
        try:
            v = int(input(prompt).strip())
            if v < min_val or v > max_val:
                print(f"Digite um número entre {min_val} e {max_val}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def add_profile():
    name = input("Nome: ").strip()
    profile_type = input("Perfil (ex: desenvolvedor, designer, etc): ").strip()
    email = input("E-mail: ").strip()

    print("\nAgora informe suas competências (0 a 5):")
    logica = input_int_in_range("Lógica (0-5): ")
    criatividade = input_int_in_range("Criatividade (0-5): ")
    colaboracao = input_int_in_range("Colaboração (0-5): ")
    adaptabilidade = input_int_in_range("Adaptabilidade (0-5): ")

    skills = {
        "logica": logica,
        "criatividade": criatividade,
        "colaboracao": colaboracao,
        "adaptabilidade": adaptabilidade
    }

    profile = Profile(name, profile_type, email, skills)
    repo.create_profile(profile.to_dict())
    print("Perfil adicionado.\n")

def list_profiles():
    profiles = repo.read_profile()
    if not profiles:
        print("Nenhum perfil cadastrado")
        return

    header = f"\n## | {'Nome':<20} | {'Perfil':<15} | {'E-mail':<25} | L | Crea | Colab | Adapt |"
    print(header)
    for i, p in enumerate(profiles):
        name = p.get("name", "")
        perfil = p.get("profile", "")
        email = p.get("email", "")
        l = p.get("logica", "")
        c = p.get("criatividade", "")
        col = p.get("colaboracao", "")
        a = p.get("adaptabilidade", "")
        print(f"{i:02d} | {name:<20} | {perfil:<15} | {email:<25} | {l!s:^1} | {c!s:^4} | {col!s:^5} | {a!s:^5}")

def search_profile():
    user_search = input("Buscar por (nome/perfil/email): ").strip().lower()
    if not user_search:
        print("Consulta vazia")
        return

    profiles = repo.read_profile()
    results = []
    for profile in profiles:
        profile_str = f"{profile.get('name','')} {profile.get('profile','')} {profile.get('email','')}".lower()
        if user_search in profile_str:
            results.append(profile)

    if not results:
        print("Nenhum perfil encontrado")
        return

    print(f"\n## | {'Nome':<20} | {'Perfil':<15} | {'E-mail':<25}")
    for i, p in enumerate(results):
        print(f"{i:02d} | {p.get('name',''):<20} | {p.get('profile',''):<15} | {p.get('email',''):<25}")

def recommend_from_skills(skills):
    """
    Recomendador simples baseado em regras:
    regra: se logica alta -> carreiras técnicas; criatividade alta -> design/marketing; colaboração+adaptabilidade -> papéis de produto/gestão
    """
    recs = []
    l = skills.get("logica", 0)
    cr = skills.get("criatividade", 0)
    co = skills.get("colaboracao", 0)
    ad = skills.get("adaptabilidade", 0)

    if l >= 4:
        recs.append("Desenvolvedor / Eng. de Dados / Engenharia")
    if cr >= 4:
        recs.append("Design (UX/UI) / Marketing Criativo")
    if co >= 4 and ad >= 4:
        recs.append("Gerente de Produto / Scrum Master / Customer Success")
    # recomendações complementares
    if l >= 3 and cr >= 3:
        recs.append("Full-stack / Projetos interdisciplinares")
    if not recs:
        recs.append("Trilhas: lógica, colaboração; considerar cursos básicos de programação e comunicação")

    return recs

def recommend_profile():
    profiles = repo.read_profile()
    if not profiles:
        print("Nenhum perfil cadastrado")
        return
    list_profiles()
    try:
        idx = int(input("Escolha o índice do perfil para gerar recomendações: ").strip())
    except ValueError:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(profiles):
        print("Índice fora do intervalo.")
        return
    p = profiles[idx]
    skills = {
        "logica": int(p.get("logica", 0)),
        "criatividade": int(p.get("criatividade", 0)),
        "colaboracao": int(p.get("colaboracao", 0)),
        "adaptabilidade": int(p.get("adaptabilidade", 0))
    }
    recs = recommend_from_skills(skills)
    print("\nRecomendações personalizadas:")
    for r in recs:
        print(f"- {r}")

def export_profiles():
    path_csv = repo.export_csv()
    if path_csv is None:
        print("Erro na exportação... Feche o arquivo CSV se ele estiver aberto e tente novamente.")
    else:
        print(f"Perfis exportados para: {path_csv}")

def print_menu():
    print("\nMini CRM de perfis - (Adicionar / listar / recomendar)")
    print("[1] Adicionar perfil")
    print("[2] Listar perfis")
    print("[3] Buscar perfis por (nome/perfil/email)")
    print("[4] Exportar perfis como CSV")
    print("[5] Gerar recomendações para um perfil")
    print("[0] Sair")

def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            add_profile()
        elif op == "2":
            list_profiles()
        elif op == "3":
            search_profile()
        elif op == "4":
            export_profiles()
        elif op == "5":
            recommend_profile()
        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
