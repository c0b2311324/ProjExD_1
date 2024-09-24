import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img= pg.image.load("fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img,True,False)
    character_img=pg.image.load("fig/3.png")
    character_img=pg.transform.flip(character_img,True,False)
    character_rect=character_img.get_rect()
    character_rect.center=300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        character_first_place_becide=-1
        character_first_place_vertical=0
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            character_first_place_vertical=-1
        elif key_lst[pg.K_DOWN]:
            character_first_place_vertical=+1
        else:
            character_first_place_becide=0
        if key_lst[pg.K_LEFT]:
            character_first_place_becide=-1
        elif key_lst[pg.K_RIGHT]:
            character_first_place_becide=+2
        else:
            character_first_place_vertical=0
        character_rect.move_ip(character_first_place_becide,character_first_place_vertical)

        x=-(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2,[x+1600,0])
        screen.blit(bg_img,[x+3200,0])
        screen.blit(bg_img2,[x+4800,0])
        screen.blit(character_img,character_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()