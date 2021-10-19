import subprocess
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
import requests
import re
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from Web_Scraping import Web_Scraping
import logging, socket
import sys
import errno
import getpass
import shodan
import dns, dns.resolver, dns.query, dns.zone, dns.name, dns.reversename 
import socket
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import folium
import webbrowser

logging.basicConfig(filename="app.log",level=logging.INFO)

#Analisis de Procesos
def Proc():
    try:
        command="powershell -Executionpolicy ByPass -File Process.ps1"
        running1=subprocess.check_output(command)
        print("Analisis de Procesos Exitosa")
        filename1="file:///"+os.getcwd()+"/"+"Report-CPU.html"
        filename2="file:///"+os.getcwd()+"/"+"Report-PCPU.html"
        filename3="file:///"+os.getcwd()+"/"+"Report-TCPU.html"
        webbrowser.open_new_tab(filename1)
        webbrowser.open_new_tab(filename2)
        webbrowser.open_new_tab(filename3)
        logging.info("Se analizo los procesos exitosamente")
    except Exception as e:
        logging.error("Ocurrio un error con el analisis de procesos: "+str(e))
        print("Ocurrio un error")

#Web Scraping
def Wsc(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            exit()
        regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        new_emails = set(re.findall(regExMail, response.text, re.I))
        f = open("Correos.txt", 'a')
        for i in new_emails:
            print("----Correos encontrados----")
            print(i)
            print("############################")
            f.write(i)
        f.close()
        Web_Scraping().ScrapingImg(url)
        Web_Scraping().ScrapingPDF(url)
        Web_Scraping().ScrapingLinks(url)
        logging.info("Web scraping iniciado exitosamente")
        
    except Exception as e:
        logging.error("Ocurrio un error con Web scraping en: "+str(e))
        print("Ocurrio un error")
        
#Analisis de puertos        
def Port(ip, port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result=sock.connect_ex((ip,port))
        if result ==0:
            print("Puerto %s : Abierto" %(port))
        else:
            print("Puerto %s : Cerrado" %(port))
        sock.close()
        logging.info("Se analizaron correctamente los puertos")
    except socket.error as e:
        logging.error("Hubo un fallo al analizar los puertos"+str(e))
        print("Error de conexion")
        sys.exit()
#Metadata
def Md(ruta):
    try:
        os.chdir(ruta)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                print(os.path.join(root, name))
                print ("[+] Metadata for file: %s " %(name))
                try:
                    exifData = {}
                    exif = get_exif_metadata(name)
                    for metadata in exif:
                        print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    print ("\n")
                except:
                    import sys, traceback
                    traceback.print_exc(file=sys.stdout)
        logging.info("Se inicio exitosamente Metadata")
    except:
        logging.error("Error al iniciar Metadata: "+str(e))
        print("Ocurrio un error")

def get_exif_metadata(image_path):
    try:
        ret = {}
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
        decode_gps_info(ret)
        return ret
        logging.info("El proceso Metadata se ejecuto exitosamente")
    except Exception as e:
        logging.error("Error en el proceso"+str(e))
        print("Ocurrio un error")

def decode_gps_info(exif):
    try:
        gpsinfo = {}
        if 'GPSInfo' in exif:
            Nsec = exif['GPSInfo'][2][2] 
            Nmin = exif['GPSInfo'][2][1]
            Ndeg = exif['GPSInfo'][2][0]
            Wsec = exif['GPSInfo'][4][2]
            Wmin = exif['GPSInfo'][4][1]
            Wdeg = exif['GPSInfo'][4][0]
            if exif['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            if exif['GPSInfo'][3] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
            exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        logging.info("Finalizo la busqueda de Metadata exitosamente")
    except Exception as e:
        logging.error("Ocurrio un error con la metadata: " + str(e))
        print("Ups ocurrio un error")
        
#Api Shodan

def BS(Api,buscar):
    try:
        api = shodan.Shodan(Api)
        # Search Shodan
        results = api.search(buscar)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            if result["ip_str"] is not None:
                f=open("IP.txt","a")
                f.write(result["ip_str"])
                f.write("\n")
                f.close()
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
        logging.info("Finalizo la busqueda shodan exitosamente")
    except Exception as e:
        logging.error("Ocurrio un error con la busqueda: " + str(e))
        print('Error: {}'.format(e))
        
#Consultas a registros DNS   
def DNS(dom):
    try:
        ansA, ansMX, ansNS, ansAAAA=(dns.resolver.resolve(dom,"A"),
                                     dns.resolver.resolve(dom,"MX"),
                                     dns.resolver.resolve(dom,"NS"),
                                     dns.resolver.resolve(dom,"AAAA"))
        print("Registros de Servidores de correo")
        print("---------------------------------")
        print(ansMX.response.to_text())
        print("\nRegistros de Servidores de nombre")
        print("-----------------------------------")
        print(ansNS.response.to_text())
        print("\nRegistros de Direcciones IPV4")
        print("-------------------------------")
        print(ansA.response.to_text())
        print("\nRegistros de direcciones IPV6")
        print("-------------------------------")
        print(ansAAAA.response.to_text())
        logging.info("Finalizo el registro DNS con exito")
    except Exception as e:
        logging.error("Ocurrio un error con la solicitud: " + str(e))
        print(str(e))
#Obtener dominio con una ip
def DIP(ip):
    domain=dns.reversename.from_address(ip)
    print(domain)

#Enviar Correo Electronico
def Env(user,pwd,to,subject,text):
    msg=MIMEText(text)
    msg["From"]=user
    msg["To"]=to
    msg["Subject"]= subject
    try:
        smtpServer= smtplib.SMTP("smtp.gmail.com",587)
        print("[+]Conectando con el servidor....")
        smtpServer.ehlo()
        print("[+]Iniciando la sesion Encriptada....")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+]Loging en el servidor....")
        smtpServer.login(user,pwd)
        print("[+]Enviando mail....")
        smtpServer.sendmail(user,to,msg.as_string())
        smtpServer.close()
        print("[+]Se envio el email correctamente")
        logging.info("Se envio el correo con exito")
    except Exception as e:
        logging.error("Ocurrio un error al enviar el correo: "+str(e))
        print("[-]Error al enviar el mail "+str(e))

#Ubicacion por coordenadas
def UC(key,lat, lon):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.reverse_geocode(lat, lon)
        pprint(results)
        MyMap=folium.Map(location=[lat,lon],zoom_start=15)
        folium.Marker([lat,lon]).add_to(MyMap)
        MyMap.save("location.html")
        filename="file:///"+os.getcwd()+"/"+"location.html"
        webbrowser.open_new_tab(filename)
        logging.info("Finalizo la geolocalizacion con exito")
    except Exception as e:
        logging.error("Ocurrio un error con la ubicacion: "+str(e))
        print("Ocurrio un error: "+str(e))


