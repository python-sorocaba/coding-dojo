import pytest
from commands import command_add, command_del, command_info, command_query, DB, _init_db


@pytest.fixture
def roberto():
    return [
        123,
        'Roberto',
        'Nascimento',
        '01/01/1960',
        '+55-21-0190-0190'
    ]


@pytest.fixture
def rosangela():
    return [
        456,
        'Rosangela',
        'Nascimento',
        '01/01/1960',
        '+55-21-0190-0190'
    ]


def test_command_add(roberto):
    _init_db()
    assert command_add(*roberto) == ''


def test_command_add_values(roberto):
    _init_db()
    roberto[0] = 124
    command_add(*roberto)
    assert len(DB) == 1


def test_command_add_id(roberto):
    _init_db()
    roberto[0] = 125
    command_add(*roberto)
    assert 125 in DB


def test_command_add_same(roberto):
    _init_db()
    assert command_add(*roberto) == ''
    assert command_add(*roberto) == 'ID 123 ja cadastrado.'


def test_command_del(roberto):
    _init_db()
    command_add(*roberto)
    assert command_del(123) == ''


def test_command_del_not_found_id():
    _init_db()
    assert command_del(123) == 'ID 123 nao existente.'


def test_command_del_2(roberto):
    _init_db()
    command_add(*roberto)
    assert command_del(123) == ''
    assert command_del(123) == 'ID 123 nao existente.'


def test_command_info(roberto):
    _init_db()
    command_add(*roberto)
    assert command_info(roberto[0]) == 'Roberto Nascimento 01/01/1960 +55-21-0190-0190'


def test_command_info_not_found():
    _init_db()
    assert command_info(1) == 'ID 1 nao existente.'


def test_command_query(roberto):
    _init_db()
    command_add(*roberto)
    assert command_query('fn:Roberto') == '123'


def test_command_query_multiple(roberto, rosangela):
    _init_db()
    command_add(*roberto)
    command_add(*rosangela)
    assert command_query('ln:Nascimento') == '123 456'


def test_command_query_multiple_unordered(roberto, rosangela):
    _init_db()
    command_add(*rosangela)
    command_add(*roberto)
    assert command_query('ln:Nascimento') == '123 456'
