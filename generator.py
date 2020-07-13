from random import randint

rude_list = [
    'Pauvre cloche',
    'Cher vieux débris',
    'Misérable loque humaine',
    'Vieux shnoque',
    'Séducteur déplumé',
    'Vieux macaque édenté',
    'Noble Jean-Foutre',
    'Chère vieille crapule',
    'Vieille charogne',
    'Pâle escroc',
    'Bougre de galapiat',
    'Vieux pourri',
    'Méprisable ordure',
    'Sinistre individu',
    'Vieux machin',
    'Vieillard cacochyme',
    'Petit foutriquet',
    'Vieux matou',
    'Gros malpropre',
    'Greluchon famélique',
    'Petit voyou',
    'Gibier de potence'
]

def generate():
    print(rude_list[randint(0,len(rude_list)-1)])

if __name__ == "__main__":
    generate()