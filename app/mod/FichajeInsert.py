
from pydantic import BaseModel, field_validator
from datetime import datetime, date

class FichajeInsert(BaseModel):
    IDControlPresencia: int | None=None
    IDOperario: str
    Fecha: date
    Hora: str
    Entrada: int
    MotivoAusencia: str | None = None
    Usuario: str

    @field_validator("Fecha", mode="before")
    def parse_fecha(cls, value):
        if isinstance(value, date):
            return value
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use dd/MM/yyyy (ej: 02/12/2025)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "IDOperario": "167",
                "Fecha": "03/12/2025",
                "Hora": "10:00:00",
                "Entrada": 0,
                "MotivoAusencia": "14",
                "Usuario": "favram\\a.obregon",
            }
        }
    }
