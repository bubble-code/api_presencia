from pydantic import BaseModel,ConfigDict

class OperarioActivo(BaseModel):
    IDOperario: str | None = None
    DescOperario: str | None = None
    IDDepartamento: str | None = None
    DescDepartamento: str | None = None
    Activo: bool | None = None