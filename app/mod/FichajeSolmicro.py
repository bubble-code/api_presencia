
from pydantic import BaseModel,ConfigDict

class FichajeSolmicro(BaseModel):
    IDControlPresencia: int | None = None
    IDDepartamento: str | None = None
    DescDepartamento: str | None = None
    IDOperario: str | None = None
    DescOperario: str | None = None
    Fecha: str | None = None
    Hora: str | None = None
    Entrada: bool | None = None
    MotivoAusencia: str | None = None
    DescMotivo: str | None = None
    IDTipoTurno: str | None = None
    DescTipoTurno: str | None = None
    TipoDia: int | None = None
    TipoDiaEmpresa: int | None = None
    Activo: bool | None = None
    
    
    # model_config = ConfigDict(
    #     json_schema_extra={
    #         "example": {
    #             "IDControlPresencia": 89290496,
    #             "IDDepartamento": "004",
    #             "DescDepartamento": "Oficina",
    #             "IDOperario": "053",
    #             "DescOperario": "LOPEZ LOPEZ, ARANZAZU MARIA",
    #             "Fecha": "03/12/2025",
    #             "Hora": "03/12/2025 07:00:00.533000",
    #             "Entrada": True,
    #             "MotivoAusencia": None,
    #             "DescMotivo": None,
    #             "IDTipoTurno": "M",
    #             "DescTipoTurno": "Turno de mañana",
    #             "TipoDia": 0,
    #             "TipoDiaEmpresa": 0,
    #             "Activo": True
    #         }
    #     }
    # )
