<img align="center" src="https://github.com/user-attachments/assets/cf337f3d-8a4b-4bc7-83e7-c9b053838a26" />


**<div align="center">QA AUTOMATION TALENTO TECH - PRE ENTREGA PROYECTO</div>**


<!-- Descripción -->
## <img width="20" height="20" src="https://raw.githubusercontent.com/HijelHub/GitStrap_SVG_Icons/30c18ea7ca4c0ac2dae00a5dac593b4f49ffa7f6/icons/blue/info-circle.svg"> Descripción  

  Este repositorio contiene tests automatizados realizados como prácticas del curso *QA AUTOMATION*, en el marco del programa Talento Tech. 
  El objetivo es demostrar lo aprendido hasta la clase 8, automatizando casos de pruebas (funcionales y no funcionales) del sitio [www.saucedemo.com ](url)

<!-- Herramientas -->    
## <img width="20" height="20" src="https://raw.githubusercontent.com/HijelHub/GitStrap_SVG_Icons/30c18ea7ca4c0ac2dae00a5dac593b4f49ffa7f6/icons/blue/laptop.svg"> Tecnologías Utilizadas  

  * Python<br>  
  * Pytest para ejecutar pruebas automatizadas<br>  
  * Selenium WebDriver para ejecutar pruebas en navegadores<br>
  * Git y Github para control de versiones

<!-- Instalaciones -->  
## <img width="20" height="20" src="https://raw.githubusercontent.com/HijelHub/GitStrap_SVG_Icons/30c18ea7ca4c0ac2dae00a5dac593b4f49ffa7f6/icons/blue/gear.svg"> Ambiente de Trabajo - Entorno y Configuración  

1. Visual Studio Code

   + Ingresar a [https://code.visualstudio.com/Download](url) y descargar la versión más reciente compatible con el SO
   + Ejecutar instalador y seguir los pasos
   + Se recomienda tildar las opciones Add To Path y Register Code As Editor

2. Python

   + Ingresar a [https://code.visualstudio.com/Download](https://www.python.org/downloads/) y descargar la versión más reciente compatible con el SO
   + Ejecutar instalador y seguir los pasos
   + Tildar la opción Add Python to PATH
   + Verificar la instalación desde la terminal, ejecutando el comando `python --version` lo que deberia retornar un mensaje similar al siguiente `Python 3.xx.x`

3. Extensiones y dependencias
   
   + Se recomienda trabajar e instalar las dependencias en un entorno virtual. <br>[VER MÁS INFORMACIÓN](https://micro.recursospython.com/recursos/como-crear-un-entorno-virtual-venv.html)
   + Desde el menú de extensiones de VSCODE (barra lateral izquierda) buscar la extension Python (desarrollado por Microsoft) y hacer clic en instalar
   + Abrir una terminal en el mismo VSCODE e instalar Pytest ejecutando `pip3 install pytest` y verificar su instalación con `pip3 show pytest`
   + Instalar dependencia que permite la generación de reportes ejecutando `pip install pytest-html`

5. Selenium y WebDriver

   + Ejecutar una terminal e instalar Selenium con el comando `pip install -U selenium`. Verificar la instalación con `pip show selenium`
   + Ingresar a [https://pypi.org/project/selenium/](url) y deslizarse a la opción de Drivers para elegir el correspondiente al navegador deseado para ejecutar las
     pruebas. (En este caso se utilizó Chrome, por lo que se descargó la version Stable desde [https://googlechromelabs.github.io/chrome-for-testing/](url))
   + Descomprimir el archivo descargado y copiar su contenido en la carpeta donde se alojaran los scripts.
   + Instalar WebDriver Manager desde una terminal, con el comando: `pip install webdriver-manager`

<!-- Reportes -->   
## <img width="20" height="20" src="https://raw.githubusercontent.com/HijelHub/GitStrap_SVG_Icons/30c18ea7ca4c0ac2dae00a5dac593b4f49ffa7f6/icons/blue/journal-text.svg"> Ejecución de pruebas y reportes  

 * Desde la terminal integrada de VSCODE y estando en la carpeta raiz del proyecto ejecutar `pytest -s -v` para correr los tests
 * Generar reportes de las pruebas emitidas ejecutando `pytest -v -s --html=reporte.html`
     
   
  
   







