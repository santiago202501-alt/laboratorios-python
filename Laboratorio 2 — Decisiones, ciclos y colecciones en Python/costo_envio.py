valor_compra = float(input("Introduce el valor de la compra: $"))

if valor_compra >= 200000:
    costo_envio = 0
elif valor_compra >= 100000:
     costo_envio = 10000
else:
      costo_envio = 18000

      total_pagar = valor_compra + costo_envio
      print("\n--- Resumen de la Compra ---")
      print(f"Valor de la compra: ${valor_compra:,.0f}")
      print(f"Costo de envío:     ${costo_envio:,.0f}")
      print(f"Total a pagar:      ${total_pagar:,.0f}")