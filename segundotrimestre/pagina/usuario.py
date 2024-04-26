usuarios = {
    "jose": {
        "Usuario": "jose",
        "Contraseña": "jose15",
        "rol": "aspirante"
    },
    "eider": {
        "Usuario": "eider",
        "Contraseña": "carechimbauwu",
        "rol": "aprendiz"
    },
    "niche": {
        "Usuario": "joel",
        "Contraseña": "joel",
        "rol": "usuario"
    }
}


def autentica_usuarios():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["Contraseña"] == contraseña:
        print(f"Bienvenido {usuario} su Rol es {rol} <3")
        return usuarios[usuario]["rol"]
    else:
        print("Contraseña o usuario invalido.")
        return 


rol = autentica_usuarios()


if rol == "aspirante":
    
    print("Tiene acceso a: ")
    print("___________________________")
    print("Inscripcion: ")
    print("Consultar programas de formacion")
    print("Consultar inscripciones a programas de formacion")
    print("Eventos de divulgacion tecnologica")
    print("Consultar eventos de divulgacion tecnologica")
    print("Consultar inscripciones a eventos de divulgacion tecnologicas")
    print("___________________________")
    print("Matricula:")
    print("Consultas")
    print("Consultar convocatorias")
    print("___________________________")
    print("Registro:")
    print("Registro persona")
    print("Atualizacion tipo de poblacion")
    print("Contacto")
    print("Datos basicos")
    print("Documentos")
    print("Estudios")
    print("Experiencia laboral")
    print("___________________________")
    print("Seleccion:")
    print("Actividades aspirante")
    print("Consultar citacion a pruebas fase II")
    print("Consultar Resultados de prueba")
    
elif rol == "aprendiz":
    
    print("Tiene acceso a: ")
    print("__________________________")
    print("Certificacion:")
    print("Certificacion")
    print("Eventos de divulgacion")
    print("__________________________")
    print("Ejecucion de la formacion: ")
    print("Complementaria virtual ")
    print("Desarrollar rutas de aprendizaje")
    print("Encuestas")
    print("Evaluar instructores virtuales")
    print("_________________________")
    print("Gestion de ambientes: ")
    print("ambientes")
    print("_______________________")
    print("Gestion de tiempos:")
    print("Gestion tiempo del Aprendiz")
    print("_________________________")
    print("Inscripcion: ")
    print("Consultar programas de formacion")
    print("Eventos de divulgacion Tecnologica")
    print("________________________")
    print("LMS:")
    print("LMS")
    print("Registro: ")
    print("Registro persona")

elif rol == "usuario":
    
    print("Tiene acceso a: ")
    print("________________________")
    print("Inscripcion:")
    print("Eventos de divulgacion tecnologica")
    print("________________________")
    print("Registro: ")
    print("Registro persona")
else:

    print("NO esta registrado en Sofiaplus.")