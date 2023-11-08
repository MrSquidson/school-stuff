import pickle
from colorama import Fore
filename = 'betalinger.pk'

# Directory til betalinger.pk filen...
fodboldtur ={}

# Farven til numrene i menuerne
numbercolor = Fore.LIGHTCYAN_EX

# Lukker og gemmer programmet
def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

# Print liste over ALLE DELTAGERE! og deres indbetalings status
def printliste():
    try:
        for k,v in fodboldtur.items():
            if v < 4500:
                # Hvis de har indbetalt mindre end 4500
                paymentRemaining = 4500 - v
                print(f'{k} har betalt {v} og ', Fore.RED + f'mangler at betale {paymentRemaining}', Fore.BLACK + ' ')
            else:
                if v > 4500:
                    # Hvis du har betalt 4500 får de denne besked...
                    print(f'{k} har betalt {v} totalt og er derfor', Fore.GREEN +'færdig med at indbetale penge', Fore.BLACK + f'{k} kan derfor modtage {(v - 4500)} tilbage fra deres konto status!')

                else: 
                    print(f'{k} har betalt {v} totalt og er derfor', Fore.GREEN +'færdig med at indbetale penge.', Fore.BLACK +' ')
        menu()
    except:
        print('Det virkede ikke')
        menu()

# For at få individuel status på enklete medlemmer
def medlemInfo():
    # Printer en liste med alle medlemsnavnene 
    print('\nMedlems navne:')
    for items in fodboldtur.keys():
        print(items)

# Tjekker om personen er medlem imod keys'ne i dictionary'et
    x = input('Medlems Navn: ')
    if x.upper() in fodboldtur.keys.upper():
        # Hvis personen er medlem printes der en besked der informere brugeren + Personens status
        print('Personen er medlem!')
        print(f'{x} har indbetalt {fodboldtur[x]}')

        betalinger()

    else:
        # Hvis de ikke er medlem modtager brugeren en besked om dette og bliver sendt tilbage til betalings menuen
        print(Fore.RED + 'Personen er ikke medlem!', Fore.BLACK + 'Tjek evt. for Stavefejl og prøv igen!')
        betalinger()

# Ny indbetaling i systemet
def nyBetaling():
    # Print medlemsliste / Keys
    print('\nMedlems navne:')
    try:
        for items in fodboldtur.keys():
            print(items)

    except:
        print('Medlemsliste printede ikke')
        betalinger()

# Validere at person's navn er i listen af keys
    navn = input('Deltagerens navn: ')
    if navn in fodboldtur.keys():
        print('Personen er medlem! \n')
        
        # Prøver at modtage et int input for mængden af penge i.e. hvor mange kroner der er indbetalt til turen 
        try:
            kronerIndbetalt = int(input('Værdi indbetalt i kroner; '))
        except:
            # Hvis f.eks. bogstaver bliver indtastet
            print('Ikke en valid mængde penge')
            print('Returnere til Betalings MENU')
            nyBetaling()
    
    # Printer information om personens status samt hvor meget du ændre deres status med
        print(f'Personen har indbetalt: {fodboldtur[navn]}kr.- til dato \n')
        print(f'Vil du ændre {navn}\'s indbetalings status med {kronerIndbetalt}?')
        print(f'Deres nye konto status vil være {(fodboldtur[navn] + kronerIndbetalt)}kr.- \n')
        if ((fodboldtur[navn]+kronerIndbetalt) > 4500):
            print(Fore.RED + f'{navn} vil være gyldig til at modtage {(fodboldtur[navn] + kronerIndbetalt) - 4500} tilbage', Fore.BLACK + ' \n\n')
        else:
            pass

    # Validering af indtastningen (Tænk nu hvis man tastede forkert!...)
        print('Vil du gemme personens opdateret data Y/N?')
        validering = input('Y/N: ')
        match validering.upper():
            # Yes case - Deres ændringer bliver updateret i dokumentet
            case 'Y':
                    fodboldtur.update({navn: (fodboldtur[navn] + kronerIndbetalt)})
                    print('Personens Konto er opdateret!')
                    print('Returner til betalings menu \n')
                    # SAVES
                    outfile = open(filename, 'wb')
                    pickle.dump(fodboldtur, outfile)
                    outfile.close()
                    betalinger()
            # No case - Bliver sendt tilbage til Betalings menuen... 
            # Dette er muligt fordi vi faktisk aldrig har manipuleret data indtil nu kun observeret den
            case 'N':
                print('Indbetaling annulleret')
                print('Returnere til Betalings menu \n')
                betalinger()
            
            # Non Y/N case - Til alt andet en Y/N bliver personen bare sent tilbage til starten af dette script
            # Bagtanke; Dette kunne have været et modul/Funktion for sig selv hvor den kunne call sig selv ved en other case....
            case _:
                print('Du skal validere om dataen du har indtastet er korrekt!')
                print('Start forfra; \n')
                nyBetaling()
                
    else:
        # Hvis personen navn ikke kan findes i key listen
        print('Navnet er skrevet forkert eller de er ikke medlem')
        print('Returnere til Betalings MENU')
        betalinger()
    

# Liste over alle DER MANGLER AT INDBETALE!
def missingPaymentsFull():
    try:
        for k,v in fodboldtur.items():
            if v < 4500:
                paymentRemaining = 4500 - v
                print(f'{k} har betalt {v} og mangler at betale {paymentRemaining}')


        betalinger()

    except:
        print('Det virkede ikke')
        betalinger()


# Liste med top 3 / Bund 3????
def top3MissingPayment():    
    top = sorted(fodboldtur.items(), key=lambda item: item[1])
    for pair in top[:3]:
        print(f"{pair[0]} har betalt {pair[1]}")
   
    # Ved ærligt talt ikke hvor jeg skal starte...
    # Mine søge termer i google har været "Sorting dictionary python"
    # Det jeg har fundet på stack overflow var ikke behjælpsomt (sortere som regel kun 1 svar ud)
    # Har ikke spurgt ChatGPT. 

    betalinger()
    #TODO: Make top 3 missing payments print...
    #TODO: Make algorithm that can sort the entire list

# Main menu - Det eneste der stadig er semi originalt i dette script...
def menu():
    
    # Menu tekst - Oneliner fordi at det er match casen der er relevant :p
    # Passer ikke helt men jeg huskede man kunne gøre det og så i et kaffein mareridt gjorde jeg det
    # Antal folk der ikke kan læse hvad der står; 3

    print(Fore.GREEN + "\nMENU", Fore.LIGHTCYAN_EX + "\n1:", Fore.BLUE + "Print liste", Fore.LIGHTCYAN_EX + "\n2:", Fore.BLUE + "Betalinger", Fore.LIGHTCYAN_EX + "\n3:", Fore.RED + "Afslut program\n", Fore.BLACK + " ")

# Ændret fra 'if' statements til match case
    valg = input("Indtast dit valg: ")
    match valg:
        case '1':
            # Liste med alle
            # Dette valg er fremhævet fordi det giver et hurtigt overblik i stedet for hvad vi ser i de andre valg
            # Disse er flyttet til betalings menuen...
            print('\n')
            printliste()    
        case '2':
            # Betalings menu
            print('\n')
            betalinger()            
        case '3':
            # Luk + Gem program
            print('\n')
            afslut()
        case _:
            # Alt andet
            print('\n')
            print('Ikke en mulighed')
            menu()

# Betalings Menuen
def betalinger():

    # Se Main Menu Kommentar;
        # Menu tekst - Oneliner fordi at det er match casen der er relevant :p
        # Passer ikke helt men jeg huskede man kunne gøre det og så i et kaffein mareridt gjorde jeg det
        # Antal folk der ikke kan læse hvad der står; 3

    print(Fore.GREEN + '\nBETALINGER', numbercolor + '\n1: ', Fore.LIGHTBLUE_EX + 'Tilføj Betaling', numbercolor +  '\n2: ', Fore.BLUE + 'Print liste med alle der mangler at betale', numbercolor +  '\n3: ', Fore.MAGENTA + 'Print liste med Top 3 manglende', numbercolor + '\n4: ', Fore.BLUE + 'Individuel Medlems status', numbercolor + '\n5: ', Fore.GREEN + 'Tilbage til start menuen' '\n', Fore.BLACK + " ")

    valg = input("Indtast dit valg: ")
    match valg:
        case '1':
            # Ny indbetaling
            print('\n')
            nyBetaling()
        case '2':
            # Liste over alle der mangler at indbetale
            print('\n')
            missingPaymentsFull()
        case '3':
            # Liste over top/bund 3 
            print('\n')
            top3MissingPayment()
        case '4':
            # Individuel medlems status
            print('\n')
            medlemInfo()
        case '5':
            # Tilbage til hovedmenu
            print('\n')
            menu()  
        case _:
            # Ikke et tal/menu valg...
            print('\n')
            print('Vælg en af menuerne')                      
            betalinger()


infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

