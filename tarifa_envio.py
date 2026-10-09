def calcular_costo_envio(peso, largo, ancho, alto, distancia, tipo_envio):
    # VALIDACIONES
    if peso <= 0:
        raise ValueError("El peso debe ser un número positivo.")

    if largo <= 0:
        raise ValueError("El largo debe ser un número positivo.")

    if ancho <= 0:
        raise ValueError("El ancho debe ser un número positivo.")

    if alto <= 0:
        raise ValueError("El alto debe ser un número positivo.")

    if distancia <= 0:
        raise ValueError("La distancia debe ser un número positivo.")

    tipo_envio = tipo_envio.lower()

    if tipo_envio not in ["estándar", "exprés"]:
        raise ValueError(
            "El tipo de envío debe ser 'estándar' o 'exprés'."
        )

    # TARIFA BASE
    costo = 5000

    # CARGO POR PESO
    cargo_peso = peso * 2000
    costo += cargo_peso

    # Recargo del 10% si supera 10 kg
    if peso > 10:
        recargo_peso = cargo_peso * 0.10
        costo += recargo_peso

    # CARGO POR VOLUMEN
    volumen = largo * ancho * alto

    if volumen > 0.1:
        costo += 20000

    # CARGO POR DISTANCIA
    if distancia > 100:
        kilometros_extra = distancia - 100
        costo += kilometros_extra * 100

    # AJUSTE POR TIPO DE ENVÍO
    if tipo_envio == "exprés":
        costo *= 1.5

    return costo

try:
    costo = calcular_costo_envio(
        peso=12,
        largo=0.5,
        ancho=0.5,
        alto=0.5,
        distancia=150, tipo_envio="exprés" )
    print(f"Costo de envío: ${costo:,.0f}")
except ValueError as error:
    print(f"Error: {error}")