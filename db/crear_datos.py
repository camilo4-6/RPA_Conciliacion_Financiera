import sqlite3

# Usamos tu ruta absoluta exacta para evitar crear duplicados
ruta_db = r"E:\Programacion\RPA_Conciliacion_Financiera\db\datos_empresa.db"
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Borramos la tabla anterior para empezar limpios
cursor.execute('DROP TABLE IF EXISTS facturas_pendientes')

# Creamos la tabla
cursor.execute('''
CREATE TABLE facturas_pendientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nit_cliente TEXT NOT NULL,
    numero_factura TEXT NOT NULL,
    monto_esperado REAL NOT NULL,
    estado TEXT DEFAULT 'Pendiente'
)
''')

# Insertamos 5 facturas (Escenarios mixtos)
facturas = [
    ('900123456-7', 'FAC-1001', 150000.00, 'Pendiente'), # Discrepancia matemática
    ('800987654-3', 'FAC-1002', 320500.50, 'Pendiente'), # Éxito
    ('700111222-1', 'FAC-1003', 45000.00, 'Pendiente'),  # Éxito
    ('600333444-2', 'FAC-1004', 9999.99, 'Pendiente'),   # Discrepancia matemática
    ('500555666-5', 'FAC-1005', 125000.00, 'Pendiente')  # Éxito
]

cursor.executemany('''
INSERT INTO facturas_pendientes (nit_cliente, numero_factura, monto_esperado, estado)
VALUES (?, ?, ?, ?)
''', facturas)

conexion.commit()
conexion.close()
print("Base de datos actualizada con 5 facturas para pruebas masivas.")