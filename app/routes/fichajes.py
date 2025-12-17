from datetime import date, datetime
from fastapi import APIRouter,HTTPException, Query
from app.mod.CalendarioEmpresaRequest import CalendarioEmpresaRequest
from app.mod.CalendarioEmpresaDuracion import CalendarioEmpresaDuracion
from app.mod.MotivoAusencia import MotivoAusencia
from app.mod.OperarioActivo import OperarioActivo
from app.services.fichajes_services import get_calendario_empresa, get_fichajes, get_operarios_motivos_ausencias,update_fichaje,get_operarios_activos
from app.mod.FichajesRequest import FichajesRequest
from app.mod.FichajeSolmicro import FichajeSolmicro
from app.mod.FichajeUpdate import FichajeUpdate
from app.mod.FichajeInsert import FichajeInsert
from app.services.fichajes_services import insert_fichaje

router = APIRouter()
    
#region Peticion GET
@router.get("/getOperariosActivos",response_model=list[OperarioActivo], 
             summary="Lista todos los operarios activos",
             description=f"""\n
             Lista todos los operarios activos""")
def get_operarios_activos_endPoint():
    try:
        result = get_operarios_activos()
        return result
    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error interno {str(ex)}") 

@router.get("/getMotivosAusencias",response_model=list[MotivoAusencia], 
             summary="Lista los motivos de ausencias",
             description=f"""\n
             Lista los motivos de ausencias""")
def get_operarios_motivos_ausencias_endPoint():
    try:
        result = get_operarios_motivos_ausencias()
        return result
    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error interno {str(ex)}") 
    
 
 
def _parse_ddmmyyyy(value: str) -> date:
    try:
        return datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="Formato de fecha inválido. Use dd/MM/yyyy (ej: 02/12/2025)"
        )
   
    
@router.get("/getCalendarioEmpresa",response_model=list[CalendarioEmpresaDuracion], 
             summary="Lista el calendario de la empresa",
             description=f"""\n
             Lista el calendario de la empresa filtrado por el rango de fechas incluyendo ambos días.\n
             Fecha desde y fecha hasta son obligatorias""")
def get_calendario_empresa_endPoint(
fechaDesde: str = Query(..., description="Fecha inicio (dd/MM/yyyy)", examples=["01/10/2025"]),
    fechaHasta: str = Query(..., description="Fecha fin (dd/MM/yyyy)", examples=["31/12/2025"]),
):
    try:
        fd = _parse_ddmmyyyy(fechaDesde)
        fh = _parse_ddmmyyyy(fechaHasta)
        return get_calendario_empresa(fd, fh)
    
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error interno {str(ex)}") 

#endregion

#region Peticion POST
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

#endregion

#region Peticiones PUT
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

#endregion
