.. activecode::  mcd_cl
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Introduction
    :subchapter: ProgramacionOrientadaAObjetosEnPythonDefinicionDeClases
    :topics: Introduction/ProgramacionOrientadaAObjetosEnPythonDefinicionDeClases
    :from_source: None
    :caption: Función del máximo común divisor

    def mcd(m,n):
        while m%n != 0:
            mViejo = m
            nViejo = n

            m = nViejo
            n = mViejo%nViejo
        return n

    print(mcd(20,10))