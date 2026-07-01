banco = {}

def crear_cuenta(numero, titular, saldo_inicial, tipo):
    if saldo_inicial < 0:
        print("No se permiten saldos iniciales negativos.")
        return
    banco[numero] = {
        "titular": titular,
        "saldo": saldo_inicial,
        "tipo": tipo,
        "historial": [("Apertura", saldo_inicial)]
    }

def depositar(numero, monto):
    if numero in banco and monto > 0:
        banco[numero]["saldo"] += monto
        banco[numero]["historial"].append(("Depósito", monto))
    else:
        print("Transacción inválida.")

def retirar(numero, monto):
    if numero in banco and 0 < monto <= banco[numero]["saldo"]:
        banco[numero]["saldo"] -= monto
        banco[numero]["historial"].append(("Retiro", monto))
    else:
        print("Fondos insuficientes o cuenta inexistente.")

def transferir(origen, destino, monto):
    if origen in banco and destino in banco and 0 < monto <= banco[origen]["saldo"]:
        banco[origen]["saldo"] -= monto
        banco[destino]["saldo"] += monto
        banco[origen]["historial"].append((f"Transferencia enviada a {destino}", monto))
        banco[destino]["historial"].append((f"Transferencia recibida de {origen}", monto))
    else:
        print("No se pudo realizar la transferencia.")

crear_cuenta("123", "Juan Pérez", 500, "Ahorros")
crear_cuenta("456", "María López", 100, "Corriente")
transferir("123", "456", 200)

print("Estado final cuenta 123:", banco["123"])