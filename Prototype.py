import copy

# Prototipo: Interfaz Documento
class Documento:
    def clonar(self):
        pass

# Prototipos concretos
class CurriculumVitae(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Curriculum Vitae: {self.contenido}"

class CartaPresentacion(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Carta de Presentación: {self.contenido}"

class Informe(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Informe: {self.contenido}"


# Cliente: Editor de Documentos
class EditorDocumentos:
    def __init__(self):
        self.plantillas = {
            "CV": CurriculumVitae("Este es un CV básico"),
            "Carta": CartaPresentacion("Estimado Señor, ..."),
            "Informe": Informe("Informe del proyecto...")
        }

    def clonar_documento(self, tipo):
        plantilla = self.plantillas.get(tipo)
        if plantilla:
            return plantilla.clonar()
        else:
            return None


# Simulación de uso real:
editor = EditorDocumentos()

cv_clon = editor.clonar_documento("CV")
print(cv_clon)

carta_clon = editor.clonar_documento("Carta")
print(carta_clon)


import unittest

class TestPrototype(unittest.TestCase):
    def test_clonacion_documentos(self):
        editor = EditorDocumentos()
        cv_clon = editor.clonar_documento("CV")
        self.assertIsNotNone(cv_clon)
        self.assertEqual(cv_clon.contenido, "Este es un CV básico")

if __name__ == "__main__":
    unittest.main()
