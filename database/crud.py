from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm.session import Session
from .db_postgre import session
from .models import User, Note


def get_user(login: str, password: str) -> User:
    """
    Функция возвращает пользователя по Login и Password
    """


def get_user_by_id(id: int) -> User:
    """
    Функция возвращает пользователя по user_id
    """


def add_user(login: str, password: str):
    """
    Функция добавляет в базу нового пользователя с информацией login и password 
    """


def add_note(user_id: int, title: str, content: str):

    """
    Функция добавляет в базу новую заметку с Title и Content 

    Ничего не возвращает
    """


def get_note_by_id(note_id: int) -> Note|None:
    """
    Функция возращает одну заметку по note_id
    """


def get_all_notes_by_user(user_id):
    """
    Функция возвращает все заметки для определенного пользователя
    """


def update_note(note_id: int, title: str, content: str):
    """
    Функция берет заметку по note_id и обновляет ей Title и Content 
    """


def get_last_note_id():
    """
    Функция возвращает последний обновленную заметку
    
    """


def delete_note(note_id: int):
    """
    Функция удаляет заметку из базы по note_id

    Ничего не возвращает
    """


