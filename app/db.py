
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from app.config import settings

odbc_str = (
    f"DRIVER={{{settings.DB_ODBC_DRIVER}}};"
    f"SERVER={settings.DB_SERVER};"
    f"DATABASE={settings.DB_NAME};"
    f"UID={settings.DB_USER};"
    f"PWD={settings.DB_PASSWORD};"
    f"Encrypt={settings.DB_ENCRYPT};"
    f"TrustServerCertificate={settings.DB_TRUST_CERT};"
)

connect_url = f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}"
engine = create_engine(connect_url, pool_pre_ping=True, future=True)
