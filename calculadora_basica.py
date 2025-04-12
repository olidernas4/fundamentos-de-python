def calculadora(a, b, operacion):
    operacion = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b if b != 0 else "Error: Division por cero",
    }
    return operacion.get(operacion, "Error: Operacion no valida")
    print(calculadora(10, 5, "suma"))
    print(calculadora(10, 5, "resta"))
