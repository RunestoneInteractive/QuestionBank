.. activecode:: tree_list1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Trees
    :subchapter: RepresentacionDeListaDeListas
    :topics: Trees/RepresentacionDeListaDeListas
    :from_source: None
    :caption: Uso de indización para acceder a los subárboles

    miArbol = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
    print(miArbol)
    print('subárbol izquierdo = ', miArbol[1])
    print('raíz = ', miArbol[0])
    print('subárbol derecho = ', miArbol[2])