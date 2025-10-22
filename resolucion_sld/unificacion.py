def unificacion(sintomas_a_probar, sintomas_enfermedad):
    if not sintomas_a_probar:
        return True

    (parte_afectada, sintoma) = sintomas_a_probar[0]
    resto_sintomas = sintomas_a_probar[1:]

    if (parte_afectada in sintomas_enfermedad and 
        sintoma in sintomas_enfermedad[parte_afectada]):
        
        return unificacion(resto_sintomas, sintomas_enfermedad)
    else:
        return False