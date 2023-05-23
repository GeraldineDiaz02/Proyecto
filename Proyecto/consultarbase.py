import sqlite3

def registrar(nombre,fechana,genero,intereses,descripcion,profesion,areatrab):
    db = sqlite3.connect("Bseusuarios.s3db")
    cursor = db.cursor()
    consulta = "insert into Registros (Nombre,fechana,genero,intereses,descripcion,profesion,areatrab) values ('"+ nombre +"','" + fechana + "'," +genero+","+intereses+"','"+descripcion+"','"+profesion+"','"+areatrab+")"
    cursor.execute(consulta)
    db.commit()
    cursor.close()
    db.close()
    return "1"

def crearusu(email,contrasena,numcel):
    db = sqlite3.connect("Bseusuarios.s3db")
    cursor = db.cursor()
    consulta = "insert into Creacionusuario (email,contrasena,numcel) values('"\
        + email +"','" + contrasena + "'," + str(numcel)
    cursor.execute(consulta)
    db.commit()
    cursor.close()
    db.close()
    return "1"

def validar(usuario):
    db=sqlite3.connect("Bseusuarios.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select contrasena from Usuarios where usuario = "+x+""
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    print(list(resultado))
    cursor.close()
    db.close()
    return resultado

def main():
    Nombre=input('Ingrese su Nombre: ')
    fechana=int(input('Ingrese su fecha de nacimiento: '))
    genero=input('escoja su genero ')
    intereses=(input('Ingrese sus interes: '))
    descripcion=(input('Ingrese una descripcion de su persona: '))
    profesion=input('Ingrese su Profesion ')
    areatrab=input('Ingrese su area de trabajo ')
    Registrar(Nombre,fechana,genero,intereses,descripcion,profesion,areatrab)
    x = input('\nIngrese su usuario: ')
    validar(consulta)


def hola():
    print("funcnion")

if __name__ == "__main__":
    main()