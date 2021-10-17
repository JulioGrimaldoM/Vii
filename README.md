# <img src="Logo/Icon.png" width="64" valign="middle" alt="Scapy" />&nbsp;&nbsp;

_Vii es un script desarrollado en python y powershell contiene
herramientas muy utiles para la ciberseguridad como obtener la Metadata de imagenes, ver los procesos que realiza nuestra computadora, podemos hacer web scraping entre otras cosas más, es muy util para obtener informacion de manera automatizada_

### Pre-requisitos 📋

_Necesitaras instalar estos modulos en python para que funcione correctamente el script, debes crear un archivo txt con el nombre que quieras y guardarlo en Desktop debera contener lo siguiente_

_Modulos.txt_
```
folium==0.12.1
requests==2.25.1
opencage==2.0.0
shodan==1.25.0
lxml==4.6.3
beautifulsoup4==4.10.0
dnspython==2.1.0
Pillow==8.4.0
```
_En el cmd ejecutamos el siguente comando_
```
C:\Users\Julio\Desktop> pip install -r Modulos.txt
```
##### Api key 👀

_Deberas crear una cuenta y obtener una api key, tiene versiones gratuitas pero con limitaciones_

* [Shodan](https://www.shodan.io/) - Pagina principal
* [Opencagedata](https://opencagedata.com/) - Pagina principal


### Instrucciones 🔧

_Es muy sencillo utilizar Vii lo primero que podemos hacer es pedir ayuda con el siguiente comando pero primero
abriremos cmd, luego haremos cd "ruta"_
```
C:\Users\Julio> cd "C:\Users\Julio\Desktop\PIA"
```
_luego escribimos el siguiente comando_
```
C:\Users\Julio\Desktop\PIA>python Vii.py -h
```
nos dara como resultado los siguiente
```
usage: Vii.py [-h] -Name Nombre [-r Ruta] [-url Url] [-msg Mensaje] [-c Correo] [-s Asunto] [-ip IP] [-port Puerto]
              [-key key] [-b Buscar] [-d Dominio] [-ln Latitud] [-lg Longitud]

___ _      ___ _  ___ _   ___ _
\  \ \    /  / / |   | | |   | |
 \  \ \  /  / /  |   | | |   | |
  \  \ \/  / /   |   | | |   | |
   \  \/  / /    |   | | |   | |
    \_ _ /_/     |_ _|_| |_ _|_|

optional arguments:
  -h, --help    show this help message and exit
  -Name Nombre  Nombre de la Herramienta Vii
  -r Ruta       Ruta de la carpeta con las imagenes
  -url Url      Link de la pagina Web
  -msg Mensaje  Mensaje a enviar al corro
  -c Correo     Correo electronico
  -s Asunto     Encabezado del mensaje
  -ip IP        IP del equipo
  -port Puerto  Puerto a analizar
  -key key      Api key de la cuenta
  -b Buscar     Palabra a Buscar
  -d Dominio    Dominio del DNS
  -ln Latitud   Distancia en grados, minutos y segundos respecto al paralelo principal
  -lg Longitud  Distancia en grados, minutos y segundos respecto al meridiano principal

<-------------------------------------------- Herramientas Vii -------------------------------------------->

 Name      Descripcion                                  Ejemplos
------ --------------------- -----------------------------------------------------------------------------
[Proc] Analizar Procesos     python Vii.py -Name Proc
[Wsc]  Web Scraping          python Vii.py -Name Wsc -url "Url de la pagina"
[Md]   Metadata de Imagenes  python Vii.py -Name Md -r C:\Users\Alonso\Downloads\Imagenes\
[Env]  Enviar correos        python Vii.py -Name Env -msg "Tu mensaje" -c "Correo" -s "Asunto del mensaje"
[PA]   Analizar los puertos  python Vii.py -Name PA -ip "Tu IP" -port "Puerto a analizar"
[BS]   Api shodan            python Vii.py -Name BS -key "Api key" -b "Buscar"
[DNS]  Registros DNS         python Vii.py -Name DNS -d "domino del DNS"
[DIP]  Obtener dominio IP    python Vii.py -Name DIP -ip "IP del DNS"
[UC]   Obtener ubicacion     python Vii.py -Name UC -key "Api key" -ln "Latitud" -lg "Longitud"
```
## Version 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

* **Julio Alonso** - *Trabajo Inicial, Documentación* - [JulioGrimaldoM](https://github.com/JulioGrimaldoM)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* Da las gracias públicamente 🤓.
* etc.
