import unittest
from tarifa_envio import calcular_costo_envio


class TestCalcularCostoEnvio(unittest.TestCase):

    # Caso base: todos los valores son válidos
    def test_envio_estandar(self):
        resultado = calcular_costo_envio(
            5, 0.4, 0.4, 0.4, 50, "estándar"
        )

        self.assertEqual(resultado, 15000)

    # El peso supera los 10 kg
    def test_recargo_por_peso(self):
        resultado = calcular_costo_envio(
            15, 0.4, 0.4, 0.4, 50, "estándar"
        )

        self.assertEqual(resultado, 38000)

    # El volumen supera los 0.1 m^3
    def test_cargo_por_volumen(self):
        resultado = calcular_costo_envio(
            5, 0.5, 0.5, 0.5, 50, "estándar"
        )

        self.assertEqual(resultado, 35000)

    # La distancia supera los 100 km
    def test_cargo_por_distancia(self):
        resultado = calcular_costo_envio(
            5, 0.4, 0.4, 0.4, 150, "estándar"
        )

        self.assertEqual(resultado, 20000)

    # El envío exprés multiplica el costo por 1.5
    def test_envio_expres(self):
        resultado = calcular_costo_envio(
            5, 0.4, 0.4, 0.4, 50, "exprés"
        )

        self.assertEqual(resultado, 22500)

    # Se aplican simultáneamente todos los cargos
    def test_todos_los_cargos(self):
        resultado = calcular_costo_envio(
            12, 0.5, 0.5, 0.5, 150, "exprés"
        )

        self.assertEqual(resultado, 84600)

    # Peso exactamente igual a 10 kg: sin recargo
    def test_peso_limite_10_kg(self):
        resultado = calcular_costo_envio(
            10, 0.4, 0.4, 0.4, 50, "estándar"
        )

        self.assertEqual(resultado, 25000)

    # Volumen exactamente igual a 0.1 m^3: sin cargo
    def test_volumen_limite(self):
        resultado = calcular_costo_envio(
            5, 0.5, 0.2, 1.0, 50, "estándar"
        )

        self.assertEqual(resultado, 15000)

    # Distancia exactamente igual a 100 km: sin cargo adicional
    def test_distancia_limite_100_km(self):
        resultado = calcular_costo_envio(
            5, 0.4, 0.4, 0.4, 100, "estándar"
        )

        self.assertEqual(resultado, 15000)

    # Validación de peso
    def test_peso_cero(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                0, 0.4, 0.4, 0.4, 50, "estándar"
            )

    def test_peso_negativo(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                -5, 0.4, 0.4, 0.4, 50, "estándar"
            )

    # Validación de dimensiones
    def test_largo_cero(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0, 0.4, 0.4, 50, "estándar"
            )

    def test_ancho_negativo(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0.4, -0.4, 0.4, 50, "estándar"
            )

    def test_alto_cero(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0.4, 0.4, 0, 50, "estándar"
            )

    # Validación de distancia
    def test_distancia_cero(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0.4, 0.4, 0.4, 0, "estándar"
            )

    def test_distancia_negativa(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0.4, 0.4, 0.4, -10, "estándar"
            )

    # Validación del tipo de envío
    def test_tipo_envio_invalido(self):
        with self.assertRaises(ValueError):
            calcular_costo_envio(
                5, 0.4, 0.4, 0.4, 50, "económico"
            )

    # Se aceptan mayúsculas gracias a lower()
    def test_tipo_envio_mayusculas(self):
        resultado = calcular_costo_envio(
            5, 0.4, 0.4, 0.4, 50, "ESTÁNDAR"
        )

        self.assertEqual(resultado, 15000)


if __name__ == "__main__":
    unittest.main()