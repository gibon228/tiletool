Properties and object creation
==========





 Creating an object from external file.
 
object = TileTool('filename',**layer=1)

**filename** - file format: 

-.csv(file with separator) 

-.tmx(format of XML files. Can be created in Tiled editor.) 

-.txt(text file with separator)


**layer** - int, layer number from .tmx file. Used only with .tmx files.





 Generating a frame or a simple rectangle of tiles.

object = TileTool([x,y],0)

**[x,y]** - list, where x is the width of the generating object and y is the height(in tiles).


 Object properties.

**object.matrix** - 2-dimensional array, matrix storing tiles IDs, inner lists are matrix' rows.

**object.layers** - number of layers in .tmx file.

**object.dictionary** - dictionary where the keys are tile IDs, values are the pictures connected to them. It is filled after the call of fill_dict() method.

