import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logging.basicConfig(filename="app.log",level=logging.INFO)

class Web_Scraping:
    def ScrapingImg(self,url):
        print("Obteniendo imagenes de la url: "+ url)
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)
            images = parsed_body.xpath('//img/@src')
            print ('Imagenes %s encontradas' % len(images))
            os.system("mkdir imagenes ")
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                r = requests.get(download)
                f = open('imagenes/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
            logging.info("Se descargo la imagen exitosamente")    
        except Exception as e:
            logging.error("Ocurrio un error al descargar la imagen: "+str(e))
            print ("Error de conexion con " + url)
            pass
            
    def ScrapingPDF(self,url):
        print("Obteniendo pdfs de la url: "+ url)
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
            if len(pdfs) >0:
                os.system("mkdir pdf_encontrados")
            print ('Encontrados %s pdf' % len(pdfs))
                
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                r = requests.get(download)
                f = open('pdf_encontrados/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
            logging.info("Se descargo el PDF exitosamente")
        except Exception as e:
            logging.error("Ocurrio un error al descargar el PDF "+str(e))
            print("Error conexion con " + url)
            pass
        
    def ScrapingLinks(self,url):
            now = datetime.now()
            print("\nObteniendo links de la url:"+ url)
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)
                links = parsed_body.xpath('//a/@href')
                print('links %s encontrados' % len(links))
                f = open("Links.txt", 'a')
                f.write(str(now))
                f.write("\n")
                for link in links:
                    f.write(str(link))
                    f.write("\n")
                f.close
                logging.info("Se obtuvieron los links exitosamente")
            except Exception as e:
                logging.error("Ocurrio un error al obtener los links: "+str(e))
                print("Error conexion con " + url)
                pass
