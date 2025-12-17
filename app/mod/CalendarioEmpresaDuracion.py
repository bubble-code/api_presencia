from pydantic import BaseModel,ConfigDict

class CalendarioEmpresaDuracion(BaseModel):
    Fecha: str | None = None
    TipoDia: str | None = None
    DescTipoDia: str | None = None
    IDTipoTurno: str | None = None
    DescTurno: str | None = None
    Duracion: str | None = None