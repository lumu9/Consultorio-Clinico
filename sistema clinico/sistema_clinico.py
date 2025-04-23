# Simulación de Componentes del Sistema Clínico

# Base de Datos (simulada)
class BaseDeDatos:
    def guardar(self, entidad, datos):
        print(f"[BD] Guardando en {entidad}: {datos}")

    def consultar(self, entidad, criterio):
        print(f"[BD] Consultando {entidad} con criterio: {criterio}")
        return {"resultado": "datos simulados"}

# Repositorios
class RepositorioPaciente:
    def __init__(self, db):
        self.db = db

    def guardar_paciente(self, datos):
        self.db.guardar("Pacientes", datos)

class RepositorioHistoriaClinica:
    def __init__(self, db):
        self.db = db

    def guardar_historia(self, datos):
        self.db.guardar("HistoriasClinicas", datos)

class RepositorioFolio:
    def __init__(self, db):
        self.db = db

    def guardar_folio(self, datos):
        self.db.guardar("Folios", datos)

# Servicios
class ServicioPaciente:
    def __init__(self, repo):
        self.repo = repo

    def registrar_paciente(self, datos):
        print("[ServicioPaciente] Procesando datos del paciente...")
        self.repo.guardar_paciente(datos)

class ServicioHistoriaClinica:
    def __init__(self, repo):
        self.repo = repo

    def crear_historia(self, datos):
        print("[ServicioHistoriaClinica] Creando historia clínica...")
        self.repo.guardar_historia(datos)

class ServicioFolio:
    def __init__(self, repo_folio):
        self.repo_folio = repo_folio

    def registrar_consulta(self, datos):
        print("[ServicioFolio] Registrando consulta médica...")
        self.repo_folio.guardar_folio(datos)

# Controladores
class ControladorPaciente:
    def __init__(self, servicio):
        self.servicio = servicio

    def registrar(self, datos):
        print("[ControladorPaciente] Llamando al servicio de paciente...")
        self.servicio.registrar_paciente(datos)

class ControladorHistoria:
    def __init__(self, servicio):
        self.servicio = servicio

    def generar(self, datos):
        print("[ControladorHistoria] Llamando al servicio de historia clínica...")
        self.servicio.crear_historia(datos)

class ControladorConsulta:
    def __init__(self, servicio):
        self.servicio = servicio

    def registrar(self, datos):
        print("[ControladorConsulta] Llamando al servicio de folio...")
        self.servicio.registrar_consulta(datos)

# Simulación de Aplicación Web
class AplicacionWeb:
    def __init__(self):
        # Inicialización de la infraestructura
        bd = BaseDeDatos()
        self.ctrl_paciente = ControladorPaciente(ServicioPaciente(RepositorioPaciente(bd)))
        self.ctrl_historia = ControladorHistoria(ServicioHistoriaClinica(RepositorioHistoriaClinica(bd)))
        self.ctrl_consulta = ControladorConsulta(ServicioFolio(RepositorioFolio(bd)))

    def ejecutar(self):
        # Simulamos una sesión
        self.ctrl_paciente.registrar({"nombre": "Ana", "cedula": "1234567", "eps": "Salud Total"})
        self.ctrl_historia.generar({"paciente_id": 1, "fecha": "2025-04-09"})
        self.ctrl_consulta.registrar({"diagnóstico": "Gripe", "tratamiento": "Reposo"})

# Ejecución del sistema
if __name__ == "__main__":
    app = AplicacionWeb()
    app.ejecutar()