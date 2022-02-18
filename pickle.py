import os

lista = open('lista.txt', 'w')
lista.close()

try:
	respaldo = open('respaldo.txt', 'r')
	datos = respaldo.readlines()
	lista = open('lista.txt', 'a')
	if len(datos) == 1:
		print("Datos restaurados\n")
		print("Nombre:", datos[0])
		numero_lista = int(input("Ingresa el numero de lista: "))
		calificacion = int(input("Ingresa la calificación: "))
		lista.write(datos[0])
		lista.write('\n')
		lista.write(str(numero_lista))
		lista.write('\n')
		lista.write(str(calificacion))
		lista.write('\n')
		lista.write('\n')
		lista.close()
	elif len(datos) == 2:
		print("Datos restaurados\n")
		print("Nombre:", datos[0])
		print("Numero de lista:", datos[1])
		calificacion = int(input("Ingresa la calificación: "))
		lista.write(datos[0])
		lista.write('\n')
		lista.write(str(datos[1]))
		lista.write('\n')
		lista.write(str(calificacion))
		lista.write('\n')
		lista.write('\n')
		lista.close()
	elif len(datos) == 3:
		print("Datos restaurados\n")
	
	os.system('cls')
	print("Alumno registrado...\n")
	respaldo.close()
	os.remove('respaldo.txt')

except:
	pass

opcion = 0
while opcion != 3:
	print("Selecciona la opción deseada:\n1.-Agregar alumno\n2.-Ver lista de alumnos\n3.-Salir")
	opcion = int(input())
	if opcion == 1:
		os.system("cls")
		crear_respaldo = open('respaldo.txt', 'a')
		nombre = input("Ingresa el nombre del alumno: ")
		crear_respaldo.write(nombre)
		crear_respaldo.write('\n')
		crear_respaldo.close()
		crear_respaldo = open('respaldo.txt', 'a')
		numero_lista = int(input("Ingresa el numero de lista: "))
		crear_respaldo.write(str(numero_lista))
		crear_respaldo.write('\n')
		crear_respaldo.close()
		crear_respaldo = open('respaldo.txt', 'a')
		calificacion = int(input("Ingresa la calificación: "))
		crear_respaldo.write(str(calificacion))
		crear_respaldo.write('\n')
		crear_respaldo.write('\n')
		crear_respaldo.close()
		lista = open("lista.txt", "a")
		lista.write(nombre)
		lista.write('\n')
		lista.write(str(numero_lista))
		lista.write('\n')
		lista.write(str(calificacion))
		lista.write('\n')
		lista.write('\n')
		lista.close()
		os.system("cls")
		os.remove('respaldo.txt')
		print("Alumno registrado...\n")
	elif opcion == 2:
		os.system("cls")
		lista = open("lista.txt", "r")
		lineas = lista.readlines()
		if len(lineas) > 0:
			for linea in lineas:
				if linea != "\n":
					print(linea)
			lista.close()
		else:
			os.system("cls")
			print("No hay alumnos registrados...\n")
	elif opcion == 3:
		os.system("cls")
		input("Programa Finalizado...")
	else:
		os.system("cls")
		print("Opcion Incorrecta, vuelva a intentar\n")