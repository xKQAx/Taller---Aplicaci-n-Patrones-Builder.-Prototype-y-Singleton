import unittest

class TestCVBuilder(unittest.TestCase):
    def test_builder_cv_cronologico(self):
        info = "John Doe"
        experiencias = ["Dev en ZCorp"]
        educaciones = ["Ingeniería en Software"]
        habilidades = ["Java"]
        proyectos = ["Sistema de Inventarios"]
        referencias = ["Jane Doe"]

        builder = CVBuilderCronologico()
        generador = GeneradorCV(builder)
        cv = generador.construir_cv(info, experiencias, educaciones, habilidades, proyectos, referencias)
        
        self.assertIn("John Doe", str(cv))
        self.assertIn("Dev en ZCorp", str(cv))
        self.assertIn("Java", str(cv))

if __name__ == "__main__":
    unittest.main()