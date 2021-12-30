import pygame
import warnings
from pygame import*
import base64 
import zlib
import xml.etree.ElementTree as ET


warnings.filterwarnings("ignore")

class camera(object):
        def __init__(self,w,h,player):
                self.sets=self.defSettings
                self.connected=player
                self.state=Rect(0,0,w,h)

        def updateCam(self):
            self.state=self.sets(self.state,self.connected.rect)

        def drawCam(self,obj):
            return obj.rect.move(self.state.topleft)

        def defSettings(self,camera, target_rect):
            l, t, _, _ = target_rect
            _, _, w, h = camera
            l, t = -l+pygame.display.get_surface().get_width() / 2, -t+pygame.display.get_surface().get_height() / 2
            l = min(0, l)
            l = max(-(camera.width-pygame.display.get_surface().get_width()), l)
            t = max(-(camera.height-pygame.display.get_surface().get_height()), t)
            t = min(0, t)
            return Rect(l, t, w, h)





        
class TileTool(pygame.sprite.Sprite):
    """ TileTool - простой, базовый, основанный на pygame.sprite.Sprite модуль для работы с тайлами. С его помощью можно переносить тайл-уровни и рисунки из файлов множества
поддерживаемых форматов в tile-игры на pygame.
TileTool is a simple, base module for working with tiles, based on pygame.sprite.Sprite. With TileTool you can transfer tile-levels and drawings from different format files to 
tile games created on pygame.
    """
    def __init__(self,file,x,y,fill=0,**layer):
        """object = TileTool('filename',**layer=1)
----
Создание объекта из внешнего файла.

filename - файл формата: 
-.csv(файл с разделителем) 
-.tmx(формат файлов XML. Может быть создан в редакторе Tiled.) 
-.txt(текстовой файл с разделителем)

layer - int, номер слоя из .tmx файла. Используется только с tmx файлами

----
object = TileTool([x,y],0)

 Генерация рамки или простого прямоугольника из тайлов.


[x,y] - список, где x - ширина создаваемого объекта, y - высота в тайлах.
0 - будет создана рамка(фигура без заливки внутри), 1 - прямоугольник. Значение по умолчанию - 0.
----
Свойства объекта.

object.matrix - двумерный массив, матрица, хранящая id тайлов, вложенные списки - строки матрицы.
object.layers - количество слоев в файле tmx
object.dictionary - словарь, в котором ключи - id тайлов, значения - картинки, привязанные к ним. Заполняется после вызова метода fill_dict()


object = TileTool('filename',**layer=1)
----
Creating an object from external file.

filename - file format: 
-.csv(file with separator) 
-.tmx(format of XML files. Can be created in Tiled editor.) 
-.txt(text file with separator)

layer - int, layer number from .tmx file. Used only with .tmx files.

----
object = TileTool([x,y],0)

 Generating a frame or a simple rectangle of tiles.


[x,y] - list, where x is the width of the generating object and y is the height(in tiles).

----
Object properties.

object.matrix - 2-dimensional array, matrix storing tiles IDs, inner lists are matrix' rows.
object.layers - number of layers in .tmx file.
object.dictionary - dictionary where the keys are tile IDs, values are the pictures connected to them. It is filled after the call of fill_dict() method.

        """
        super().__init__()
        self.matrix=[]
        self.x=x
        self.y=y
        self.empty_list=[]
        self.group=pygame.sprite.Group()
        self.dictionary={}
        self.pic_h=0
        self.pic_w=0
        self.layers=0
        if layer!={}:
                self.layer=layer['layer']
        else:
                self.layer=0
        self.obj_matrix=[]
        self.moved_distance=0.0
        self.moving_direction='RIGHT'
       
        if isinstance(file,str):
            self.opened_file=open(file,'r')
            self.filetype=file.split('.')[1]
            if self.filetype=='csv' or self.filetype=='txt':
                self.matrix=self.transform_csv_and_txt()
            elif self.filetype=='tmx':
                if self.layer==0:
                        print('Передайте номер слоя тайлов: object = TileTool("filename",**layer=1)')
                        return None
                self.matrix=self.transform_tmx_to_csv()
                self.create_obj_matrix()
        else:
           
            inner_list=[]
            if fill==0:
                    for i in range(file[1]):
                        for j in range(file[0]):
                            if i==0 or i==file[1]-1:
                                inner_list.append('1')
                            else:
                                if j==0 or j==file[0]-1:
                                    inner_list.append('1')
                                else:
                                    inner_list.append('0')
                        self.matrix.append(inner_list)
                        inner_list=[]
            else:
                    for i in range(file[1]):
                        for j in range(file[0]):
                            
                                inner_list.append('1')
                            
                        self.matrix.append(inner_list)
                        inner_list=[]
        
                
        
    def transform_tmx_to_csv(self):
        tree = ET.parse(self.opened_file).getroot()
        data_encoding=tree.find('layer/data').get('encoding')
        for i in range(1,len(tree.findall('layer/data'))+1):
                self.layers+=1
        if self.layer>self.layers:
                print("введите номер существующего слоя")
                return [[]]
        if data_encoding=='base64':
            for i in range(1,len(tree.findall('layer/data'))+1):
            
                
                
                if i==self.layer:
                
                    
                    
                    layer_width=int(tree.findall('layer')[i-1].get('width'))
                    unencoded_data = base64.b64decode(tree.findall('layer/data')[i-1].text)
            unzipped_data = zlib.decompress(unencoded_data)
            tile_grid=[[]]
            byte_count = 0
            int_count = 0
            int_value = 0
            row_count = 0
            
            for byte in unzipped_data:
                int_value += byte << (byte_count * 8)
                byte_count += 1
                if not byte_count % 4:
                    byte_count = 0
                    int_count += 1
                    
                    tile_grid[row_count].append(int_value-1)
                    
                    int_value = 0
                    if not int_count % layer_width:
                        row_count += 1
                        tile_grid.append([])

            tile_grid.pop()
            self.opened_file=''
            
            for i in tile_grid:
                for j in i:
                    self.opened_file+=str(j)    
                    self.opened_file+=','
                self.opened_file+='\n'
            self.opened_file=self.opened_file[:-1]
            
            
        if data_encoding=='csv':
            for i in range(1,len(tree.findall('layer/data'))+1):
            
                
            
                if i==self.layer:
                
                    self.opened_file=tree.findall('layer/data')[i-1].text
                
        for i in range(1,len(tree.findall('layer'))+1):
            if i==self.layer:
                self.length=tree.findall('layer')[i-1].get('width')
        temp_file=open('temp.txt','w')
       
        temp_file.write(self.opened_file)
        temp_file.close()
        self.opened_file=open('temp.txt','r')
        self.transform_tsx(tree)
        return tile_grid
            
    def transform_csv_and_txt(self):

        a=self.opened_file.readlines()
       
        return self.check_file(a)


    def transform_tsx(self,tree_obj):
        
        found_pics=tree_obj.findall('tileset')
        
        for i in range(len(found_pics)):
            bush = ET.parse(open(found_pics[i].get('source'),'r')).getroot()
            keys_tuple=()
            values_tuple=()
            
            if bush.get('tilecount')=="1":
                
                self.fill_dict((found_pics[i].get('firstgid'),),(bush.find('image').get('source'),))
            else:
                
                
                piclist=[]
                    
                fff=pygame.image.load(bush.find('image').get('source')).convert_alpha()
                    
                pyig=pygame.Surface((int(bush.get('tilewidth')),int(bush.get('tileheight'))))
                found_ids=bush.findall('tile')
                
                for i in range(len(found_ids)):
                    piclist.append(pygame.Surface((int(bush.get('tilewidth')),int(bush.get('tileheight')))))
                   
                    piclist[i].blit(fff,(0,0),(int(found_ids[i].get('id'))%int(bush.get('columns'))*int(bush.get('tilewidth'))+int(bush.get('margin'))*int(found_ids[i].get('id'))%int(bush.get('columns')),int(found_ids[i].get('id'))//int(bush.get('columns'))*int(bush.get('tileheight'))+int(bush.get('margin'))*int(found_ids[i].get('id'))//int(bush.get('columns')),32,32))
    
                    self.fill_dict((found_ids[i].get('id'),),(piclist[i],))
                   
                    pygame.display.update()
        self.create_obj_matrix()
                
    def transform_excel(self):
        pass
        return self.check_file(a)
    
    def check_file(self,file):
        matrix0=[]
        

        for i in file:
            if i=='\n':
                file.remove(i)
        file_1st=file[0].replace('\n','').split(',')
        for i in range(len(file_1st)):
                if file_1st[i]=='':
                    file_1st.pop(i)
        
        self.length=len(file_1st)
        for i in file:
            
            b = i.replace('\n','')
            b = b.split(',')
            for j in range(len(b)):
                if b[j] == '':
                    b.pop(j)
            s = len(b)
           
            
            if s!=self.length:
                print('incorrect length of a line ')
                self.length='error'
                self.height='error'
                break
            else:
                self.height=len(file)
                self.length=len(b)


        
            

        for i in range(len(file)):
            file[i]=file[i].replace('\n','')
            file_1st=file[i].split(',')
            
            for j in range(len(file_1st)):
                if file_1st[j]=='':
                    file_1st.pop(j)
            matrix0.append(file_1st)
        return matrix0



    def print_matrix(self):

        """object.print_matrix() - выводит object.matrix в консоли в виде наглядного двухмерного списка

object.print_matrix() - prints object.matrix in the console as a clear 2-dimensional list 
        """
        maxdigits=0
        notinthelist=False
        for i in self.matrix:#определяет максимальную длину элемента
            for j in i:
                if len(j)>maxdigits:
                    maxdigits=len(j)
                if i==0 and j==0:
                    self.dictionary[j]=0
                for d in self.dictionary:
                    if j==d:
                        notinthelist=True
                if notinthelist!=True:
                    self.dictionary[j]=0
                notinthelist=False
        
        for i in range(len(self.matrix)):#выводит на экран матрицу
            for j in range(len(self.matrix[i])):
                print(' '*(maxdigits-len(self.matrix[i][j]))+self.matrix[i][j],end=' ')
            print()
    def fill_dict(self,keys,values):

        """object.fill_dict(keys,values) - устанавливает соответствие номера тайла с файлом изображения(JPG/JPEG, PNG). keys - id тайлов в формате tuple, values -
- имена файлов(JPG/JPEG, PNG) в формате tuple, соответствующие ключам. Если требуется оставить тайл без картинки, вместо имени файла передать 'empty'.
пример:
cc.fill_dict((1,0),('platform2.png','empty'))

object.fill_dict(keys,values) - sets the relationship of tile number and image file(JPG/JPEG, PNG). keys - tile IDs in tuple format, values -
- file names(JPG/JPEG, PNG) in tuple format according to the keys. If tile needs to be left without image, pass 'empty' instead of a filename.
example:
cc.fill_dict((1,0),('platform2.png','empty'))
        """
        if len(keys)!=len(values):
                print('разное количество переданных ключей и значений')
                return 0
        transp_surface=pygame.Surface((self.pic_w,self.pic_h))
        transp_surface.set_alpha(0)
        self.dictionary['-1']=transp_surface
        self.empty_list.append('-1')
        
				
        for i in range(len(keys)):
            
            if isinstance(values[i],pygame.Surface):
                if i==0:
                    
                    self.pic_h=values[i].get_height()
                    self.pic_w=values[i].get_width()
                self.dictionary[str(keys[i])]=values[i]
                if self.dictionary[str(keys[i])].get_height()!=self.pic_h or self.dictionary[str(keys[i])].get_width()!=self.pic_w:
                    print('Incorrect size of a picture')
                    self.pic_h=0
                    self.pic_w=0
                    dictionary={}
                    break
            else:
                if values[i].lower()!='empty':
                    try:
                        opened_file=pygame.image.load(values[i]).convert_alpha()
                    except:
                        print('не удалось найти или открыть файл')
                        return 0
                if i==0 and values[i].lower()!='empty':
				
                    self.pic_h=opened_file.get_height()
                    self.pic_w=opened_file.get_width()
                elif i==0 and values[i].lower()=='empty':
                    print('first value cannot be empty')
                    break
                if values[i].lower()!='empty' :
                    
                    self.dictionary[str(keys[i])]=opened_file
                else:
                    self.dictionary[str(keys[i])]=pygame.Surface((self.pic_w,self.pic_h))
                    self.empty_list.append(str(keys[i]))
                if self.dictionary[str(keys[i])].get_height()!=self.pic_h or self.dictionary[str(keys[i])].get_width()!=self.pic_w:
                    print('Incorrect size of a picture')
                    self.pic_h=0
                    self.pic_w=0
                    dictionary={}
                    break
        self.create_obj_matrix()
    def blit_tiles(self,window,*object_camera):

        """object.blit_tiles(window,*object_camera) - отображение object в окне window. Если за каким-либо объектом должна двигаться камера, в object_camera  всех объектов TileTool 
передать объект класса camera.

object.blit_tiles(window,*object_camera) - display object in window. If the camera needs to follow any object, pass the camera class object in object_camera argument of all
TileTool objects. 

        """
        if len(object_camera)==0 or (len(object_camera)>0  and not(isinstance(object_camera[0],camera))):
            if isinstance(self,platforms_objects):
                window.blit(self.image,self.rect)
            
            else:
                if self.pic_h!=0 and self.pic_w!=0:
                    for i in range(len(self.obj_matrix)):
                        for j in range(len(self.obj_matrix[i])):
                           window.blit(self.obj_matrix[i][j].image,self.obj_matrix[i][j].rect)
            
        else:
            
            for h in self.group:
                
                window.blit(h.image,object_camera[0].drawCam(h))
            object_camera[0].updateCam()
            
    def create_obj_matrix(self):
        
        """object.create_obj_matrix() - создает матрицу, содержащую каждый тайл в виде объекта класса pygame

object.create_obj_matrix() - creates matrix storing each tile as a pygame class object.
        """
        
        inner_obj_list=[]
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                
                platform_obj=platforms_objects(j*self.pic_w + self.x,i*self.pic_h + self.y,self.dictionary[str(self.matrix[i][j])])
                
                inner_obj_list.append(platform_obj)
                
                if not self.matrix[i][j] in self.empty_list:
                    
                    self.group.add(platform_obj)
            self.obj_matrix.append(inner_obj_list)
            inner_obj_list=[]
        
    def paint_tile(self,x,y,color):
        
        """object.paint_tile(x,y,color) - создает тайл в координатах(x*ширина тайла,y*высота тайла) цвета в формате RGB - например (255,255,255) и отображает на экране. Созданный тайл
        не будет отдельным объектом.

        object.paint_tile(x,y,color) - creates a tile in coordinates(x*tile width,y*tile height) colored in RGB format - i.e (255,255,255) and displays it on screen. Created tile
        is not an individual object.
        """
        df=pygame.Surface((self.pic_w,self.pic_h))
        df.fill(color)
        window.blit(df,((x-1)*self.pic_w,(y-1)*self.pic_h))

 

   
    def moving_tile(self,coord,speed,border,direction,window):

        """ object.moving_tile(coord,speed,border,direction,window) - при вызове в бесконечном цикле object будет двигаться в окне window от начальных координат coord в кортеже 
до границы border(в пикселях). В direction передать "HORIZONTAL" для перемещения платформы по горизонтали, "VERTICAL" для перемещения по вертикали. Минимальная скорость - 1.
пример:
object.moving_tile((50,50),1,10,window)

object.moving_tile(coord,speed,border,direction,window) - when called out in infinite loop, object will move in window from starting coordinates (coord) in the tuple 
to the border (in pixels). Pass "HORIZONTAL" in direction for moving horizontally, "VERTICAL" for moving vertically. Minimal speed is 1.
example:
object.moving_tile((50,50),1,10,window)
        """
        if speed < 1:
                speed=1
                
        self.moving_platform_speed=speed
        self.moving_surface=pygame.Surface((len(self.matrix[0])*self.pic_w,len(self.matrix)*self.pic_h))
        if direction.upper() == 'HORIZONTAL':
                
                if self.moving_direction=='LEFT':
                    self.moved_distance-=speed
                    for i in range(len(self.obj_matrix)):
                        for j in range(len(self.obj_matrix[i])):
                             self.obj_matrix[i][j].rect.x-=speed
                             self.obj_matrix[i][j].rect.y=coord[1]+i*self.pic_h
                             
                        
                else:
                    self.moved_distance+=speed
                    for i in range(len(self.obj_matrix)):
                        for j in range(len(self.obj_matrix[i])):
                             self.obj_matrix[i][j].rect.x+=speed
                             self.obj_matrix[i][j].rect.y=coord[1]+i*self.pic_h
                             

                            
                if coord[0]+self.moved_distance>border:
                            
                    self.moving_direction='LEFT'
                    
                elif coord[0]+self.moved_distance<coord[0]:

                    self.moving_direction='RIGHT'
        else:
                if self.moving_direction=='UP':
                    self.moved_distance-=speed
                    for i in range(len(self.obj_matrix)):
                        for j in range(len(self.obj_matrix[i])):
                             self.obj_matrix[i][j].rect.y=coord[1]+self.moved_distance+i*self.pic_h
                             self.obj_matrix[i][j].rect.x=coord[0]+j*self.pic_w
                            
                        
                else:
                    self.moved_distance+=speed
                    for i in range(len(self.obj_matrix)):
                        for j in range(len(self.obj_matrix[i])):
                             self.obj_matrix[i][j].rect.y=coord[1]+self.moved_distance+i*self.pic_h
                             self.obj_matrix[i][j].rect.x=coord[0]+j*self.pic_w
                             

                            
                if coord[1]+self.moved_distance>border:
                            
                    self.moving_direction='UP'
                    
                elif coord[1]+self.moved_distance<coord[1]:

                    self.moving_direction='DOWN'
class platforms_objects(TileTool,pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))          

         
                
            
            
       
            
        
            

    
    

