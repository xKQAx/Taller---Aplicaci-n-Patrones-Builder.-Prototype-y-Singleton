# Producto: Clase CV
class CV:
    def __init__(self):
        self.informacion_personal = None
        self.experiencia_laboral = []
        self.educacion = []
        self.habilidades = []
        self.proyectos = []
        self.referencias = []

    def __str__(self):
        return (f"CV:\n"
                f"Información Personal: {self.informacion_personal}\n"
                f"Experiencia Laboral: {self.experiencia_laboral}\n"
                f"Educación: {self.educacion}\n"
                f"Habilidades: {self.habilidades}\n"
                f"Proyectos: {self.proyectos}\n"
                f"Referencias: {self.referencias}\n")


# Interfaz: CVBuilder
class CVBuilder:
    def set_informacion_personal(self, info):
        pass

    def add_experiencia_laboral(self, experiencia):
        pass

    def add_educacion(self, educacion):
        pass

    def add_habilidades(self, habilidad):
        pass

    def add_proyectos(self, proyecto):
        pass

    def add_referencias(self, referencia):
        pass

    def get_cv(self):
        pass


# Constructores concretos
class CVBuilderCronologico(CVBuilder):
    def __init__(self):
        self.cv = CV()

    def set_informacion_personal(self, info):
        self.cv.informacion_personal = info

    def add_experiencia_laboral(self, experiencia):
        self.cv.experiencia_laboral.append(experiencia)

    def add_educacion(self, educacion):
        self.cv.educacion.append(educacion)

    def add_habilidades(self, habilidad):
        self.cv.habilidades.append(habilidad)

    def add_proyectos(self, proyecto):
        self.cv.proyectos.append(proyecto)

    def add_referencias(self, referencia):
        self.cv.referencias.append(referencia)

    def get_cv(self):
        return self.cv


class CVBuilderCreativo(CVBuilder):
    def __init__(self):
        self.cv = CV()

    def set_informacion_personal(self, info):
        self.cv.informacion_personal = f"Creativo: {info}"

    def add_experiencia_laboral(self, experiencia):
        self.cv.experiencia_laboral.append(f"Exp Creativa: {experiencia}")

    def add_educacion(self, educacion):
        self.cv.educacion.append(f"Edu Creativa: {educacion}")

    def add_habilidades(self, habilidad):
        self.cv.habilidades.append(f"Habilidad Creativa: {habilidad}")

    def add_proyectos(self, proyecto):
        self.cv.proyectos.append(f"Proyecto Creativo: {proyecto}")

    def add_referencias(self, referencia):
        self.cv.referencias.append(f"Referencia Creativa: {referencia}")

    def get_cv(self):
        return self.cv


# Director: GeneradorCV
class GeneradorCV:
    def __init__(self, builder):
        self.builder = builder

    def construir_cv(self, info, experiencias, educaciones, habilidades, proyectos, referencias):
        self.builder.set_informacion_personal(info)
        for exp in experiencias:
            self.builder.add_experiencia_laboral(exp)
        for edu in educaciones:
            self.builder.add_educacion(edu)
        for hab in habilidades:
            self.builder.add_habilidades(hab)
        for pro in proyectos:
            self.builder.add_proyectos(pro)
        for ref in referencias:
            self.builder.add_referencias(ref)
        return self.builder.get_cv()


# Simulación de uso real:
info_personal = "John Doe, johndoe@mail.com"
experiencias = ["Desarrollador en XCorp", "Ingeniero de software en YTech"]
educaciones = ["Bachiller en Ciencias de la Computación", "Maestría en Ingeniería"]
habilidades = ["Python", "C++", "SQL"]
proyectos = ["App de gestión de tareas", "Sistema de inventarios"]
referencias = ["Jane Smith, Directora de Proyectos"]

builder = CVBuilderCronologico()
generador = GeneradorCV(builder)
cv_final = generador.construir_cv(info_personal, experiencias, educaciones, habilidades, proyectos, referencias)
print(cv_final)


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

