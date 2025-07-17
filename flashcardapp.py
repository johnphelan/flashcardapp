import keyboard
import random
import os

def main():
    
    class DeckManager:

        def __init__(self):
            self.decks = {}  # name → Flashstack object
            
        def add_deck(self, name):
            if name not in self.decks:
                self.decks[name] = Flashstack(name)

        def get_deck(self, name):
            return self.decks.get(name)

        def remove_deck(self, name):
            if name in self.decks:
                del self.decks[name]

    class Flashstack:
        def __init__(self, name):
            self.name = name
            self.stack = []
        
        def add_card(self, question, answer):
            self.stack.append(Flashcard(question, answer))

        def remove_card(self, index):
            del self.stack[index]

        def flash_rewiewoutput(self, option):
            
            stack_dict = {}
            stackquestion_list = []
            for z in self.stack:
                stack_dict[z.question] = z.answer
                stackquestion_list.append(z.question)

            if option == 1:
                return stack_dict
            if option == 2:
                return stackquestion_list
            
    class Flashcard:
        def __init__(self, question, answer):
            self.question = question
            self.answer = answer

    manager = DeckManager()

    manager.add_deck("verbs") # sample decks
    manager.add_deck("seconddeck")
    manager.get_deck("verbs").add_card("走る", "to run")
    manager.get_deck("verbs").add_card("飲む", "to drink")
    manager.get_deck("verbs").add_card("会う", "to meet")
    manager.get_deck("verbs").add_card("手伝う", "to help")

    def mainprompter():

        def safe_int(s):
            try:
                return int(s)
            except ValueError:
                return None

        def mainscreen():   # main screen that gives basic options to view or create decks
            
            print()
            print("\033[92mFLASH CARD APP 1.0.1\033[0m")
            print()
            
            if len(manager.decks) == 0:
                print("NO CURRENT DECKS ")
            
            else:
                print("\033[34mDECKS\033[0m")
                print()
                for i, deck_name in enumerate(manager.decks, start=1):
                    print(f"\033[34m{i}. {deck_name}\033[0m")
                    
            print()
            
            while True:
                print("  ")
                print("\033[34;3mOPTIONS\033[0m")
                print("\033[38;5;54m1. VIEW DECK/EDIT DECK\033[0m")
                print("\033[38;5;54m2. CREATE DECK\033[0m")
                print("\033[38;5;54m3. DELETE DECK\033[0m")
                print("\033[38;5;54m4. REVIEW\033[0m")
                print("\033[38;5;54m5. QUIT PROGRAM\033[0m")
                input1 = input('CHOOSE OPTION:')
                
                if (safe_int(input1) == int(1) or safe_int(input1) == int(3)) and len(manager.decks) == 0: # checks to see if user has no decks and choices to view/delete
                    print()
                    print("[NO DECKS...UNABLE TO SELECT THIS OPTION]")
                    print()

                elif safe_int(input1) == int(1) and len(manager.decks) > 0:  # goes to view/edit
                    alldeckmenu()
                    break
                    
                elif safe_int(input1) == int(2):  # goes to create deck
                    create_deck()
                    break

                elif safe_int(input1) == int(3): # delete deck sequence
                    delete_deck()
                    break

                elif safe_int(input1) == int(4): # goes to review function
                    reviewmenu()
                    break

                elif safe_int(input1) == int(5): # stops program
                    break

                else:   # displays message if input does not match any option
                    print()
                    print("INVALID OPTION PLEASE TRY AGAIN")
                    print()
                    
        def alldeckmenu():
            deckselectionpath(1)  # option for deck selection

        def reviewmenu():
            deckselectionpath(2)  # option for deck review

        def deckselectionpath(option):   # gives a deck selection that goes to multiple options(ex: EDIT SCREEN/ REVIEW SCREEN)
            while True:
                print()
                print()
                if option == 1:
                    print("SELECT DECK:")
                if option == 2:
                    print("\033[92mSELECT DECK FOR REVIEW: \033[0m")
                print("(Type 'x' to go back to main menu)")
                print()
                print("\033[34mCURRENT DECKS\033[0m")
                print()
                for i, deck_name in enumerate(manager.decks, start=1):
                    print(f"\033[34m{i}. {deck_name}\033[0m")
                print()
                input2 = input('CHOOSE OPTION:')

                if safe_int(input2) is not None and safe_int(input2) > 0 and safe_int(input2) <= len(manager.decks): #checks to see if number matches a deck

                    totaldecklist = list(manager.decks)
                    selected_deck = totaldecklist[safe_int(input2)-1]

                    if option == 1:  # option for deck selection
                        deckview(selected_deck)
                        break

                    if option == 2:  # option for deck review
                        
                        if manager.get_deck(selected_deck).stack == []:
                            print("NO CARDS ADDED TO DECK YET.  PLEASE ADD BEFORE REVIEW")
                        else:
                            deck_review(selected_deck)
                            break 
                    
                elif input2 == "x": # goes to main screen
                    mainscreen()
                    break
                else:
                    print()
                    print("NOT A VALID OPTION")

        def reviewinput():
            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "space":     
                        return("SPACE")
                    elif event.name == "enter":
                        return("ENTER")
                    elif event.name == "x":
                        return("x")
                    
        def fliporquit():
            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "f":     
                        return("f")
                        
                    elif event.name == "x":
                        return("x")
        
        def spaceprint(no_spaces):
            for x in range(no_spaces):
                print()

        def deck_review(deck):
            while True:    
                print()  # main text sequence / instructions for review mode
                print()
                print("\033[34;3mREVIEW MODE\033[0m")
                print("INSTRUCTIONS:")
                print("Press 'f' to flip card")
                print("Press 'enter' for a correct answer")
                print("Press 'space' for a wrong answer")
                print("Press 'x' to quit review")
                print()
                print("\033[92mPRESS 'f' to start REVIEW\033[0m")
                
                firstflip = fliporquit()
                if firstflip == 'x':
                    mainscreen()
                    break
                elif firstflip == 'f':
                    pass
                
                deck_dict = manager.get_deck(deck).flash_rewiewoutput(1)  # deck_dict = dictionary to look up answer to each card
                remlist = manager.get_deck(deck).flash_rewiewoutput(2)    # remlist = remaining list of cards to go through
                random.shuffle(remlist)
                
                spaceprint(10)
                index = 0
                while remlist != []:
                    if index > len(remlist)-1: #sets index back to 0 if the index goes out of range
                        index = 0
                    
                    spaceprint(10)
                    print(remlist[index]) # prints question
                    print("\033[34m---------------------------- press f ------------------\033[0m")
                    reviewflip = fliporquit()

                    if reviewflip == 'x': # cancels review to go back to menu
                        mainscreen()
                        break
                    elif reviewflip == 'f':  # checks for flip
                        pass
                    
                    print(deck_dict[remlist[index]])  # prints answer
                    print()
                    print('---------------------------- space/enter --------------')
                    print()
                    reviewcheck = reviewinput()

                    if reviewcheck == 'x': # cancels review to go back to menu
                        break
                    elif reviewcheck == 'ENTER': # correct answer  REMOVES ITEM FROM LIST
                        remlist.pop(index)   
                        pass
                    elif reviewcheck == 'SPACE':  # correct answer SKIPS TO NEXT INDEX
                        index += 1
                        pass

                print("\033[92mREVIEW ENDED\033[0m")
                
                
        def delete_deck(): # deck DELETION screen
            while True:
                print()
                print()
                print("\033[34mDECKS\033[0m")
                for i, deck_name in enumerate(manager.decks, start=1):
                        print(f"\033[34m{i}. {deck_name}\033[0m")
                print()
                print("CHOOSE DECK TO DELETE")
                print("\033[31mWARNING THIS CANNOT BE REVERSED!\033[0m")
                print()
                print("(Type 'x' to cancel)")
                
                deleteinput = input("WRITE DECK NUMBER TO DELETE:")
                if safe_int(deleteinput) is not None and safe_int(deleteinput) > 0 and safe_int(deleteinput) <= len(manager.decks): #checks to see if number matches a deck

                    totaldecklist = list(manager.decks)
                    selected_deck = totaldecklist[safe_int(deleteinput)-1]
            
                    manager.remove_deck(selected_deck)
                    print()
                    print('DELETED [' + selected_deck + '] SUCCESSFULLY')
                    print()

                    mainscreen()
                    break

                elif deleteinput == "x":
                    mainscreen()
                    break
                else:
                    print()
                    print("NOT A VALID OPTION")

        def create_deck():  # deck CREATION screen
            while True:
                print()
                print("\033[34mCREATE DECK\033[0m")
                print("(Type 'x' to go back)")
                print()

                creationanswer = input('WRITE DECK NAME:')
                if creationanswer == "x":
                    mainscreen()
                    break
                manager.add_deck(creationanswer)
                print(creationanswer + ' ADDED')
                print()

        def deckview(deck): # LOOKS AT EACH SPECIFIC DECK TO ADD/EDIT DELETE CARDS
            while True:
                print()
                print('DECKNAME: ' + deck)  # prints deck name 
                
                if manager.get_deck(deck).stack == []:  # checks scenario where there are no cards
                    print("NO CARDS ADDED YET!")
                else:
                    for i, z in enumerate(manager.get_deck(deck).stack):  # prints all cards from selected deck
                        print(f"{i+1}: {z.question} - {z.answer}")
                        
                print()
                print("\033[34;3mDECK OPTIONS\033[0m")    # prints menu options
                print("\033[38;5;54m1. ADD CARD\033[0m")
                print("\033[38;5;54m2. DELETE CARD\033[0m")
                print("\033[38;5;54mx. GO BACK\033[0m")
                print()
                input3 = input('CHOOSE OPTION:')   # takes input
                
                if safe_int(input3) == int(1):    # add card option
                    while True:
                        print()
                        for i, z in enumerate(manager.get_deck(deck).stack):
                            print(f"{i+1}: {z.question} - {z.answer}")
                        print()
                        print("\033[34mADD CARD TO DECK.  (Type 'x' to go back)\033[0m")
                        print()

                        question = input('WRITE FRONT:')
                        if question == "x":
                            break
                        answer = input('WRITE BACK:')
                        if answer == "x":
                            break
                        manager.get_deck(deck).add_card(question, answer)

                    

                elif safe_int(input3) == int(2):      # delete card option
                    while True:
                    
                        print()
                        print("\033[34mDELETE CARD\033[0m")
                        print()
                        for i, z in enumerate(manager.get_deck(deck).stack):
                            print(f"{i+1}: {z.question} - {z.answer}")
                        print()
                        print("(Type 'x' to go back)")
                        card_delete_no = input('CHOOSE CARD TO DELETE:')
                        if safe_int(card_delete_no) is not None and safe_int(card_delete_no)> 0 and safe_int(card_delete_no) <= len(manager.get_deck(deck).stack):
                            
                            manager.get_deck(deck).remove_card(safe_int(card_delete_no)-1)
                        elif card_delete_no == "x":  
                            break
                        else:
                            print()
                            print("NOT A VALID OPTION")


                elif input3 == 'x':     
                    alldeckmenu()
                    break
                else:
                    print()
                    print("INVALID OPTION PLEASE TRY AGAIN")
                    print()

        mainscreen()
        
    mainprompter()

if __name__ == "__main__":
    main()