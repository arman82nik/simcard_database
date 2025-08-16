from model.repository.simcard_repository import *

def save_simcard(number,owner,register_data,operator,charge):
    if register_data is None:
        return save(number,owner,register_data,operator,charge)
    else:
        raise Exception("error")