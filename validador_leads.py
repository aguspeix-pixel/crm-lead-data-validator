import re
import sqlite3
import pandas as pd

PATRON_EMAIL = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def limpiar_telefono(valor):
    digitos = re.sub(r"\D", "", str(valor))
    return digitos if len(digitos) >= 8 else "INVALIDO"

def validar_email(email):
    email_limpio = str(email).strip().lower()
    return bool(PATRON_EMAIL.match(email_limpio))

def procesar_leads(archivo_entrada="leads_crudos.csv"):
    print("🚀 Iniciando validación y limpieza de base CRM...")
    df = pd.read_csv(archivo_entrada).fillna("")

    # 1. Normalización de textos
    df["Nombre_Completo"] = df["Nombre_Completo"].astype(str).str.strip().str.title()
    df["Empresa"] = df["Empresa"].astype(str).str.strip().str.title()
    df["Origen"] = df["Origen"].astype(str).str.strip().str.title()
    df["Email"] = df["Email"].astype(str).str.strip().str.lower()

    # 2. Limpieza de teléfonos y validación de correos
    df["Telefono_Limpio"] = df["Telefono"].apply(limpiar_telefono)
    df["Email_Valido"] = df["Email"].apply(validar_email)

    # 3. Separar registros válidos vs rechazados
    condicion_valida = df["Email_Valido"] & (df["Telefono_Limpio"] != "INVALIDO")
    df_validos = df[condicion_valida].copy()
    df_rechazados = df[~condicion_valida].copy()

    # 4. Eliminar duplicados por Email en los válidos
    df_validos = df_validos.drop_duplicates(subset=["Email"], keep="first")

    columnas_finales = ["Nombre_Completo", "Email", "Telefono_Limpio", "Empresa", "Origen"]
    df_validos = df_validos[columnas_finales]

    # 5. Guardar en base de datos SQLite y consultar resumen
    conexion = sqlite3.connect("crm_leads_limpios.db")
    df_validos.to_sql("leads_calificados", conexion, if_exists="replace", index=False)

    query_origen = """
        SELECT 
            Origen,
            COUNT(*) AS Total_Leads_Validos
        FROM leads_calificados
        GROUP BY Origen
        ORDER BY Total_Leads_Validos DESC;
    """
    df_resumen = pd.read_sql_query(query_origen, conexion)
    conexion.close()

    # 6. Exportar Excel listo para importar a CRM
    archivo_salida = "Base_CRM_Limpia.xlsx"
    with pd.ExcelWriter(archivo_salida, engine="openpyxl") as writer:
        df_validos.to_excel(writer, sheet_name="Leads_Validos", index=False)
        df_rechazados.to_excel(writer, sheet_name="Registros_Rechazados", index=False)
        df_resumen.to_excel(writer, sheet_name="Resumen_Por_Origen", index=False)

    print(f"✅ Leads válidos listos para CRM: {len(df_validos)}")
    print(f"⚠️ Registros rechazados para revisión: {len(df_rechazados)}")
    print(f"📊 Base SQLite actualizada: 'crm_leads_limpios.db'")
    print(f"📑 Reporte generado: '{archivo_salida}'")

if __name__ == "__main__":
    procesar_leads()