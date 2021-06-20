
Methods
==========
**object.print_matrix()** - prints object.matrix in the console as a clear 2-dimensional list

**object.fill_dict(keys,values)** - sets the relationship of tile number and image file(JPG/JPEG, PNG). keys - tile IDs in tuple format, values - file names(JPG/JPEG, PNG) in 
tuple format according to the keys. If tile needs to be left without image, pass 'empty' instead of a filename. If the object is created using the generator, pass 1 and 0 into 
keys (1 for the image, 0 for empty space).

*example:*

*cc.fill_dict((1,0),('platform2.png','empty'))*

**object.blit_tiles(window,** ***object_camera)** - display object in window. If the camera needs to follow any object, pass the camera class object in object_camera argument of all TileTool objects. 

**object.create_obj_matrix()** - creates matrix storing each tile as a pygame class object.

**object.paint_tile(x,y,color)** - creates a tile in coordinates(x*tile width,y*tile height) colored in RGB format - i.e (255,255,255) and displays it on screen. Created tile is not an individual object.

**object.moving_tile(coord,speed,border,direction,window)** - when called out in infinite loop, object will move in window from starting coordinates (coord) in the tuple to the border (in pixels). Pass "HORIZONTAL" in direction for moving horizontally, "VERTICAL" for moving vertically. Minimal speed is 1.

*example:*

*object.moving_tile((50,50),1,10,window)*
