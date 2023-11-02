import pickle
from colorama import Fore
filename = 'betalinger.pk'

fodboldtur ={}

numbercolor = Fore.LIGHTCYAN_EX

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    try:
        for k,v in fodboldtur.items():
            if v < 4500:
                paymentRemaining = 4500 - v
                print(f'{k} har betalt {v} og ', Fore.RED + f'mangler at betale {paymentRemaining}', Fore.BLACK + ' ')
            else:
                    print(f'{k} har betalt {v} totalt og er derfor ', Fore.GREEN + 'færdig med at indbetale penge', Fore.BLACK + ' ')        
        menu()
    except:
        print('Det virkede ikke')
        menu()


def medlemInfo():
    print('\nMedlems navne:')
    for items in fodboldtur.keys():
        print(items)

    x = input('Medlems Navn: ')
    if x.upper() in fodboldtur.keys.upper():
        print('Personen er medlem!')
        print(f'{x} har indbetalt {fodboldtur[x]}')

        betalinger()


def nyBetaling():
    print('\nMedlems navne:')
    try:
        for items in fodboldtur.keys():
            print(items)

    except:
        print('Medlemsliste printede ikke')
        betalinger()

    navn = input('Deltagerens navn: ')
    if navn in fodboldtur.keys():
        print('Personen er medlem! \n')
        try:
            kronerIndbetalt = int(input('Værdi indbetalt i kroner; '))
        except:
            print('Ikke en valid mængde penge')
            nyBetaling()
    
        print(f'Personen har indbetalt: {fodboldtur[navn]}kr.- til dato \n')
        print(f'Vil du ændre {navn}\'s indbetalings status med {kronerIndbetalt}?')
        print(f'Deres nye konto status vil være {(fodboldtur[navn] + kronerIndbetalt)}kr.- \n')

        print('Vil du gemme personens opdateret data Y/N?')
        validering = input('Y/N: ')
        match validering.upper():
            case 'Y':
                    fodboldtur.update({navn: (fodboldtur[navn] + kronerIndbetalt)})
                    print('Personens Konto er opdateret!')
                    print('Returner til betalings menu \n')
                    betalinger()

            case 'N':
                print('Indbetaling annulleret')
                print('Returnere til Betalings menu \n')
                betalinger()
                
            case _:
                print('Du skal validere om dataen du har indtastet er korrekt!')
                print('Start forfra; \n')
                nyBetaling()
                
    else:
        print('Navnet er skrvet forkert eller de er ikke medlem')
        nyBetaling()
    


def missingPaymentsFull():
    try:
        for k,v in fodboldtur.items():
            if v < 4500:
                paymentRemaining = 4500 - v
                try:
                    print(f'{k} har betalt {v} og mangler at betale {paymentRemaining}')
                except:
                    print('string fucked up')

        betalinger()

    except:
        print('Det virkede ikke')
        betalinger()

def top3MissingPayment():    
    print('Not done yet... sorry :(')


    betalinger()
    #TODO: Make top 3 missing payments print...
    #TODO: Make algorithm that can sort the entire list

def menu():
    print(Fore.GREEN + "\nMENU", Fore.LIGHTCYAN_EX + "\n1:", Fore.BLUE + "Print liste", Fore.LIGHTCYAN_EX + "\n2:", Fore.BLUE + "Betalinger", Fore.LIGHTCYAN_EX + "\n3:", Fore.RED + "Afslut program\n", Fore.BLACK + " ")

    valg = input("Indtast dit valg: ")
    match valg:
        case '1':
            print('\n')
            printliste()    
        case '2':
            print('\n')
            betalinger()            
        case '3':
            print('\n')
            afslut()
        case _:
            print('\n')
            print('Ikke en mulighed')
            menu()

def betalinger():
    print(Fore.GREEN + '\nBETALINGER', numbercolor + '\n1: ', Fore.LIGHTBLUE_EX + 'Tilføj Betaling', numbercolor +  '\n2: ', Fore.BLUE + 'Print liste med alle der mangler at betale', numbercolor +  '\n3: ', Fore.MAGENTA + 'Print liste med Top 3 manglende (Not done)', numbercolor + '\n4: ', Fore.BLUE + 'Individuel Medlems status', numbercolor + '\n5: ', Fore.GREEN + 'Tilbage til start menuen' '\n', Fore.BLACK + " ")

    valg = input("Indtast dit valg: ")
    match valg:
        case '1':
            print('\n')
            nyBetaling()
        case '2':
            print('\n')
            missingPaymentsFull()
        case '3':
            print('\n')
            top3MissingPayment()
        case '4':
            print('\n')
            medlemInfo()
        case '5':
            print('\n')
            menu()  
        case _:
            print('\n')
            print('Vælg en af menuerne')                      
            betalinger()


infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

