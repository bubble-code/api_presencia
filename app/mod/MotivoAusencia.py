from pydantic import BaseModel,ConfigDict

class MotivoAusencia(BaseModel):
    IDMotivo: str | None = None
    DescMotivo: str | None = None
    Computable: bool | None = None