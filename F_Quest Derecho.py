"Quizz: Derecho Constitucional Interactivo"

print("\n")
inicio="Bienvenido al cuestionario sobre el 'Derecho Constitucional'"
print(inicio.center(66,"="))
print("\n")

q_0="¿Qué es el derecho?"
print(q_0.center(26,"/"))
print("a. Ciencia social que estudia las normas que regulan a la sociedad.")
print("b. Materia académica y judicial que impone normas a seguir.")
print("c. Orden normativo que regula la conducta humana.")

laws=input("Respuesta 0: ")

if laws == "a" or laws=="c":
    print("Correcto :)")
    r0 = 1 if laws == "a" or laws == "c" else 0
else:
    print("Incorrecto :(")
    r0=0
print("\n")

q_1="El Derecho Constitucional es una rama que estudia..."
print(q_1.center(50,"/"))
print("a. La administración pública.")
print("b. Principios, Conceptos y Leyes.")
print("c. Las relaciones jurídicas entre individuos.")
print("d. Las condiciones laborales y económicas.")
definition=input("Respuesta 1: ")

if definition == "b":
    print("Correcto :)")
    r1 = 1 if definition == "b" else 0
else:
    print("Incorrecto :(")
    r1=0
print("\n")

q_2="¿Qué es la soberanía?"
print(q_2.center(60,"/"))
print("a. Capacidad del estado para decidir sobre asuntos internos.")
print("b. Integridad de un individuo.")
print("c. La represión y privatización de bienes.")
soberanía=input("Respuesta 2: ")

if soberanía == "a":
    print("Correcto :)")
    r2 = 1 if soberanía == "a" else 0
else:
    print("Incorrecto :(")
    r2=0
print("\n")

q_3="¿A qué clasificación pertenece el Derecho Constitucional?"
print(q_3.center(50,"/"))
print("a. Derecho Privado.")
print("b. Derecho Público.")
clasification=input("Respuesta 3: ")

if clasification == "b":
    print("Correcto :)")
    r3 = 1 if clasification == "b" else 0
else:
    print("Incorrecto :( ")
    r3=0
print("\n")

q_4="¿Qué límites establece el Derecho Constitucional?"
print(q_4.center(60,"/"))
print("a. El control sobre el pueblo.")
print("b. El alcance que tienen las leyes.")
print("c. Restringe al poder político en la creación de normas.")
constiq4=input("Respuesta 4: ")

if constiq4 == "c":
    print("Correcto :)")
    r4 = 1 if constiq4 == "c" else 0
else:
    print("Incorrecto :(")
    r4=0
print("\n")

q_5="¿Cuáles son las dos partes de la Constitución?"
print(q_5.center(50,"/"))
print("a. Arcana, Civil y Electoral.")
print("b. Judicial, Ejecutiva y Legislativa.")
print("c. Dogmática y Orgánica.")
constitución=input("Respuesta 5: ")

if constitución == "c":
    print("Correcto :)")
    r5 = 1 if constitución == "c" else 0
else:
    print("Incorrecto :(")
    r5=0
print("\n")

q_6="¿Qué constituciones son aquellas donde la propiedad fundamental de los medios de producción está en manos del gobierno?"
print(q_6.center(100, "/"))
print("a. Capitalistas.")
print("b. Mixtas.")
print("c. Socialistas.")
socialistas=input("Respuesta 6: ")

if socialistas == "c":
    print("Correcto :)")
    r6 = 1 if socialistas == "c" else 0
else:
    print("Incorrecto :(")
    r6=0
print("\n")

q_7="Según lo visto, ¿cómo pueden ser las constituciones?"
print(q_7.center(60,"/"))
print("a. Pueden ser unitarias o dispersas.")
print("b. Pueden ser largas o cortas.")
print("c. Pueden ser antiguas o modernas.")
formas_constitución=input("Respuesta 7: ")

if formas_constitución == "a":
    print("Correcto :)")
    r7 = 1 if formas_constitución == "a" else 0
else:
    print("Incorrecto :(")
    r7=0
print("\n")

q_8="¿Cuál es el propósito de la Constitución mexicana?"
print(q_8.center(60,"/"))
print("a. Establecer un sistema federal de gobierno y reconocer los derechos humanos, sociales y económicos de los ciudadanos.")
print("b. Establecer un sistema unitario de gobierno y reconocer solo los derechos humanos de los ciudadanos.")
print("c. Establecer un sistema confederado de gobierno y reconocer solo los derechos económicos de los ciudadanos.")
consti_mexicana=input("Respuesta 8: ")

if consti_mexicana == "a":
    print("Correcto :)")
    r8 = 1 if consti_mexicana == "a" else 0
else:
    print("Incorrecto :(")
    r8=0
print("\n")

q_9="¿Cuál es el propósito de la Constitución mexicana?"
print(q_9.center(60,"/"))
print("a. México es una monarquía constitucional donde el rey tiene el poder supremo.")
print("b. México es una república representativa, democrática, laica y federal, donde la soberanía reside esencial y originariamente en el pueblo.")
print("c. México es una república teocrática donde la religión oficial tiene un papel dominante en el gobierno.")
propósito=input("Respuesta 9: ")

if propósito == "b":
    print("Correcto :)")
    r9 = 1 if propósito == "b" else 0
else:
    print("Incorrecto :(")
    r9=0
print("\n")

q_10="¿Qué limitaciones impone la Constitución a los niveles de gobierno?"
print(q_10.center(60,"/"))
print("a. No pueden celebrar alianzas con otros estados o potencias extranjeras.")
print("b. No pueden acuñar moneda o emitir papel moneda.")
print("c. No pueden gravar el tránsito o las mercancías que atraviesen su territorio.")
print("d. Todas las anteriores.")
limitaciones=input("Respuesta 10: ")

if limitaciones == "d":
    print("Correcto :)")
    r10 = 1 if limitaciones == "d" else 0
else:
    print("Incorrecto :(")
    r10=0
print("\n")

q_11="¿Qué deben hacer los estados con las leyes federales?"
print(q_11.center(60,"/"))
print("a. Ignorarlas.")
print("b. Publicarlas y hacerlas cumplir.")
print("c.  Modificarlas.")
print("d. Rechazarlas.")
leyesf=input("Respuesta 11: ")

if leyesf == "b":
    print("Correcto :)")
    r11 = 1 if leyesf == "b" else 0
else:
    print("Incorrecto :(")
    r11=0
print("\n")

q_12="¿Cómo se divide el Congreso general según el Artículo 50?"
print(q_12.center(60,"/"))
print("a. En tres Cámaras.")
print("b. En dos Cámaras, una de diputados y otra de senadores.")
print("c. En una Cámara de diputados.")
print("d. En una Cámara de senadores.")
art50=input("Respuesta 12: ")

if art50 == "b":
    print("Correcto :)")
    r12 = 1 if art50 == "b" else 0
else:
    print("Incorrecto :(")
    r12=0
print("\n")

q_13="¿Qué establece el artículo 83 sobre los ex-presidentes?"
print(q_13.center(60,"/"))
print("a. No pueden ser reelegidos.")
print("b. Pueden ser reelegidos.")
print("c. Pueden postularse para senadores.")
print("d. Pueden postularse para diputados.")
art80=input("Respuesta 13: ")

if art80 == "a":
    print("Correcto :)")
    r13 = 1 if art80 == "a" else 0
else:
    print("Incorrecto :(")
    r13=0
print("\n")

q_14="¿En quién recae el ejercicio del Supremo Poder Ejecutivo de la Unión según el Artículo 80?"
print(q_14.center(60,"/"))
print("a. En el Congreso.")
print("b. En los diputados.")
print("c. En los senadores.")
print("d. En el presidente de los Estados Unidos Mexicanos.")
poder_supremo=input("Respuesta 14: ")

if poder_supremo == "d":
    print("Correcto :)")
    r14 = 1 if poder_supremo == "d" else 0
else:
    print("Incorrecto :(")
    r14=0
print("\n")

q_15="¿Qué caracteriza al modelo de Gobierno Parlamentario?"
print(q_15.center(60,"/"))
print("a. El poder reace en el pueblo, en donde los ciudadanos tienen el poder de elegir a sus representantes.")
print("b. Se basa en la jefatura de 2 jefes de estado.")
print("c. El jefe de estado y el jefe de gobierno son la misma persona.")
print("d. El jefe de estado y el jefe de gobierno son personas distintas personas.")
g_p=input("Respuesta 15: ")

if g_p == "d":
    print("Correcto :)")
    r15 = 1 if g_p == "d" else 0
else:
    print("Incorrecto :(")
    r15=0
print("\n")

q_16="'La República Mexicana es definida como una república representativa, democrática, laica y federal.'"
print(q_16.center(60,"/"))
print("a. Artículo 39.")
print("b. Artículo 40.")
print("c. Artículo 38.")
art40=input("Respuesta 16: ")

if art40 == "b":
    print("Correcto :)")
    r16 = 1 if art40 == "b" else 0
else:
    print("Incorrecto :(")
    r16=0
print("\n")

q_17="¿Qué artículo estipula la función del poder legislativo?"
print(q_17.center(60,"/"))
print("a. No. 45")
print("b. No. 50")
print("c. No. 72")
legislativo=input("Respuessta : ")

if legislativo == "b":
    print("Correcto :)")
    r17 = 1 if legislativo == "b" else 0
else:
    print("Incorrecto :(")
    r17=0
print("\n")

q_18="¿Cuáles son las 3 formas de gobierno en México?"
print(q_18.center(50,"/"))
print("a. Estatal, Federal, Municipal.")
print("b. Centralista, Izquierdista, Socialismo.")
print("c. Neoliberalismo, Capitalismo, Independiente.")
emf=input("Respuesta 18: ")

if emf == "a":
    print("Correcto :)")
    r18 = 1 if emf == "a" else 0
else:
    print("Incorrecto :(")
    r18=0

respuestas = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18]
puntaje_total = sum(respuestas)

if puntaje_total >= 13:
    print(f"Felicidades, tu puntaje fue de {puntaje_total}, te ganaste un dulce a elegir.")
elif puntaje_total <= 10:
    print("Desafortunadamente reprobaste, tendrás que repasar el tema.")
