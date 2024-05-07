from datetime import datetime
import uuid
import hashlib

def format_currency(value):
    """Formata um valor numérico como moeda."""
    return "${:,.2f}".format(value)

def validate_email(email):
    """Valida o formato do email."""
    import re
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

def print_debug_info(message):
    """Imprime informações de depuração no console, formatado de maneira específica."""
    print(f"DEBUG: {message}")

def get_uuid_string():
    """Gera uma string UUID."""
    import uuid
    return str(uuid.uuid4())

def generate_unique_zip_filename():
    """Gera um nome de arquivo único."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")
    
    hashed = hashlib.sha512(str(uuid.uuid4()).encode())
    hashed = hashed.hexdigest()

    name_unique_file = f'{timestamp}{hashed}'
    return name_unique_file + ".zip"