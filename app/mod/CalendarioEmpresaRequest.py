from pydantic import BaseModel, field_validator
from datetime import datetime,date

class CalendarioEmpresaRequest(BaseModel):
    fechaDesde: date
    fechaHasta: date

    @field_validator("fechaDesde", "fechaHasta", mode="before")
    def parse_fecha(cls, value):
        if isinstance(value, date):
            return value
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use dd/MM/yyyy (ej: 02/12/2025)")        
    
    model_config = {
                    "json_schema_extra": {
                        "examples": [
                            {
                             "fechaDesde": "01/10/2025",
                             "fechaHasta": "31/12/2025"
                             }
                            ]
                        }
                    }
