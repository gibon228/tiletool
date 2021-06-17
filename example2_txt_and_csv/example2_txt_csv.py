import tiletool
import pygame
window=pygame.display.set_mode((800, 800))

b1=tiletool.TileTool('test.csv',100,100)
"""
Creating an object based on a csv file(file with divider) in (100,100) coordinates.
(Cоздаем объект на основе csv-файла(файла с разделителем) в координатах(100,100).)
"""


b1.fill_dict((42,21,0),('platform2.png','platform.png','empty'))
"""
Matching the keys from the file with images and "empty" for 0.
(Связываем ключи из файла с картинками, для 0 передаем "empty").
"""

b2=tiletool.TileTool('temp.txt',0,0)
"""
Creating an object based on a txt file with divider in (0,0) coordinates.
(Cоздаем объект на основе txt-файла с разделителем в координатах(0,0).)
"""

b2.fill_dict((10,-1),('platform.png','empty'))
"""
Matching the keys from the file with images and "empty" for -1.
(Cвязываем ключи из файла с картинками, для -1 передаем "empty".)
"""

while True:
    window.fill((0,0,0))#filling the window black to clear the mark of the moving object(заливаем окно черным для очистки следа от движущегося объекта)

    b1.blit_tiles(window)
    b2.blit_tiles(window)
    """
    Displaying both objects on the window.
    (Oтображаем оба объекта в окне.)
    """


    b1.moving_tile((300,500),1,500,'HoriZONTAL',window)
    """
    Our b1 object will move horizontally from (300,500) to (500,500) with speed 1(minimal speed). If it is too fast, you can set the fps higher with clock module.
    (Oбъект b1 будет двигаться горизонтально от точки(300,500) до (500,500) с минимальной скоростью 1. Если это слишком быстро, можно настроить частоту кадров с помощью модуля clock.)
    """

    
    for i in pygame.event.get():                            
        
            if i.type == pygame.QUIT:
                      
                pygame.quit()
    
    #Checking the events like mouse clicks, window exit etc. In here only the window exit is checked. It is a part of pygame program minimum.
    #(Проверяет события(например нажатия мыши, закрытие окна и т.д). Здесь проверяется только закрытие окна. Является частью минимального каркаса программы на pygame.)
    


    pygame.display.update()#Updating the display.(Обновляем экран.)
