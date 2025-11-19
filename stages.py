from datetime import date

class Profile:
    """
    Classe simples que representa um perfil com algumas skills.
    """
    def __init__(self, name: str, profile_type: str, email: str, skills: dict = None, stage: str = "novo", created: str = None):
        self.name = name
        self.profile = profile_type
        self.email = email
        # skills: dict with keys 'logica','criatividade','colaboracao','adaptabilidade' values 0-5
        default_skills = {"logica": 0, "criatividade": 0, "colaboracao": 0, "adaptabilidade": 0}
        self.skills = {**default_skills, **(skills or {})}
        self.stage = stage
        self.created = created or date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "profile": self.profile,
            "email": self.email,
            "logica": self.skills["logica"],
            "criatividade": self.skills["criatividade"],
            "colaboracao": self.skills["colaboracao"],
            "adaptabilidade": self.skills["adaptabilidade"],
            "stage": self.stage,
            "created": self.created
        }
