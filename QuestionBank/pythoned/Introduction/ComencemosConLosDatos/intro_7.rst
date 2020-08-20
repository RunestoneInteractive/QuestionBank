.. activecode:: intro_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Introduction
    :subchapter: ComencemosConLosDatos
    :topics: Introduction/ComencemosConLosDatos
    :from_source: None
    :caption: Uso de un diccionario

    capitales = {'Iowa':'DesMoines','Wisconsin':'Madison'}
    print(capitales['Iowa'])
    capitales['Utah']='SaltLakeCity'
    print(capitales)
    capitales['California']='Sacramento'
    print(len(capitales))
    for k in capitales:
       print(capitales[k]," es la capital de ", k)