import argparse
import getpass
import logging
import Funciones

if __name__ == "__main__":
    
    Opciones="""<---------------------------------------------------- Herramientas Vii ----------------------------------------------------->

 Name      Descripcion                                              Ejemplos
------ --------------------- -----------------------------------------------------------------------------------------------
[Proc] Analizar Procesos     python Vii.py -Name Proc
[Wsc]  Web Scraping          python Vii.py -Name Wsc -url "Url de la pagina"
[Md]   Metadata de Imagenes  python Vii.py -Name Md -r C:\\Users\\Alonso\\Downloads\\Imagenes\\
[Env]  Enviar correos        python Vii.py -Name Env -msg "Tu mensaje" -c "Correo" -s "Asunto del mensaje" -e "Destinatario"
[PA]   Analizar los puertos  python Vii.py -Name PA -ip "Tu IP" -port "Puerto a analizar"
[BS]   Api shodan            python Vii.py -Name BS -key "Api key" -b "Buscar"
[DNS]  Registros DNS         python Vii.py -Name DNS -d "domino del DNS"
[DIP]  Obtener dominio IP    python Vii.py -Name DIP -ip "IP del DNS"
[UC]   Obtener ubicacion     python Vii.py -Name UC -key "Api key" -ln "Latitud" -lg "Longitud" """

    vii="""___ _      ___ _  ___ _   ___ _
\  \ \    /  / / |   | | |   | |
 \  \ \  /  / /  |   | | |   | |
  \  \ \/  / /   |   | | |   | |
   \  \/  / /    |   | | |   | |
    \_ _ /_/     |_ _|_| |_ _|_| """    

    try:
        parser=argparse.ArgumentParser(description=vii,
                                       epilog=Opciones, formatter_class=argparse.
                                       RawDescriptionHelpFormatter)
    
        parser.add_argument("-Name", metavar="Nombre", dest="Nombre", help="Nombre de la Herramienta Vii", required=True)
        parser.add_argument("-r", metavar="Ruta", dest="ruta", help="Ruta de la carpeta con las imagenes",required=False)
        parser.add_argument("-url", metavar="Url", dest="Url", help="Link de la pagina Web",required=False)
        parser.add_argument("-msg", metavar="Mensaje", dest="Mensaje", help="Mensaje a enviar al corro",required=False)
        parser.add_argument("-c", metavar="Correo", dest="Correo", help="Correo electronico",required=False)
        parser.add_argument("-s", metavar="Asunto", dest="Asunto", help="Encabezado del mensaje",required=False)
        parser.add_argument("-e", metavar="Destinatario", dest="Destinatario", help="Cuenta que recibira el correo",required=False)
        parser.add_argument("-ip", metavar="IP", dest="IP", help="IP del equipo",required=False)
        parser.add_argument("-port", metavar="Puerto", dest="Puerto", help="Puerto a analizar",required=False)
        parser.add_argument("-key", metavar="key", dest="key", help="Api key de la cuenta",required=False)
        parser.add_argument("-b", metavar="Buscar", dest="Buscar", help="Palabra a Buscar",required=False)
        parser.add_argument("-d", metavar="Dominio", dest="Dominio", help="Dominio del DNS",required=False)
        parser.add_argument("-ln", metavar="Latitud", dest="Latitud", help="Distancia en grados, minutos y segundos respecto al paralelo principal",required=False)
        parser.add_argument("-lg", metavar="Longitud", dest="Longitud", help="Distancia en grados, minutos y segundos respecto al meridiano principal",required=False)
        params=parser.parse_args()
        
        logging.basicConfig(filename="app.log",level=logging.INFO)
        Name=params.Nombre.encode()
        if Name.decode() == "Proc":
            Funciones.Proc()
        elif Name.decode()=="Wsc":
            Url=params.Url.encode()
            Funciones.Wsc(Url.decode())
        elif Name.decode()=="Md":
            rut=params.ruta.encode()
            Funciones.Md(rut.decode())
        elif Name.decode()=="Env":
            user=params.Correo.encode()
            dest=params.Destinatario.encode()
            mess=params.Mensaje.encode()
            ass=params.Asunto.encode()
            pwd=getpass.getpass()
            Funciones.Env(user.decode(),pwd,dest.decode(),ass.decode(),mess.decode()) 
        elif Name.decode()=="PA":
            ip=params.IP.encode()
            port=params.Puerto.encode()
            pp=int(port.decode())
            Funciones.Port(ip.decode(),pp)
        elif Name.decode()=="BS":
            api=params.key.encode()
            bus=params.Buscar.encode()
            Funciones.BS(api.decode(),bus.decode())
        elif Name.decode()=="DNS":
            dom=params.Dominio.encode()
            Funciones.DNS(dom.decode())
        elif Name.decode()=="DIP":
            ip=params.IP.encode()
            Funciones.DIP(ip.decode())
        elif Name.decode()=="UC":
            key=params.key.encode()
            lat=params.Latitud.encode()
            lng=params.Longitud.encode()
            Funciones.UC(key.decode(),lat.decode(),lng.decode())
        else:
            print("No existe la herramienta")
        logging.info("Se inicio Vii Correctamente")
        
    except Exception as e:
        logging.error("Error al inciar Vii "+ str(e))
        print("No se pudo inciar Vii")
