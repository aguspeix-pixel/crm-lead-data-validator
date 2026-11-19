import pandas as pd

leads_sucios = {
    "Nombre_Completo": [
        "  maria gomez ", "Carlos Ruiz", "MARIA GOMEZ", "Laura Fernandez",
        "pedro lopez", "Sofia Martinez", "Juan Perez", "Ana Torres"
    ],
    "Email": [
        "maria.gomez@empresa.com ", "carlos.ruiz@gmail.com", "maria.gomez@empresa.com",
        "laura_fernandez_sin_arroba.com", "pedro@dominio", "sofia.martinez@startup.io",
        "", "ana.torres@corp.com"
    ],
    "Telefono": [
        "+54 (11) 4567-8901", "11 2345 6789", "+54 11 4567-8901",
        "abc-123", "1198765432", "+1-800-555-0199",
        "1144445555", "11-3333-2222"
    ],
    "Empresa": [
        "tech solutions", "Innova SA", "TECH SOLUTIONS", "Grupo Sur",
        "Logistica Express", "Startup IO", "Comercial Norte", "corp argentina"
    ],
    "Origen": [
        "LinkedIn", "Web", "LinkedIn", "Evento",
        "Web", "LinkedIn", "Referido", "Web"
    ]
}

pd.DataFrame(leads_sucios).to_csv("leads_crudos.csv", index=False)
print("✅ Archivo 'leads_crudos.csv' generado con registros sucios y duplicados.")