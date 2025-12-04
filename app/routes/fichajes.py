from fastapi import APIRouter,HTTPException
from app.services.fichajes_services import get_fichajes,update_fichaje
from app.mod.FichajesRequest import FichajesRequest
from app.mod.FichajeSolmicro import FichajeSolmicro
from app.mod.FichajeUpdate import FichajeUpdate


router = APIRouter()
    
@router.post("/getFichajes",response_model=list[FichajeSolmicro], 
             summary="Obtiene los fichajes filtrados por fecha y operario o todos",
             description=f"""\n
             Obtiene los fichajes filtrando por operario y rango de fechas.\n 
             Si el operario se pasa vacio, devuelve los registros de todos lo operarios\n
             las fechas son obligatorias  """)
def get_fichajes_endPoint(data:FichajesRequest):
    try:
        result = get_fichajes(data.idoperario,data.fechaDesde,data.fechaHasta)
        return result
    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error interno {str(ex)}") 
    

from app.mod.FichajeInsert import FichajeInsert
from app.services.fichajes_services import insert_fichaje

@router.post("/insertarFichaje",
    summary="Inserta un fichaje",
    description="""Inserta un registro en presencia\n
    usando formato de fecha d/m/a\n
    Datos Obligatorios: idOperario, fecha, Hora en formato H/m/s, Entrada es 1 ó 0, MotivoAusencia, Usuario"""    
)
def insert_fichaje_endpoint(data: FichajeInsert):
    try:
        result = insert_fichaje(data)
        return result
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error interno {str(ex)}")

@router.put(
    "/updateFichaje",
    summary="Actualizar fichaje",
    description="Actualiza un fichaje"   
)
def update_fichaje_endpoint(data: FichajeUpdate):
    try:
        result = update_fichaje(data)
        return result
    except Exception as ex:
        print(str(ex))
        raise HTTPException(status_code=500, detail=f"Error interno {str(ex)}")

