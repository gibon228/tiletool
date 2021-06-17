import tiletool
import pygame
window=pygame.display.set_mode((800, 800))


b1=tiletool.TileTool('desert1.tmx',0,0,layer=1)
b2=tiletool.TileTool('desert1.tmx',0,0,layer=2)
"""
Creating 2 objects based on .tmx file(xml-format file),but 2 are based on file's different layers. We don't need to call the fill_dict method since we have all the information about
the images matched to keys in .tsx file linked to the .tmx file.
(Cоздание 2 объектов на базе .tmx файла(файла XML-формата), но они основаны на разных слоях этого файла. Нам не нужно вызывать метод fill_dict, так как вся информация о изображениях,
привязанных к ключам,указана в .tsx файле, относящемуся к данному .tmx файлу.)
"""

while True:
    window.fill((0,0,0))#filling the window black to clear the mark of the moving object(заливаем окно черным для очистки следа от движущегося объекта)

    b1.blit_tiles(window)
    b2.blit_tiles(window)
    """
    Displaying both objects on the window.
    (Oтображаем оба объекта в окне.)
    """


    b2.moving_tile((0,0),1,200,'HoriZONTAL',window)
    """
    Our b2 object will move horizontally from (0,0) to (200,0) with speed 1(minimal speed). If it is too fast, you can set the fps higher with clock module.
    (Oбъект b2 будет двигаться горизонтально от точки(0,0) до (200,0) с минимальной скоростью 1. Если это слишком быстро, можно настроить частоту кадров с помощью модуля clock.)
    """
    

    for i in pygame.event.get():                            
        
            if i.type == pygame.QUIT:
                      
                pygame.quit()
    
    #Checking the events like mouse clicks, window exit etc. In here only the window exit is checked. It is a part of pygame program minimum.
    #(Проверяет события(например нажатия мыши,закрытие окна и т.д). Здесь проверяется только закрытие окна. Является частью минимального каркаса программы на pygame.)
    


    pygame.display.update()#Updating the display.(Oбновляем экран.)
