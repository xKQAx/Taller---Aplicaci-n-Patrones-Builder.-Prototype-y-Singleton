import unittest

class TestPrototype(unittest.TestCase):
    def test_clonacion_documentos(self):
        editor = EditorDocumentos()
        cv_clon = editor.clonar_documento("CV")
        self.assertIsNotNone(cv_clon)
        self.assertEqual(cv_clon.contenido, "Este es un CV básico")

if __name__ == "__main__":
    unittest.main()
