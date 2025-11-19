from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "profiles.json"

def _load():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def _save(profiles):
    DB_PATH.write_text(
        json.dumps(profiles, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def create_profile(profile_dict):
    profiles = _load()
    profiles.append(profile_dict)
    _save(profiles)

def read_profile():
    return _load()

def export_csv():
    path_csv = DATA_DIR / "profiles.csv"
    profiles = _load()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "name", "profile", "email",
                "logica", "criatividade", "colaboracao", "adaptabilidade",
                "stage", "created"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in profiles:
                # ensure keys exist (backwards compatibility)
                row = {
                    "name": p.get("name", ""),
                    "profile": p.get("profile", ""),
                    "email": p.get("email", ""),
                    "logica": p.get("logica", ""),
                    "criatividade": p.get("criatividade", ""),
                    "colaboracao": p.get("colaboracao", ""),
                    "adaptabilidade": p.get("adaptabilidade", ""),
                    "stage": p.get("stage", p.get("Stages", "")),
                    "created": p.get("created", p.get("Created", ""))
                }
                writer.writerow(row)
        return path_csv
    except PermissionError:
        # caso o arquivo esteja aberto e vc tente trocar o nome...
        return None
