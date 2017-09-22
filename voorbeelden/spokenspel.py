
from random import randint
# Hiermee importeren we de functie 'randint', waarmee we
# willekeurige getallen kunnen laten kiezen door de computer


print('Spokenspel') # De titel verschijnt
print('----------')

# --- VARIABELEN ---
ik_ben_dapper = True # Hiermee houden we bij of we nog verder durven gaan score = 0 # Onze beginscore.

while ik_ben_dapper:
    # De regeltjes hieronder worden uitgevoerd zolang ik dapper ben
    spokendeur = randint(1,3) # De computer kiest een deur
    print('Er zijn drie deuren.')
    print('Er zit een spook achter een van de deuren.')
    print('Welke deur wil je openen?')
    gekozendeur = input('Deur 1, 2 of 3? ') # We vragen een keuze
    deurnummer = int(gekozendeur)           # Wat ingetypt is wordt omgezet
                                            # naar een getal

    if deurnummer == spokendeur:
        print('SPOOK!!!')
        ik_ben_dapper = False
    # Als er een spook is, stopt het spel
    else:
        print('Geen spook!')
        print('Je mag door naar de volgende kamer.')
        print('\n') # Een lege regel
        score = score + 1

# Onderstaande regels worden pas uitgevoerd als het spel voorbij is
print('Loop weg!!!!')
print('Spel voorbij! Je score is:', score)
