
DB = {}


def _init_db():
    DB.clear()


def command_add(_id, first_name, last_name, birthday, phone_number):
    if _id in DB:
        return "ID " + str(_id) + " ja cadastrado."

    DB[_id] = {
        'fn': first_name,
        'ln': last_name,
        'bd': birthday,
        'pn': phone_number
    }
    return ""


def command_del(_id):
    try:
        DB.pop(_id)
        return ''
    except KeyError:
        return f'ID {_id} nao existente.'


def command_info(_id):
    try:
        data = DB[_id]
        return ' '.join(data.values())
    except KeyError:
        return f'ID {_id} nao existente.'


def command_query(query):
    # fn:Roberto
    result = []

    tag, data_value = query.split(':')
    for key, value in DB.items():
        if value[tag] == data_value:
            result.append(key)

    # result2 = []
    # for number in result:
    #     result2.append(str(number))
    # return ' '.join(result2)

    return ' '.join(str(number) for number in sorted(result))
