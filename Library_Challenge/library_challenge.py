from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Book:

    id: int
    title: str
    author: str
    tags: list[str] = field(default_factory=list)


class BookNotFoundError(Exception):
    pass


class Library:

    def __init__(self):
        self._books: dict[int, Book] = {}
        self._next_id = 1

    def add_book(
        self, title: str, author: str, tags: Optional[list[str]] = None
    ) -> Book:
        book = Book(
            id=self._next_id,
            title=title,
            author=author,
            tags=tags or [],
        )
        self._books[book.id] = book
        self._next_id += 1
        return book

    def get_book(self, book_id: int) -> Book:
        try:
            return self._books[book_id]
        except KeyError:
            raise BookNotFoundError(f"Livro com id {book_id} não encontrado.")

    def list_books(self) -> list[Book]:
        return list(self._books.values())

    def delete_book(self, book_id: int) -> None:
        print(self._books)
        if book_id not in self._books:
            raise BookNotFoundError(f"Livro com id {book_id} não encontrado.")
        del self._books[book_id]

    def update_book(
        self,
        book_id: int,
        title: Optional[str] = None,
        author: Optional[str] = None,
        tags: Optional[list[str]] = None,
    ) -> Book:
        book = self.get_book(book_id)

        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if tags is not None:
            book.tags = tags

        return book


lib = Library()

livro1 = lib.add_book("Dom Casmurro", "Machado de Assis", ["clássico", "romance"])
livro2 = lib.add_book("1984", "George Orwell", ["ficção", "distopia"])

lib.list_books()
lib.get_book(livro1.id)
lib.update_book(livro1.id, title="Dom Casmurro (revisado)")
lib.delete_book(livro2.id)
