
from sqlalchemy import text
from datetime import date,datetime
from app.db import engine
from app.mod.FichajeUpdate import FichajeUpdate

def get_fichajes(idOperario: str | None, fechaDesde: date, fechaHasta: date)->list[dict]:
    listResultSolmicro = []
    try: 
        query = text("""SELECT IDControlPresencia, IDDepartamento, DescDepartamento, IDOperario, DescOperario,
                     Fecha, Hora, Entrada, MotivoAusencia, DescMotivo, IDTipoTurno, DescTipoTurno,
                     TipoDia, TipoDiaEmpresa, Activo
                     FROM vGetDataPreseciaAPP
                     WHERE Fecha >= CONVERT(DATETIME, :fechaDesde + ' 00:00:00', 120)
                     AND Fecha <= CONVERT(DATETIME, :fechaHasta + ' 23:59:00', 120)
                     {condicion}
                     ORDER BY Fecha DESC""".replace("{condicion}", "AND IDOperario = :operario" if idOperario else ""))
        params = {
            "fechaDesde": fechaDesde.strftime("%Y-%m-%d"),
            "fechaHasta": fechaHasta.strftime("%Y-%m-%d")
            }
        if idOperario:
            operariosolmicro = idOperario.replace('FV', '').strip().zfill(3)
            params["operario"] = operariosolmicro

        with engine.connect() as connection:
            resultado = connection.execute(query,params).fetchall()
            listResultSolmicro = [
                                  {
                                    "IDControlPresencia": row[0],
                                    "IDDepartamento": row[1],
                                    "DescDepartamento": row[2],
                                    "IDOperario": row[3],
                                    "DescOperario": row[4],
                                    "Fecha": str(row[5]),
                                    "Hora": str(row[6]),
                                    "Entrada": row[7],
                                    "MotivoAusencia": row[8],
                                    "DescMotivo": row[9],
                                    "IDTipoTurno": row[10],
                                    "DescTipoTurno": row[11],
                                    "TipoDia": row[12],
                                    "TipoDiaEmpresa": row[13],
                                    "Activo": row[14]
                                    } for row in resultado
                                  ]
        return listResultSolmicro
    except Exception as e:
        print(f"Error al obtener los fichajes: {e}")
        return {"status": "error", "message": "Internal server error"}    


def insert_fichaje(data):
    try:
        query_get_idcontrolPresencia = text("SELECT ISNULL(MAX(IDControlPresencia), 0) + 1 AS NextID FROM tbControlPresencia")
        with engine.connect() as connection:
            idControlP = connection.execute(query_get_idcontrolPresencia).scalar()
        sql = text("""
            INSERT INTO tbControlPresencia
            (IDControlPresencia, IDOperario, Fecha, Hora, Entrada, MotivoAusencia,
             FechaCreacionAudi, FechaModificacionAudi, UsuarioAudi, UsuarioCreacionAudi)
            VALUES (:IDControlPresencia, :IDOperario, :Fecha, :Hora, :Entrada, :MotivoAusencia,
                    :FechaCreacionAudi, :FechaModificacionAudi, :UsuarioAudi, :UsuarioCreacionAudi)
        """)

        params = {
            "IDControlPresencia": idControlP,
            "IDOperario": data.IDOperario,
            "Fecha": data.Fecha.strftime("%Y-%d-%m 00:00:00"),
            "Hora": f"{data.Fecha.strftime('%Y-%d-%m')} {data.Hora}",
            "Entrada": data.Entrada,
            "MotivoAusencia": data.MotivoAusencia,
            "FechaCreacionAudi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "FechaModificacionAudi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "UsuarioAudi": data.Usuario,
            "UsuarioCreacionAudi": data.Usuario
        }

        with engine.connect() as connection:
            connection.execute(sql, params)
            connection.commit()

        return {"status": "ok", "message": "Fichaje insertado correctamente"}
    except Exception as e:
        print(f"Error al insertar fichaje: {e}")
        return {"status": "error", "message": "Error al insertar fichaje"}

def update_fichaje(data:FichajeUpdate):
    try:
        sql = text("""
            UPDATE tbControlPresencia
            SET IDOperario = :IDOperario,
                Fecha = :Fecha,
                Hora = :Hora,
                Entrada = :Entrada,
                MotivoAusencia = :MotivoAusencia,
                FechaModificacionAudi = :FechaModificacionAudi,
                UsuarioAudi = :UsuarioAudi
            WHERE IDControlPresencia = :IDControlPresencia
        """)

        params = {
            "IDControlPresencia": data.IDControlPresencia,
            "IDOperario": data.IDOperario,
            "Fecha": data.Fecha.strftime("%Y-%d-%m 00:00:00"),
            "Hora": f"{data.Fecha.strftime('%Y-%d-%m')} {data.Hora}",
            "Entrada": data.Entrada,
            "MotivoAusencia": data.MotivoAusencia,
            "FechaModificacionAudi": datetime.now().strftime("%Y-%d-%m %H:%M:%S"),
            "UsuarioAudi": data.Usuario
        }

        with engine.connect() as connection:
            result = connection.execute(sql, params)
            connection.commit()

        if result.rowcount == 0:
            return {"status": "error", "message": "Registro no encontrado"}
        return {"status": "ok", "message": f"Registro {data.IDControlPresencia} actualizado correctamente"}
    except Exception as e:
        print(f"Error al actualizar fichaje: {e}")
        return {"status": "error", "message": "Error al actualizar fichaje"}


