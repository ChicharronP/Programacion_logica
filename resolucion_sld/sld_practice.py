from base_conocimiento import enfermedades
from unificacion import unificacion




def realizar_diagnotico(base_conocimiento, diagnostico_paciente):
    diagnosticos_encontrados = []
    
    for enfermedad, sintomas_de_la_enfermedad in base_conocimiento.items():
        if unificacion(diagnostico_paciente, sintomas_de_la_enfermedad):
            diagnosticos_encontrados.append(enfermedad)
            
    return diagnosticos_encontrados


if __name__ == "__main__":
    
    diagnostico = [
        ("sintoma_hoja", "enrollamiento"),
        ("sintoma_hoja", "manchas_blancas_miselio"),
        ("sintoma_hoja", "puntos negros")
    ]
    
    validar_diagnostico = realizar_diagnotico(enfermedades, diagnostico)
    
    print(f"Posibles enfermedades: {validar_diagnostico}")
