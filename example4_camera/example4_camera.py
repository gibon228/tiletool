import tiletool
import pygame
window=pygame.display.set_mode((700, 640))

b1=tiletool.TileTool('desert.tmx',0,0,layer=1)
"""
Creating a TileTool object based on the first layer of a .tmx file.
(Cоздаем объект класса TileTool на основе первого слоя .tmx файла.)
"""


filename=pygame.image.load('platform.png').convert_alpha() #Loading an image and converting it to suitable format, now we have the filename of the converted image in filename variable.
#(Загружаем изображение и конвертируем его в подходящий формат, теперь в переменной filename находится имя сконвертированного файла.)
f1=tiletool.platforms_objects(100,20,filename)
"""
Creating a platforms_objects object, the camera will follow it.
(Cоздаем объект класса platforms_objects, за ним будет следовать камера.)
"""


"""
Next 2 lines limit the frames per second figure(for clear view).
(Cледующие 2 строчки ограничивают частоту кадров в секунду(для ясного представления).)
"""
clock = pygame.time.Clock()
fps = 300


camera_obj=tiletool.camera(1000,1000,f1)
"""
The camera will follow the f1 object in coordinates x(0-1000) and y(0-1000). Beyond that range the object will go beyond the screen.
(Kамера будет следить за объектом f1 в координатах (0-1000) по x и (0-1000) по y. При выходе из этих координат объект выйдет за пределы экрана.)
"""

while True:
    window.fill((0,0,0))#Filling the window black to clear the mark of the moving object. (Заливаем окно черным для очистки следа от движущегося объекта.)
    clock.tick(fps)#Setting the speed of the screen update. (Настраиваем скорость обновления экрана.)

    b1.blit_tiles(window,camera_obj)
    """
    Displaying the object in the window. It is crucial to pass the camera class object in every blit_tiles call.
    (Oтображаем объект в окне. Необходимо передать объект класса camera во все вызовы blit_tiles.)
    """


    window.blit(f1.image,camera_obj.drawCam(f1))
    """
    Displaying the platforms_objects object in the window. You should pass the call of drawCam as shown instead of object.rect so the object can be blit in the coordinates needed
    for camera.
    (Oтображаем объект platforms_objects в окне. Следует передать вызов метода drawCam,как в примере вместо свойства rect объекта, чтобы объект мог отображаться в координатах,
    нужных камере.)
    """
    

    for i in pygame.event.get():                            
        
            if i.type == pygame.QUIT:
                      
                pygame.quit()
   
    #Checking the events like mouse clicks, window exit etc. In here only the window exit is checked. It is a part of pygame program minimum.
    #(Проверяет события(например нажатия мыши, закрытие окна и т.д). Здесь проверяется только закрытие окна. Является частью минимального каркаса программы на pygame.)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
           f1.rect.x-=1
          
    elif keys[pygame.K_RIGHT]:
           f1.rect.x+=1

    elif keys[pygame.K_DOWN]:
           f1.rect.y+=1

    elif keys[pygame.K_UP]:
           f1.rect.y-=1
    """
    These lines make the f1 object movable, use your arrows to move.
    (Эти сторочки отвечают за движение объекта, используйте стрелки для движения.)
    """
    pygame.display.update()#Updating the display.(Oбновляем экран.)

