edad = int(input("Introduce tu edad: "))
inscripcion = input("¿Estás inscrito? (sí/no): ").strip().lower()
documentos = int(input("Introduce el número de documentos entregados: "))

cumple_edad = edad >= 16
cumple_inscripcion = (inscripcion == "si")
cumple_documentos = documentos >= 3

cumple_todo = cumple_edad and cumple_inscripcion and cumple_documentos

print("\n--- Resultado de la Evaluación ---")
if cumple_todo:
    print("¡Felicidades! La solicitud cumple con TODOS los requisitos.")
else:
    print("La solicitud NO cumple con todos los requisitos. Detalles a corregir:")
if not cumple_edad:
    print("- La edad debe ser de al menos 16 años.")
if not cumple_inscripcion:
    print("- Debes estar inscrito (responde 'si').")
if not cumple_documentos:
    print("- Faltan documentos (se requieren al menos 3).")