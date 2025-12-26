from enum import Enum

class PhotoStatus(str, Enum):
    BRUTA = "bruta"
    CATALOGADA = "catalogada"
    VALIDADA = "validada"

class Visibility(str, Enum):
    PUBLICA = "publica"
    RESTRITA = "restrita"
    PRIVADA = "privada"

class UserRole(str, Enum):
    ADMIN = "admin"
    CURADOR = "curador"
    COLABORADOR = "colaborador"

class ConsentType(str, Enum):
    VERBAL = "verbal"
    ESCRITO = "escrito"
    PUBLICO = "publico"
