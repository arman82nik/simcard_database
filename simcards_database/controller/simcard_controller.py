import re
from model.service.simcard_service import save_simcard


def save(number,owner,register_data,operator,charge):
    try:
        if re.match(r"^09[\d]{12}$",number):
            return save_simcard(number,owner,register_data,operator,charge)
        else:
            return "error"
    except Exception as e:
            return f"error {e}"