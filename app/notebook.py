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
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return (f"date{self.creation_date}"
                f"{self.title}: {self.text}")


class Notebook:
    def __init__(self, notes: list[Note]):
        self.notes: list[Note] = notes

    def add_note(self, title: str, text: str, importance: str) -> int:
        new_code = len(self.notes) + 1
        new_note = Note(new_code, title, text, importance)
        self.notes.append(new_note)
        return new_code

    def delete_note(self, code: int):
        for note in self.notes:
            if note.code == code:
                self.notes.remove(note)
                return

    def important_notes(self) -> list[Note]:
        result = []
        for note in self.notes:
            if note.importance == Note.HIGH or note.importance ==  Note.MEDIUM:
                result.append(note)
            return result

    def notes_by_tag(self, tag: str) -> list[Note]:
        result = []
        for note in self.notes:
            for t in note.tags:
                if t == tag:
                    result.append(note)
        return result


    def tag_with_most_notes(self):
        pass








