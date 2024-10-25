trafikkmeldinger = [
    {'by': 'Oslo', 'alvorlighetsgrad': 'høy', 'beskrivelse': 'Ulykke på E6'},
    {'by': 'Bergen', 'alvorlighetsgrad': 'moderat', 'beskrivelse': 'Veiarbeid på E39'},
    {'by': 'Trondheim', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'Kø på vei 705'},
    {'by': 'Oslo', 'alvorlighetsgrad': 'moderat', 'beskrivelse': 'Kø på Ring 3'},
    {'by': 'Stavanger', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'Veiarbeid på E39'},
    {'by': 'Bergen', 'alvorlighetsgrad': 'høy', 'beskrivelse': 'Stor ulykke ved flyplassen'},
    {'by': 'Trondheim', 'alvorlighetsgrad': 'høy', 'beskrivelse': 'Trafikkulykke på E6'}
]


def hent_meldinger(*args, **kwargs):
    resultater = []
    
    for melding in trafikkmeldinger:
        passer = True
        for ord in args:
            if ord not in melding['beskrivelse']:
                passer = False
                break
        
        for key, value in kwargs.items():
            if melding.get(key) != value:
                passer = False
                break
                
        if passer:
            resultater.append(melding)
    return resultater


def vis_meldinger(meldinger):
    for melding in meldinger:
        print(f"By: {melding['by']}, Alvorlighetsgrad: {melding['alvorlighetsgrad']}")
        print(f"Beskrivelse: {melding['beskrivelse']}\n")


print("Henter meldinger fra Oslo med alvorlighetsgrad 'høy':")
meldinger = hent_meldinger(alvorlighetsgrad='høy', by='Oslo')
vis_meldinger(meldinger)

print("Henter meldinger fra Bergen med alvorlighetsgrad 'høy':")
meldinger = hent_meldinger(by='Bergen', alvorlighetsgrad='høy')
vis_meldinger(meldinger)



print("Henter meldinger som inneholder ordet 'Kø':")
meldinger = hent_meldinger('Kø')
vis_meldinger(meldinger)