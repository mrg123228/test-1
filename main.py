#gazenbord
from os import times_result
import pygame, random #importen van pygame
import random
#--------globale variable------------

#coordinaten van de vakjes
vakjes = [[135, 537], [230, 540], [278, 541], [323, 540], [371, 541], [414, 541],[468, 542], [517, 541], [566, 537], [616, 515], [658, 478], [690, 437], [707, 390], [719, 342], [721, 285], [713, 227], [695, 182], [670, 141],[624, 95], [559, 63], [504, 62], [455, 62], [412, 62], [365,62], [317, 61],[275, 63], [231, 64], [180, 85], [146, 112], [118, 149], [98, 190],[88, 242], [90, 299], [98, 350], [123, 389], [152, 428], [189, 457],[236, 469], [280, 471], [322, 471], [370, 470], [417, 468], [469, 470],[523, 469], [567, 462], [611, 423], [640, 371], [649, 323], [649, 273],[635, 228], [599, 176], [551, 143], [486, 141], [422, 137], [367, 137],[318, 137], [270, 137], [227, 144], [176, 191], [158, 270], [170, 328],[195, 367], [238, 388], [403, 295]]


#pion posities
posities = [0,0]

#wie is er aan de beurt
beurt = 0

# dobbelworp
worp = 0

#bord afbeelding
bord = pygame.image.load('F1bord.png')

#--------pygame initialisatie--------
#pygame inicialiseren
pygame.init()
#afmetingen spelscherm(pi{br,ho})
WINDOW_SIZE = [1200, 800]
#maken van speelscherm
screen = pygame.display.set_mode(WINDOW_SIZE)
#er voor zorgen dat het spel blijft lopen
done = False
#het maken van een klok
clock = pygame.time.Clock()


#--------hoofdloop van het prograam--
while not done:
  #check gebeurtenisen
  for event in pygame.event.get(): #doorloop alle gebeurtenissen sinds de vorige schermupdate
    if event.type == pygame.QUIT: #Het kruisje is aangeklikt
      done = True 
    elif event.type == pygame.KEYDOWN:
    #er is een toets ingedrukt, we kijken welke en ondernemen actie
      if event.key == pygame.K_SPACE: #spatie
        print ("knop: spatie")

        worp = random.randint(1,6) # kiest een getal tussen 1 en 6
        posities[beurt] += worp # verzet pion die aan de beurt is

      #verzin iets slim om de beurt over te geven 
      if beurt == 0:
        beurt +=1 
      elif beurt == 1:
        beurt = beurt - 1
      elif event.key == pygame.K_BACKSPACE:
        print("Knop: Backspace")
        posities = [0,0]

  #teken graphics
  screen.fill((255,255,255)) #begint met wite achtergrond

  bordrect = bord.get_rect() #vraagt afmetingen van het bordplaatje
  screen.blit(bord, bordrect) #teken het bord op het scherm

  #teken pionnen als gekleurde cirekels op de coordinaten van de vakjes waar ze staan
  speler0_x = vakjes[posities[0]][0]; #x-cordinaat spler op 0
  speler0_y = vakjes[posities[0]][1]; #y-cordinaat speler op 0  
  kleur0 = (0,255,0) #groen
  pygame.draw.circle(screen, kleur0, (speler0_x, speler0_y),10) #teken cirkel  als pion 0 is
  speler1_x = vakjes[posities[1]][0]+5; #x-cordinaat spler op 1
  speler1_y = vakjes[posities[1]][1]+5; #y-cordinaat speler op 1  
  kleur1 = (0,0,255) #blauw
  pygame.draw.circle(screen, kleur1, (speler1_x, speler1_y),10) #teken cirkel  als pion 2 is
  speler2_x = vakjes[posities[0]][0]+10; #x-cordinaat spler op 2
  speler2_y = vakjes[posities[0]][1]+5; #y-cordinaat speler op 2
  kleur2 = (255,0,0) #rood
  pygame.draw.circle(screen, kleur2, (speler2_x, speler2_y),10) #teken cirkel  als pion 1 is
  speler3_x = vakjes[posities[1]][0]+5; #x-cordinaat spler op 3
  speler3_y = vakjes[posities[1]][1]+10; #y-cordinaat speler op 3  
  kleur3 = (155,0,0) #blauw
  pygame.draw.circle(screen, kleur3, (speler3_x, speler3_y),10) #teken cirkel  als pion 1 is
  #update beeldscherm
  pygame.display.flip() #ververst scherm
  clock.tick(60) #limit beeldscherm

#--------afsluiting------------------
pygame.quit()

