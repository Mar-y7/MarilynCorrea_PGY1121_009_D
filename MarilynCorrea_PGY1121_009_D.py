import funciones_examen as fe

while True:
    fe.val_menu()
    opciones = fe.val_opciones()
    if opciones == 1:
        fe.comprar_entrada()
    elif opciones == 2:
        fe.ubicacion_disp()
    elif opciones == 3:
        fe.listado_asistentes()
    elif opciones == 4:
        fe.ganancia_total()
    else:
        fe.salir()