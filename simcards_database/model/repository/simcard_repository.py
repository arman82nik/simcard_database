from model.repository.database_manager import transaction_manager

def save(number,owner,register_data,operator,charge):
    return transaction_manager(
        "insert into simcards (number,owner,register_data,operator,charge) values (?,?,?,?,?)",
        [number,owner,register_data,operator,charge],
        commit=True

    )

def edit(number,owner,register_data,operator,charge):
    return transaction_manager(
        "",
        [number,owner,register_data,operator,charge],
        commit=True
    )

def remove(id):
    return transaction_manager(

        ""
        "delete from simcards where id = ?",
        [id],
    )


def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass