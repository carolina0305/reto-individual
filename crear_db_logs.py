import sqlite3

DB_PATH = "reto_carolina.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Crear la tabla LOGS si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LOGS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evento TEXT NOT NULL
    )
    """)

    # Limpiar la tabla para asegurar exactamente 30 registros (opcional)
    cursor.execute("DELETE FROM LOGS")

    # 30 eventos inventados
    eventos = [
        "Inicio de sesión de usuario admin",
        "Creación de perfil de usuario",
        "Eliminación de archivo temporal",
        "Actualización de configuración",
        "Error de conexión al servidor",
        "Respaldo automático completado",
        "Subida de imagen a galería",
        "Descarga de informe mensual",
        "Registro de nuevo comentario",
        "Exportación de datos a CSV",
        "Importación de contactos",
        "Cambio de contraseña solicitado",
        "Autenticación de dos factores activada",
        "Restablecimiento de sesión expirado",
        "Generación de token de API",
        "Correo de verificación enviado",
        "Notificación push entregada",
        "Sincronización con servicio externo",
        "Actualización de permisos de usuario",
        "Creación de copia de seguridad manual",
        "Lectura de fichero de configuración",
        "Tiempo de ejecución excedido",
        "Validación de formulario fallida",
        "Conexión WebSocket establecida",
        "Desbordamiento de buffer detectado",
        "Registro de actividad nocturna",
        "Optimización de base de datos programada",
        "Escaneo de seguridad completado",
        "Reinicio programado del servicio",
        "Aprobación de solicitud pendiente"
    ]

    # Insertar los eventos
    cursor.executemany("INSERT INTO LOGS (evento) VALUES (?)", [(e,) for e in eventos])

    conn.commit()
    inserted = cursor.execute("SELECT COUNT(*) FROM LOGS").fetchone()[0]
    conn.close()

    print(f"Base de datos '{DB_PATH}' creada/actualizada. Registros en LOGS: {inserted}")

if __name__ == "__main__":
    main()
