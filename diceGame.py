#imports
import random

#ingame stats
playerHealth = 7
monsterHealth = 20 #to be added later

gameComplete = 0 #0 = game incomplete, 1 = game complete
scrollCondition = False #scroll collect conditions

scrollUses = 0
daggerCondition = False #if dagger is collected or not
trapFound = False #if trap is discoverd or not

guess = 3 #for Foshi riddle


#riddle answers
riddleOption = ('tomorrow')


#dice rolling
def rollD10():
    return random.randint(1, 10)

def rollD20():
    return random.randint(1, 20)
    

def battleRollD20():
    roll = random.randint(1, 20)
    if roll == 1:
        return "Critical failure"
    elif roll == 20:
        return "Critical hit"
    else:
        return "success" if roll >= 10 else "failure"

    


#text dialogue
def loadText(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")


#riddle failure
if guess == 0:
    print('You failed')
    print('You succumbed to the illusion and blacked out')
    print('GAME OVER')

#library room text
libraryDesc = loadText('library.txt')
libraryOpt = loadText('libraryOpt.txt')
libraryScroll = loadText('libraryScroll.txt')
libraryOptCellar = loadText('libraryCellarWin')

#trapdoor
monster = loadText('monsterDialogue.txt')
cellarOpt = loadText('cellarOpt.txt')
monsterDefeat = loadText('monsterDefeat.txt') #reminder to fix the text file after the item is developed

#workshop room text
workshopDesc = loadText('workshop.txt')
workshopOpt = loadText('workshopOpt.txt')

#empty room text
emptyDesc = loadText('empty.txt')
emptyOpt = loadText('emptyOpt.txt')


#well room text
wellDesc = loadText('well.txt')
wellOpt = loadText('wellOpt.txt')
foshiText = loadText('foshiText.txt')
foshiExamine = loadText('foshiEx.txt')
illusionBreak = loadText('illusion.txt')
illusionFailure = loadText('illusionFail.txt')
riddle = loadText('riddle.txt')
riddleSolved = loadText('riddleSolve.txt')

#other text
gameOverOpt = loadText('gameOverOpt.txt')



#loops

#library loop when scroll is obtained
def libraryRoomScroll():
    print(libraryDesc)
    print(libraryScroll)
    option = int(input('Choose your option: '))
    
    if option == 2:
        emptyRoomTrapped()
        
    if option == 3:
        workshopRoom()
    
          
    
#library loop when scroll is missing
def libraryRoomNoScroll():
    print(libraryDesc)
    print(libraryOpt)
    option = int(input('Choose your option: '))

    if option == 1:
        perceptionCheck = rollD20()
        if perceptionCheck >= 12:
            print("You rolled a", perceptionCheck, "You found a scroll!")
            libraryRoomScroll()
    else:
        print('You rolled a', perceptionCheck, 'you find nothing of interest.')
        libraryRoomNoScroll()

    if option == 2:
        emptyRoomTrapped()
        
    if option == 3:
        workshopRoom()
        
        
        
#library post-cellar fight
def libraryCellarWin():
    print(libraryDesc)
    print(libraryOptCellar)
    option = int(input('Choose your option: '))

    if option == 1:
        perceptionCheck = rollD20()
        if perceptionCheck >= 12:
            print("You rolled a", perceptionCheck, "You found a scroll!")
            libraryRoomScroll()
    else:
        print('You rolled a', perceptionCheck, 'you find nothing of interest.')
        libraryRoomNoScroll()

    if option == 2:
        emptyRoomTrapped()
        
    if option == 3:
        workshopRoom()
    
    
#________________________________________________________________________________

#cellar fight if fight continues
def cellarFight():

    cellOption = int(input('Choose your option: '))
    
    if cellOption == 1:
        roll = random.randint(1, 20)
        monsterHealth - roll
        if roll == 1:
            print('Critical failure.')
        
        if roll == 20:
            print('Critical hit!')
            
        else:
            print('You dealt', roll, 'damage.')           
            
            if monsterHealth <= 0:
                print(monsterDefeat)
                print('You return to the library')
                libraryCellarWin()
                
            else:
                cellarFight()
                
#cellar fight. Monster attack loop
def monsterAttack():
    print('The monster attacks!')
    roll = random.randint(1, 20)
    if roll == 1:
        print('Critical failure.')
    elif roll == 20:
        print('Critical hit!')
    else:
        print('The monster dealt', roll, 'damage.')
        playerHealth - roll
        cellarFight()



#________________________________________________________________________________

#empty room if trap isn't avoided
def emptyRoomTrapped():
    print('You enter the North Door')
    print(emptyDesc)
    print(emptyOpt)
    
    emptyOption = int(input('Choose your option: '))
    
    if emptyOption == 1:
        print('You stepped on a trap!')
        trapDamage = rollD10()
        dexterityCheck = rollD20()
        if dexterityCheck >=12:
            print('You rolled a', dexterityCheck, 'you successfully avoided the trap!')
            emptyRoomClear()
        else:
            print('You rolled a', dexterityCheck, 'You were hit!')
            playerHealth - trapDamage
            emptyRoomTrapped()
            
    if emptyOption == 2:
        libraryRoomNoScroll()
    
    
  
#________________________________________________________________________________
  
#empty room loop if trap is avoided
def emptyRoomClear():
    print('Options: ')
    print('2. Enter West Door')
    print('3. leave the room')
    emptyOption = int(input('Choose your option: '))
                    
#well room via empty room
    if emptyOption == 2:
        print('You enter the North Door')
            
        print(wellDesc)
        print(wellOpt)
                
        
            
  
    
            
    if emptyOption == 3:
        print('You return to the library')
        libraryRoomNoScroll()

##________________________________________________________________________________
    
#workshop loop after dagger is found
def workshopRoom():
    print('Options: ')
    print('2. Enter North Door')
    print('3. leave the room')
    workshopOption = int(input('Choose your option: '))
    
    if workshopOption == 2:
        print('You enter the North Door')
        
       
    
    #workshop option number 3
    if workshopOption == 3:
        print('You return to the library')
        libraryRoomNoScroll()


#________________________________________________________________________________

    
    

        



#library GAME START
while playerHealth > 0:
    print(libraryDesc)
    print(libraryOpt)

    option = int(input('Choose your option: '))

    if option == 1:
        perceptionCheck = rollD20()
        if perceptionCheck >= 12:
            print("You rolled a", perceptionCheck, "You found a scroll!")
            libraryRoomScroll()
        else:
            print('You rolled a', perceptionCheck, 'you find nothing of interest.')
            libraryRoomNoScroll()

#empty room        
    if option == 2:
        print('You enter the North Door')
        print(emptyDesc)
        print(emptyOpt)
    
        emptyOption = int(input('Choose your option: '))
    
        if emptyOption == 1:
            print('You stepped on a trap!')
            trapDamage = rollD10()
            dexterityCheck = rollD20()
            if dexterityCheck >=12:
                print('You rolled a', dexterityCheck, 'you successfully avoided the trap!')       
            
            #well room via empty room
                print('You enter the North Door')
            
                print(wellDesc)
                print(wellOpt)
                
                wellOption = int(input('Choose you option: '))
            
                if wellOption == 1:
                    print(foshiExamine)
                    perceptionCheck = rollD20()
                    if perceptionCheck >= 18:
                        print('You rolled a', perceptionCheck,'!')
                        print(illusionBreak)
                        print(foshiText)
                        print(riddle)
                        
                        while guess > 0:
                            print(foshiText)
                            print(riddle)
                            riddleAnswer = input('What am I? ')
                        if riddleAnswer.lower() == 'tomorrow':
                            print(riddleSolved)
                            print('VICTORY!')
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
                        
                        else:
                            guess -= 1
                            if guess > 0:
                                print('Incorrect, try again')
                                print('You have', guess, 'guesses left.')
                            
                            else:
                                print('You have failed to solve my riddle...')
                                print('You succummed to the illusion')
                                playerHealth -= 7
                                gameRestart = input('Do you wish to play again?')
                                print('yes/no')
                                if gameRestart.lower() == 'yes':
                                    libraryRoomNoScroll()
                    
                    else:
                        print('You rolled a', perceptionCheck)
                        print('The image leaves you in a trance')
                        print(foshiText)
                        print(riddle)
                        
                        while guess > 0:
                            print(foshiText)
                            print(riddle)
                            riddleAnswer = input('What am I? ')
                            if riddleAnswer.lower() == 'tomorrow':
                                print(riddleSolved)
                                print('VICTORY!')
                                gameRestart = input('Do you wish to play again?')
                                print('yes/no')
                                if gameRestart.lower() == 'yes':
                                    libraryRoomNoScroll()
                        
                        else:
                            guess -= 1
                            if guess > 0:
                                print('Incorrect, try again')
                                print('You have', guess, 'guesses left.')
                            
                            else:
                                print('You have failed to solve my riddle...')
                                print('You succummed to the illusion')
                                playerHealth -= 7
                                gameRestart = input('Do you wish to play again?')
                                print('yes/no')
                                if gameRestart.lower() == 'yes':
                                    libraryRoomNoScroll()
                    
            
            if wellOption == 2:
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!')
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
                    
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                        
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
                    
            if wellOption == 3:
                print('As you turn around, you notice that the door you entered from magically disappeared')
                print(foshiText)
                print(riddle)
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!')
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
                    
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                        
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
            
            
            else:
                print('You rolled a', dexterityCheck, 'you fell into the trap')
                print('You lost', trapDamage, 'HP')
                playerHealth - trapDamage
                emptyRoomClear()
            
            if emptyOption == 2:
                print('You return to the library')
                libraryRoomNoScroll()
        
    if option == 3:
        print('You enter the West Door')
        print(workshopDesc)
        print(workshopOpt)
    
        workshopOption = int(input('Choose your option: '))
    
        if workshopOption == 1:
            print('You found a Dagger and some gold!')
            daggerCondition == True
            workshopRoom()
            

        
        if workshopOption == 2:
            print('You enter the North Door')
        
            print(wellDesc)
            print(wellOpt)
  
#well room via workshop        
            wellOption = int(input('Choose you option: '))
        
            if wellOption == 1:
                print(foshiExamine)
                perceptionCheck = rollD20()
                if perceptionCheck >= 18:
                    print('You rolled a', perceptionCheck,'!')
                    print(illusionBreak)
                    
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!') 
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
                    
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                        
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
                
                else:
                    print('You rolled a', perceptionCheck)
                    print('The image leaves you in a trance')
                    while guess > 0:
                        print(foshiText)
                        print(riddle)
                        riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!') 
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
                    
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                        
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
                    
            if wellOption == 2:
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!') 
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
            
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
                    
                
            if wellOption == 3:
                combatCheck = rollD20()
                print('You rolled a', combatCheck, 'You miss!')
                print(foshiText)
                print(riddle)
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!')
                        gameRestart = input('Do you wish to play again?')
                        print('yes/no')
                        if gameRestart.lower() == 'yes':
                            libraryRoomNoScroll()
                        
                
                    else:
                        guess -= 1
                        if guess > 0:
                                print('Incorrect, try again')
                                print('You have', guess, 'guesses left.')
                    
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
                            gameRestart = input('Do you wish to play again?')
                            print('yes/no')
                            if gameRestart.lower() == 'yes':
                                libraryRoomNoScroll()
            
            
            if wellOption == 4:
                print('As you turn around, you notice that the door you entered from magically disappeared')
                print(foshiText)
                print(riddle)
                while guess > 0:
                    print(foshiText)
                    print(riddle)
                    riddleAnswer = input('What am I? ')
                    if riddleAnswer.lower() == 'tomorrow':
                        print(riddleSolved)
                        print('VICTORY!')
                        break
                
                    else:
                        guess -= 1
                        if guess > 0:
                            print('Incorrect, try again')
                            print('You have', guess, 'guesses left.')
                    
                        else:
                            print('You have failed to solve my riddle...')
                            print('You succummed to the illusion')
                            playerHealth -= 7
    
    #workshop option number 3
        if workshopOption == 3:
            print('You return to the library')
            libraryRoomNoScroll()




#trapdoor cellar

    if option == 4:
        print('You enter the trapdoor...')
        print(monster)
        print(cellarOpt)
    
        cellOption = int(input('Choose your option: '))
    
        if cellOption == 1:
            roll = random.randint(1, 20)
            if roll == 1:
                print('Critical failure.')
            elif roll == 20:
                    print('Critical hit!')
            else:
                print('You dealt', roll, 'damage.')
            
            monsterHealth -= roll
            
            if monsterHealth < 1:
                print(monsterDefeat)
                print('You return to the library')
                libraryCellarWin()
                
            else:
                print('The monster attacks!')
                roll = random.randint(1, 20)
                print('The monster dealt', roll, 'damage.')
                playerHealth -= roll
                cellarFight()
    
            if cellOption == 2:
                print('The monster attacks!')
                roll = random.randint(1, 20)
                blockDamage = roll * .05
                if roll == 1:
                    print('You rolled a', roll ,'Critical failure.')
                    monsterAttack()
                elif roll == 20:
                    print('You rolled a', roll ,'Critical Success! You blocked all oncoming damage!')
                    cellarFight()
                else:
                    print('You blocked', roll, 'damage.')
                    playerHealth -= blockDamage
                    cellarFight()
            
            if cellOption == 3:
                print('The monster ignores you and attacks')
                roll = random.randint(1, 20)
                if roll == 1:
                    print('Critical failure.')
                    cellarFight()
                elif roll == 20:
                    print('Critical hit!')
                    cellarFight()
            else:
                print('The monster dealt', roll, 'damage.')
                playerHealth -= roll
                cellarFight()
            
            if cellOption == 4:
                print('You retreated to the library.')
                print('You hear the trapdock lock itself...')
                libraryCellarWin()
        
    
            

#gameover sequence
    if playerHealth < 1:
        print('GAME OVER')
        gameOverOpt = str(input('Try Again? '))
        print(gameOverOpt)
        if gameOverOpt == str('yes'):
            libraryRoomNoScroll()

    
    
    
        