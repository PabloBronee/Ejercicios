'''
    Se crea la jerarquia solicitada por el ejercicio 5, donde a partir de la clase base empleado se generan una serie
de subclases con sus propios atributos y funciones.
    Posteriormente se generan puestos austenes de la clase empleado, tales como mantenimiento o administrador, con
sus propias funciones y atributos.
'''
# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

# Clase Gerente que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        return f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: {self.salario}"

# Clase Tecnico que hereda de Empleado
class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        return f"Tecnico: {self.nombre}, Especialidad: {self.especialidad}, Salario: {self.salario}"

# Clase Voluntario que hereda de Empleado
class Voluntario(Empleado):
    def __init__(self, nombre, horas_voluntariado):
        # Salario 0 para voluntarios, por eso se especifica directamente en el codigo
        super().__init__(nombre, salario=0)
        self.horas_voluntariado = horas_voluntariado

    def mostrar_informacion(self):
        return f"Voluntario: {self.nombre}, Horas de voluntariado: {self.horas_voluntariado}"

# Clase Administrador (composición)
class Administrador:
    def __init__(self, area_responsabilidad):
        self.area_responsabilidad = area_responsabilidad

    def administrar(self):
        return f"Administrador responsable del área: {self.area_responsabilidad}"

# Clase Mantenimiento (composición)
class Mantenimiento:
    def __init__(self, equipo):
        self.equipo = equipo

    def realizar_mantenimiento(self):
        return f"Realizando mantenimiento al equipo: {self.equipo}"

# Gerente que también es Administrador mediante composición
class GerenteAdministrador(Gerente):
    def __init__(self, nombre, salario, departamento, area_responsabilidad):
        # Inicializamos el Gerente
        Gerente.__init__(self, nombre, salario, departamento)
        # Composición con la clase Administrador
        self.administrador = Administrador(area_responsabilidad)

    def mostrar_informacion_completa(self):
        info_gerente = self.mostrar_informacion()
        info_administrador = self.administrador.administrar()
        return f"{info_gerente}, {info_administrador}"

# Técnico que también hace Mantenimiento mediante composición
class TecnicoMantenimiento(Tecnico):
    def __init__(self, nombre, salario, especialidad, equipo):
        # Inicializamos el Técnico
        Tecnico.__init__(self, nombre, salario, especialidad)
        # Composición con la clase Mantenimiento
        self.mantenimiento = Mantenimiento(equipo)

    def mostrar_informacion_completa(self):
        info_tecnico = self.mostrar_informacion()
        info_mantenimiento = self.mantenimiento.realizar_mantenimiento()
        return f"{info_tecnico}, {info_mantenimiento}"

# Ejemplos de uso

# Gerente que también es Administrador
gerente_admin = GerenteAdministrador("Ana", 5000, "Recursos Humanos", "Presupuesto")
print(gerente_admin.mostrar_informacion_completa())

# Técnico que también realiza Mantenimiento
tecnico_mant = TecnicoMantenimiento("Carlos", 3000, "Redes", "Servidores")
print(tecnico_mant.mostrar_informacion_completa())

# Voluntario simple
voluntario = Voluntario("Laura", 15)
print(voluntario.mostrar_informacion())

