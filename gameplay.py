import pygame
import random
from Dino import Dino
from Obstacles import Cactus, Ptera
from Ground import Ground
from Krasivosti import Star, Scoreboard, Cloud
from Source import Source

class Gameplay:
    high_score = 0
    si = 0

    def introscreen():

        temp_dino = Dino(44, 47)
        temp_dino.isBlinking = True
        gameStart = False

        temp_ground, temp_ground_rect = Source.LoadSpriteSheet('ground.png', 15, 1, 60, 20, -1)
        temp_ground_rect.left = Source.width / 20
        temp_ground_rect.bottom = Source.height

        logo, logo_rect = Source.LoadImage('adv.png', 470, 300, -1)
        logo_rect.centerx = Source.width * 0.6
        logo_rect.centery = Source.height * 0.5

        skin, skin_rect = Source.LoadImage('skin sign.png', 110, 60, -1)
        skin_rect.centerx = Source.width * 0.11
        skin_rect.centery = Source.height * 0.6

        while not gameStart:
            if pygame.display.get_surface() == None:
                return True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            temp_dino.isJumping = True
                            temp_dino.isBlinking = False
                            temp_dino.movement[1] = -1 * temp_dino.jumpSpeed
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if mouse[0] > 11 and mouse[0] < 121 and mouse[1] > 150 and mouse[1] < 210:
                            Gameplay.si += 1
                            temp_dino = Dino(44, 47, Gameplay.si % 3)
                            temp_dino.isBlinking = True

            temp_dino.update()

            if pygame.display.get_surface() != None:
                Source.screen.fill(Source.background_col)
                Source.screen.blit(temp_ground[0], temp_ground_rect)
                if temp_dino.isBlinking:
                    Source.screen.blit(logo, logo_rect)
                    Source.screen.blit(skin, skin_rect)
                temp_dino.draw()

                pygame.display.update()

            Source.clock.tick(Source.FPS)
            if temp_dino.isJumping == False and temp_dino.isBlinking == False:
                gameStart = True

    def gameplay():
        # peremenni
        gamespeed = 4
        startMenu = False
        gameOver = False
        gameQuit = False
        playerDino = Dino(44, 47, Gameplay.si % 3)
        new_ground = Ground(-1 * gamespeed)
        scb = Scoreboard()
        highsc = Scoreboard(Source.width * 0.78)
        counter = 0
        # obstacles.memory
        cacti = pygame.sprite.Group()
        pteras = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        stars = pygame.sprite.Group()

        last_obstacle = pygame.sprite.Group()

        Cactus.containers = cacti
        Ptera.containers = pteras
        Cloud.containers = clouds
        Star.containers = stars
        # pictures
        retbutton_image, retbutton_rect = Source.LoadImage('replay_button.png', 35, 31, -1)
        gameover_image, gameover_rect = Source.LoadImage('game_over.png', 190, 11, -1)
        # Score
        temp_images, temp_rect = Source.LoadSpriteSheet('numbers.png', 12, 1, 11, int(11 * 6 / 5), -1)
        HI_image = pygame.Surface((22, int(11 * 6 / 5)))
        HI_rect = HI_image.get_rect()
        HI_image.fill(Source.background_col)
        HI_image.blit(temp_images[10], temp_rect)
        temp_rect.left += temp_rect.width
        HI_image.blit(temp_images[11], temp_rect)
        HI_rect.top = Source.height * 0.1
        HI_rect.left = Source.width * 0.73

        while not gameQuit:
            while startMenu:
                pass
            while not gameOver:
                if pygame.display.get_surface() == None:
                    gameQuit = True
                    gameOver = True
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                                if playerDino.rect.bottom == int(0.98 * Source.height):
                                    playerDino.isJumping = True
                                    if pygame.mixer.get_init() != None:
                                        Source.jump_sound.play()
                                    playerDino.movement[1] = -1 * playerDino.jumpSpeed

                            if event.key == pygame.K_DOWN:
                                if not playerDino.isDead:  # not playerDino.isJumping and
                                    playerDino.isDucking = True
                                    Source.duck_sound.play()

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                playerDino.isDucking = False
                # is_Dead?
                for c in cacti:
                    c.movement[0] = -1 * gamespeed
                    if pygame.sprite.collide_mask(playerDino, c):
                        playerDino.isDead = True
                        Source.die_sound.play()

                for p in pteras:
                    p.movement[0] = -1 * gamespeed
                    if pygame.sprite.collide_mask(playerDino, p):
                        playerDino.isDead = True
                        Source.die_sound.play()
                # dobavlenie_obstacles
                if len(cacti) < 2:
                    if len(cacti) == 0:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(gamespeed, 85, 60))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < Source.width * 0.7 and random.randrange(0, 50) == 10:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(gamespeed, 85, 60))

                if len(pteras) == 0 and random.randrange(0, 200) == 10 and counter > 500:
                    for l in last_obstacle:
                        if l.rect.right < Source.width * 0.8:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(gamespeed, 46, 40))

                if len(clouds) < 5 and random.randrange(0, 300) == 10:
                    Cloud(Source.width, random.randrange(Source.height / 5, Source.height / 2))

                if len(stars) == 0:
                    Star(600, 0)
                # update
                playerDino.update()
                cacti.update()
                pteras.update()
                clouds.update()
                stars.update()
                new_ground.update()
                scb.update(playerDino.score)
                highsc.update(Gameplay.high_score)
                # draw
                if pygame.display.get_surface() != None:
                    Source.screen.fill(Source.background_col)
                    new_ground.draw()
                    stars.draw(Source.screen)
                    clouds.draw(Source.screen)
                    scb.draw()
                    if Gameplay.high_score != 0:
                        highsc.draw()
                        Source.screen.blit(HI_image, HI_rect)
                    cacti.draw(Source.screen)
                    pteras.draw(Source.screen)
                    playerDino.draw()

                    pygame.display.update()
                Source.clock.tick(Source.FPS)
                # HS_update
                if playerDino.isDead:
                    Star.ni = 0
                    gameOver = True
                    if playerDino.score > Gameplay.high_score:
                        Gameplay.high_score = playerDino.score
                # speed
                if counter % 700 == 699:
                    new_ground.speed -= 1
                    gamespeed += 1

                counter = (counter + 1)

            if gameQuit:
                break

            while gameOver:
                if pygame.display.get_surface() == None:
                    gameQuit = True
                    gameOver = False
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                gameQuit = True
                                gameOver = False

                            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                                gameOver = False
                                Gameplay.gameplay()
                highsc.update(Gameplay.high_score)
                if pygame.display.get_surface() != None:
                    Source.DispGameOver(retbutton_image, gameover_image)
                    if Gameplay.high_score != 0:
                        highsc.draw()
                        Source.screen.blit(HI_image, HI_rect)
                    pygame.display.update()
                Source.clock.tick(Source.FPS)

        pygame.quit()
        quit()