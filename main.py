import json
import os

ARCHIVO = 'contactos.json'

def cargar_contactos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as f:
            return json.load(f)
    return []

def guardar_contactos(contactos):
    with open(ARCHIVO, 'w') as f:
        json.dump(contactos, f)

def menu():
    contactos = cargar_contactos()
    while True:
        print("\n1. Agregar contacto\n2. Ver contactos\n3. Buscar contacto\n4. Actualizar contacto\n5. Eliminar contacto\n6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            contactos.append({'id': len(contactos) + 1, 'nombre': nombre, 'tel': telefono, 'email': email})
            guardar_contactos(contactos)
            print("Contacto agregado.")
        elif opcion == '2':
            for c in contactos:
                print(f"ID: {c['id']}, Nombre: {c['nombre']}, Tel: {c['tel']}, Email: {c['email']}")
        elif opcion == '3':
            busqueda = input("Buscar por nombre o tel: ")
            encontrados = [c for c in contactos if busqueda.lower() in c['nombre'].lower() or busqueda in c['tel']]
            for c in encontrados:
                print(f"ID: {c['id']}, Nombre: {c['nombre']}, Tel: {c['tel']}, Email: {c['email']}")
            if not encontrados:
                print("No encontrado.")
        elif opcion == '4':
            id_c = int(input("ID a actualizar: "))
            for c in contactos:
                if c['id'] == id_c:
                    c['tel'] = input("Nuevo teléfono: ")
                    guardar_contactos(contactos)
                    print("Actualizado.")
                    break
            else:
                print("ID no encontrado.")
        elif opcion == '5':
            id_c = int(input("ID a eliminar: "))
            contactos = [c for c in contactos if c['id'] != id_c]
            guardar_contactos(contactos)
            print("Eliminado.")
        elif opcion == '6':
            break

menu()