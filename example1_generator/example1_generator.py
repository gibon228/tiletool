import tiletool
import pygame
window=pygame.display.set_mode((700, 640)) #creating the window(создаем окно)


b1=tiletool.TileTool([3,3],120,120,fill=1)
"""
Creating the first TileTool object with width,height = 3 tiles in (120,120) coordinates with fill enabled.
(Cоздаем первый объект TileTool с шириной и длиной = 3 тайлам в координатах(120,120) с включенной заливкой.)
"""


b1.fill_dict((1,0),('platform2.png','Empty'))
"""
Matching the default for the object created with generator '1' key(where we have tiles) and '0' key(where we leave empty space) with an image and 'Empty'.
(Cвязываем используемые для созданных генератором объектов ключи '1'(где есть тайлы) и '0'(где мы оставляем пустое пространство) с изображением и 'Empty'(показываем, что этот ключ
означает пустое пространство.)
"""


b2=tiletool.TileTool([4,4],300,300)
"""
Creating second TileTool object with width,height = 4 tiles in (300,300) coordinates with no fill.
(Cоздаем второй объект TileTool с шириной и длиной = 4 тайлам в координатах(300,300) без заливки.)
"""


b2.fill_dict((1,0),('platform.png','Empty'))
"""
Doing the same matching as with the first object but with another picture.
(Делаем связку, аналогичную с первым оюъектом, но используем другую картинку.)
"""

while True:
    window.fill((0,0,0)) #Filling the window black to clear the mark of the moving object. (Заливаем окно черным для очистки следа от движущегося объекта.)

    b1.blit_tiles(window)
    b2.blit_tiles(window)
    """
    Displaying both objects on the window.
    (Отображаем оба объекта в окне.)
    """


    b2.moving_tile((300,300),1,500,'HORIZONTAL',window)
    """
    Our b2 object will move horizontally from (300,300) to (500,300) with speed 1(minimal speed). If it is too fast, you can set the fps higher with time module.
    (Объект b2 будет двигаться горизонтально от точки(300,300) до (500,300) с минимальной скоростью 1. Если это слишком быстро, можно настроить частоту кадров с помощью модуля time.)
    """
    
    for i in pygame.event.get():                            
        if i.type == pygame.QUIT:
            pygame.quit()
    #Checking the events like mouse clicks, window exit etc. In here only the window exit is checked. It is a part of pygame program minimum.
    #(Проверяет события(например нажатия мыши, закрытие окна и т.д). Здесь проверяется только закрытие окна. Является частью минимального каркаса программы на pygame.)


    pygame.display.update() #Updating the display. (Обновляем экран.)
