meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso","AURA":"desde un concepto espiritual o médico hasta un fenómeno de la cultura de internet","XD":"emoticono de internet que representa una cara riéndose a carcajadas con los ojos fuertemente apretados","GIF":"formato de imagen digital que permite almacenar tanto imágenes estáticas como secuencias de imágenes en bucle que simulan una animación","GAMER":"persona que siente pasión, interés y dedicación por los videojuegos, ya sea de manera ocasional o profesional"
                } 

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("OK?...")
