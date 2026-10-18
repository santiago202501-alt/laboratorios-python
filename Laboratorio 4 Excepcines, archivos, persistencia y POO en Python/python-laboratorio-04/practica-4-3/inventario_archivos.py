import json
import csv
from pathlib import Path

ruta_json = Path(__file__).parent / "inventario.json"
ruta_csv = Path(__file__).parent / "inventario.csv"

def cargar():
    if ruta_json.exists():
        try:
            return json.loads(ruta_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("⚠ Error: Archivo JSON dañado. No se sobrescribirá.")
    return []

productos = cargar()

while True:
    opc = input("\n1. Ver | 2. Agregar | 3. Guardar JSON | 4. Exportar CSV | 0. Salir: ").strip()
    
    if opc == "1":
        for p in productos:
            print(p)
    elif opc == "2":
        try:
            p = {
                "codigo": input("Código: ").strip(),
                "nombre": input("Nombre: ").strip(),
                "cantidad": int(input("Cantidad: ")),
                "precio": float(input("Precio: "))
            }
            productos.append(p)
            print("Agregado temporalmente.")
        except ValueError:
            print("Error: Datos numéricos inválidos.")
    elif opc == "3":
        ruta_json.write_text(json.dumps(productos, indent=4, ensure_ascii=False), encoding="utf-8")
        print("✓ Guardado en JSON.")
    elif opc == "4":
        if productos:
            with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=productos[0].keys())
                w.writeheader()
                w.writerows(productos)
            print("✓ Exportado a CSV.")
        else:
            print("Inventario vacío.")
    elif opc == "0":
        break