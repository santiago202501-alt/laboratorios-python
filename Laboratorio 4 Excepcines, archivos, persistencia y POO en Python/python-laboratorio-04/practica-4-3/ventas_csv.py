import csv
from pathlib import Path

def gestionar_ventas():
    ruta = Path(__file__).parent / "ventas.csv"
    ventas = [
        {"codigo": "V001", "producto": "Teclado Mecánico", "cantidad": 2, "total": 300000.0},
        {"codigo": "V002", "producto": "Mouse Gamer", "cantidad": 1, "total": 80000.0},
        {"codigo": "V003", "producto": "Monitor 24 pulgadas", "cantidad": 1, "total": 650000.0},
        {"codigo": "V004", "producto": "Diadema USB", "cantidad": 3, "total": 150000.0}
    ]

    encabezados = ["codigo", "producto", "cantidad", "total"]
    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(ventas)  

    print("✓ Ventas exportadas correctamente a 'ventas.csv'.\n")
    total_acumulado = 0.0

    print("=== Lectura del archivo CSV ===")
    with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            total_venta = float(fila["total"])
            total_acumulado += total_venta
            
            print(f"[{fila['codigo']}] {fila['producto']} | Cantidad: {fila['cantidad']} | Total: ${total_venta:,.2f}")

    print("\n--------------------------------")
    print(f"TOTAL VENDIDO: ${total_acumulado:,.2f}")

if __name__ == "__main__":
    gestionar_ventas()