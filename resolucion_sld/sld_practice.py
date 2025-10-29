from base_conocimiento import enfermedades
from unificacion import unificacion




def realizar_diagnotico_recursivo(base_conocimiento, diagnostico_paciente):
    
    lista_enfermedades = list(base_conocimiento.items())
    
    def _buscar_recursivo(enfermedades_restantes, paciente, encontrados):
        
        if not enfermedades_restantes:
            return encontrados
        
        (enfermedad_actual, sintomas) = enfermedades_restantes[0]
        resto_de_la_lista = enfermedades_restantes[1:]
        
        if unificacion(paciente, sintomas):
            encontrados.append(enfermedad_actual)
        
        return _buscar_recursivo(resto_de_la_lista, paciente, encontrados)

    return _buscar_recursivo(lista_enfermedades, diagnostico_paciente, [])


if __name__ == "__main__":
    
    diagnostico = [
        ("sintoma_hoja", "enrollamiento"),
        ("sintoma_hoja", "manchas_blancas_miselio"),
        ("sintoma_hoja", "puntos negros")
    ]
    
    validar_diagnostico = realizar_diagnotico(enfermedades, diagnostico)
    
    print(f"Posibles enfermedades: {validar_diagnostico}")
