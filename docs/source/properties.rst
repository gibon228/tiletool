Properties and object creation
==========
ENG

object = TileTool('filename',**layer=1)
---
Creating an object from external file.

filename - file format: 
-.csv(file with separator) 
-.tmx(format of XML files. Can be created in Tiled editor.) 
-.txt(text file with separator)

layer - int, layer number from .tmx file. Used only with .tmx files.

---
object = TileTool([x,y],0)

 Generating a frame or a simple rectangle of tiles.


[x,y] - list, where x is the width of the generating object and y is the height(in tiles).

---
Object properties.

object.matrix - 2-dimensional array, matrix storing tiles IDs, inner lists are matrix' rows.
object.layers - number of layers in .tmx file.
object.dictionary - dictionary where the keys are tile IDs, values are the pictures connected to them. It is filled after the call of fill_dict() method.

RUS

object = TileTool('filename',**layer=1)
---
Создание объекта из внешнего файла.

filename - файл формата: 
-.csv(файл с разделителем) 
-.tmx(формат файлов XML. Может быть создан в редакторе Tiled.) 
-.txt(текстовой файл с разделителем)

layer - int, номер слоя из .tmx файла. Используется только с tmx файлами

---
object = TileTool([x,y],0)

 Генерация рамки или простого прямоугольника из тайлов.


[x,y] - список, где x - ширина создаваемого объекта, y - высота в тайлах.
0 - будет создана рамка(фигура без заливки внутри), 1 - прямоугольник. Значение по умолчанию - 0.
---
Свойства объекта.

object.matrix - двумерный массив, матрица, хранящая id тайлов, вложенные списки - строки матрицы.
object.layers - количество слоев в файле tmx
object.dictionary - словарь, в котором ключи - id тайлов, значения - картинки, привязанные к ним. Заполняется после вызова метода fill_dict()
