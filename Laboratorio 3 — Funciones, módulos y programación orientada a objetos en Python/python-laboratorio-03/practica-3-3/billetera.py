class Billetera:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"Titular: {self.titular} | Saldo actual: ${self.saldo:,.2f}")

    def registrar_ingreso(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"[{self.titular}] Ingreso exitoso de ${monto:,.2f}.")
        else:
            print(f"[{self.titular}] Error: El monto a ingresar debe ser mayor a cero.")

    def registrar_gasto(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Error: El monto del gasto debe ser mayor a cero.")
        elif monto > self.saldo:
            print(f"[{self.titular}] Error: Fondos insuficientes para gastar ${monto:,.2f}.")
        else:
            self.saldo -= monto
            print(f"[{self.titular}] Gasto registrado de ${monto:,.2f}.")

billetera_luis = Billetera("Luis", 50000)
billetera_maria = Billetera("María", 100000)

print("--- Estado Inicial ---")
billetera_luis.consultar_saldo()
billetera_maria.consultar_saldo()

print("\n--- Operaciones ---")
billetera_luis.registrar_ingreso(20000)
billetera_luis.registrar_gasto(15000)

billetera_maria.registrar_gasto(40000)
billetera_maria.registrar_gasto(200000) 

print("\n--- Estado Final (Comprobando independencia) ---")
billetera_luis.consultar_saldo()
billetera_maria.consultar_saldo()