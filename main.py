#gazenbord
from os import times_result
import pygame, random #importen van pygame
import random
#--------globale variable------------

#coordinaten van de vakjes
vakjes = [[167, 307], [168, 279], [146, 248], [130, 224], [113, 196], [91, 165], [80, 132], [85, 100], [108, 75], [146, 71], [167, 102], [189, 124], [209, 163], [240, 189], [277, 213], [292, 263], [318, 291], [366, 305], [388,340], [390, 379], [401, 425], [445, 435], [490, 427], [523, 394], [560, 350], [597, 324], [639, 292], [693, 294], [737, 331], [724, 440], [722, 481], [717, 527], [696, 566], [672, 603], [661, 639], [672, 684], [717,678], [739, 654],  [759, 623], [784, 588], [804, 576] ,[835, 551], [880, 551], [914, 564], [942, 595], [960, 632], [970, 663], [988, 693], [1012, 717], [1044, 724], [1090, 706], [1128, 676], [1123, 619], [1075, 580], [1005, 545], [936, 501], [877, 473], [820, 438], [772, 409], [720, 385], [658, 381], [606, 403], [554, 444], [517, 479], [475, 501], [442, 519], [397, 523], [360, 510], [309, 501], [272, 471], [255, 436], [229, 394], [204, 359]]


#pion posities
posities = [0,0,0,0]

#wie is er aan de beurt
beurt = 0

# dobbelworp
worp = 0

#bord afbeelding
bord = pygame.image.load('F1bord.png')
#coordinaat waarbij je 3 stappen vooruit 
drie_stappen_vooruit_coords = [[936, 501]]

#coordinaat waarbij je 4 stappen vooruit 
vier_stappen_vooruit_coords = [[597, 324]]

#coordinaat waarbij je 5 stappen vooruit 
vijf_stappen_vooruit_coords = [[388, 340]]

# Coördinaten waarbij je wint
winnende_coords = [[204, 359]]


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
      if beurt < 4:
          beurt +=1 
      if beurt == 4:
          beurt = beurt - 4
      elif event.key == pygame.K_BACKSPACE:
        print("Knop: Backspace")
        posities = [0,0,0,0]


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
  speler2_x = vakjes[posities[2]][0]-10; #x-cordinaat spler op 2
  speler2_y = vakjes[posities[2]][1]+5; #y-cordinaat speler op 2
  kleur2 = (255,0,0) #rood
  pygame.draw.circle(screen, kleur2, (speler2_x, speler2_y),10) #teken cirkel  als pion 1 is
  speler3_x = vakjes[posities[3]][0]-5; #x-cordinaat spler op 3
  speler3_y = vakjes[posities[3]][1]+10; #y-cordinaat speler op 3  
  kleur3 = (93.7,20.7,66.6) #paars
  pygame.draw.circle(screen, kleur3, (speler3_x, speler3_y),10) #teken cirkel  als pion 1 is
 
  # Controleren of een speler op een coördinaat staat waarop 3 stappen vooruit moet worden gegaan
  for coord in vijf_stappen_vooruit_coords:
      if posities[beurt] == vakjes.index(coord):
          posities[beurt] += 3
          print("Je hebt DRS dus je gaat 3 stappen vooruit. ")

  # Controleren of een speler op een coördinaat staat waarop 4 stappen vooruit moet worden gegaan
  for coord in vijf_stappen_vooruit_coords:
   if posities[beurt] == vakjes.index(coord):
       posities[beurt] += 4
       print("FIA heeft niet door dat je track limits hebt dus je gaat 4 stappen vooruit")
              
# Controleren of een speler op een coördinaat staat waarop 5 stappen vooruit moet worden gegaan
   for coord in vijf_stappen_vooruit_coords:
      if posities[beurt] == vakjes.index(coord):
           posities[beurt] += 5
           print("Je snijdt de baan af dus je gaat 5 stappen vooruit. ")
        
  #controleren of speler op vakje staat waarop je hebt gewonnen
  for coord in winnende_coords:
    if posities[beurt] == vakjes.index(coord):
        print("Je hebt gewonnen!")
        done = True
      
  #update beeldscherm
  pygame.display.flip() #ververst scherm
  clock.tick(60) #limit beeldscherm

#--------afsluiting------------------
pygame.quit()
#eind 

