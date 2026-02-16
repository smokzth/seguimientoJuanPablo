# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH : str  = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW : str = "LOW"

    def __int__(self, code: str, title: str, text: str, importance: str, creation_date: datetime ):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []

    def add_tags(self, tag: list[str]):
        self.tags.append(tag)

    def __str__(self) -> str:
        return (f"date{self.creation_date}"
                f"{self.title}: {self.text}")


class Notebook:
    def __init__(self, notes: list[Note]):
        self.notes: list[Note] = notes

    def add_note(self, title: str, text: str, importance: str) -> int:







