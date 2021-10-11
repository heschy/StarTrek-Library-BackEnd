import mhn;
from starfleet_functions import *;

def library(name):
    output='\n';

    # --- Library Building ---

    # ------Library Building: Spaceships ------
    spaceship_enterprise = [
        'USS Enterprise (NX-01)      NX Klasse            Captain Jonathan Archer,    2151 - 2161\n',
        'USS Enterprise (NCC-1701)   Constitution Klasse, Captain James Tiberus Kirk, 2245 - 2285\n',
        'USS Enterprise (NCC-1701-A) Constitution Klasse, Captain James Tiberus Kirk, 2286 - 2293\n',
        'USS Enterprise (NCC-1701-B) Excelsior Klasse,    Captain John Harriman,      2293 - Unbekannt\n',
        'USS Enterprise (NCC-1701-C) Ambassador Klasse,   Captain Rachel Garrett,     Unbekannt - 2344\n',
        'USS Enterprise (NCC-1701-D) Galaxy Klasse,       Captain Jean-Luc Picard,    2363 - 2371\n',
        'USS Enterprise (NCC-1701-E) Sovereign Klasse,    Captain Jean-Luc Picard,    2372 - Unbekannt\n',
        'USS Enterprise (NCC-1701-J) Universe Klasse,     Ubekannter Captain,         Unbekannt\n'];
    
    spaceship_prometheus = [
        'USS Prometheus (NX-59650/NX-74913) Prometheus Klasse, Unbekannter Captain,            2373 - 2385\n',
        'USS Prometheus (NCC-71201),        Nebula Klasse,     Lieutenant Commander Piersall, Unbekannt\n'  ];

    spaceship_voyager = [
        'USS Voyager (NCC-74656) Intrepid Klasse, Captain Kathryn Janeway, 2373 - 2385\n'];
    
    spaceship_prometheus_59650 = [
        'USS Prometheus',
        'Prometheus Klasse',
        'NX-59650 und NX-74913',
        'Unbekannt',
        '2373 - 2385',
        'Version 2']

    starships = [
        spaceship_enterprise,
        spaceship_prometheus,
        spaceship_voyager,
        spaceship_prometheus_59650];


    # ------ Library Builing: Starship Classes ------

    starshipclass_ufp_galaxy = [
        'Library Build uncomplete...'
    ];


    starshipclasses_ufp = [starshipclass_ufp_galaxy];
    starshipclasses     = [starshipclasses_ufp];

    db = [
        starships,
        starshipclasses
        ];
        
    # --- Library Access ---
    
    if name == 'MHN' or name == 'Medizinisches Holografisches Notfallprogramm' or name == 'mhn'or name == 'Medizinisch Holografisches Notfallprogramm':
        output = mhn.v1()+'\n';
        output += mhn.v2();
        
    elif name == 'USS Enterprise':
        for listitem in spaceship_enterprise:
            output += listitem;
            
    elif name == 'USS Prometheus':
        for listitem in spaceship_prometheus:
            output += listitem;
            
    elif name == 'USS Voyager':
        for listitem in spaceship_voyager:
            output += listitem;
    
    elif name == 'NX-59650' or name == 'NX-74913':
        output += db_entry_ship_decode(spaceship_prometheus_59650, mhn.v2());
    
    elif name == 'db_entry:nx59650' or name == 'db_entry:nx74913':
        output += str(spaceship_prometheus_59650);

    elif name == 'exit' or name == 'quit' or name == 'stop':
        return 1;
        
    elif name == 'help' or name == 'info':
        output += 'Um eine Liste der Schiffe zu erhalten, die den selben namen tragen, geben sie bitte den Namen ein.' + '\n';
        output += 'Um alle Informationen über ein bestimmtes Schiff zu erhalten, geben sie bitte die Registriernummer des Schiffes an.' + '\n';
    
    elif name == 'db' or name == 'print_db' or name == 'print db' or name == 'database' or name == 'print_database' or name == 'print database':
        print('db' + str(db));
        output = 'Output to Large, wrote into Console';
    else:
        output += 'Zugriff nicht möglich!'+'\n';
        
    return output;

