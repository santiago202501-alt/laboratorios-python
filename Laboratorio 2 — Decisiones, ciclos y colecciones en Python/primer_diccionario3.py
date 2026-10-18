producto= {}
producto ["cantidad"] = 8
producto ["activo"] = True

print(producto.get("marca"))
print(producto.get("marca", "Sin marca"))