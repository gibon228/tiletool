
Methods
==========
**object.print_matrix()** - prints object.matrix in the console as a clear 2-dimensional list

**object.fill_dict(keys,values)** - sets the relationship of tile number and image file(JPG/JPEG, PNG). keys - tile IDs in tuple format, values - file names(JPG/JPEG, PNG) in 
tuple format according to the keys. If tile needs to be left without image, pass 'empty' instead of a filename. If the object is created using the generator, pass 1 and 0 into 
keys (1 for the image, 0 for empty space).

*example:*

*cc.fill_dict((1,0),('platform2.png','empty'))*

**object.blit_tiles(window,** ***object_camera)** - display object in window. If the camera needs to follow any object, pass the camera class object in object_camera argument of all TileTool objects. 
