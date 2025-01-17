# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
from PIL import Image

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'OCR_Tesseract', 'libs')
sys.path.append(cur_path)
cur_path = os.path.join(base_path, 'modules', 'OCR_Tesseract', 'tesseract')
sys.path.append(cur_path)

import pyocr
import pyocr.tesseract
import pyocr.builders

"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "gettext":

    image = GetParams("image")
    result = GetParams("result")

    try:
        pyocr.tesseract.TESSERACT_CMD = os.path.join(base_path,  'modules', 'OCR_Tesseract', 'Tesseract-OCR', 'tesseract.exe')
        img = Image.open(image)
        w,h = img.size
        if w<= 200 or h <= 50:
            img = img.resize((w*10, h*10))
        tool = pyocr.get_available_tools()[0]
        lang = tool.get_available_languages()[0]
        # print(lang)
        # print(pyocr.tesseract.psm_parameter())
        # print("*", pyocr.builders.TextBuilder())
        text = tool.image_to_string(
            img,
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )

        if result:
            SetVar(result, text)


    except Exception as e:
        PrintException()
        raise e

    


