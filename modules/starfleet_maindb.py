
# --- Spaceships ---
spaceship_enterprise = [
    'USS Enterprise (NX-01)      NX class            Captain Jonathan Archer,    2151 - 2161\n',
    'USS Enterprise (NCC-1701)   Constitution class, Captain James Tiberus Kirk, 2245 - 2285\n',
    'USS Enterprise (NCC-1701-A) Constitution class, Captain James Tiberus Kirk, 2286 - 2293\n',
    'USS Enterprise (NCC-1701-B) Excelsior class,    Captain John Harriman,      2293 - unknown\n',
    'USS Enterprise (NCC-1701-C) Ambassador class,   Captain Rachel Garrett,     unknown - 2344\n',
    'USS Enterprise (NCC-1701-D) Galaxy class,       Captain Jean-Luc Picard,    2363 - 2371\n',
    'USS Enterprise (NCC-1701-E) Sovereign class,    Captain Jean-Luc Picard,    2372 - unknown\n',
    'USS Enterprise (NCC-1701-J) Universe class,     Ubekannter Captain,         unknown\n'];

spaceship_prometheus = [
    'USS Prometheus (NX-59650/NX-74913) Prometheus class, unknowner Captain,            2373 - 2385\n',
    'USS Prometheus (NCC-71201),        Nebula class,     Lieutenant Commander Piersall, unknown\n'  ];

spaceship_voyager = [
    'USS Voyager (NCC-74656) Intrepid class, Captain Kathryn Janeway, 2373 - 2385\n'];

# --- Individual Starships ---

spaceship_enterprise_1701 = [
    'USS Enterprise',
    'Constitution class',
    'NCC-1701',
    'Captain James Tiberus Kirk',
    '2151 - 2161',
    'Zerstört (Selbstzerstörung)'];

spaceship_enterprise_1701a = [
    'USS Enterprise',
    'Constitution class',
    'NCC-1701-A',
    'Captain James Tiberus Kirk',
    '2245 - 2285',
    'Außer Dienst gestellt.'];

spaceship_enterprise_1701b = [
    'USS Enterprise',
    'Excelsior class',
    'NCC-1701-B',
    'Captain John Harriman',
    '2293 - unknown',
    'unknown'];

spaceship_enterprise_1701c = [
    'USS Enterprise',
    'Ambassador class',
    'NCC-1701-C',
    'Captain Rachel Garrett',
    'unknown - 2344',
    'Zerstört'];

spaceship_enterprise_1701d = [
    'USS Enterprise',
    'Galaxy class',
    'NCC-1701-D',
    'Captain Jean-Luc Picard',
    '2363 - 2371',
    'Zerstört'];

spaceship_enterprise_1701e = [
    'USS Enterprise',
    'Sovereign class',
    'NCC-1701-E',
    'Captain Jean-Luc Picard',
    '2372 - unknown',
    'unknown'];

spaceship_enterprise_1701j = [
    'USS Enterprise',
    'Universe class',
    'NCC-1701-J',
    'unknown',
    '26. century',
    'unknown'];

spaceship_prometheus_59650 = [
    'USS Prometheus',
    'Prometheus class',
    'NX-59650 und NX-74913',
    'unknown',
    '2373 - 2385']

spaceship_voyager_74656 = [
    'USS Voyager',
    'Interpid class',
    'NCC-74656',
    'Captain Kathryn Janeway',
    '2373 - 2385']

starships = [
    spaceship_enterprise,
    spaceship_prometheus,
    spaceship_voyager,
    spaceship_prometheus_59650,
    spaceship_enterprise_1701,
    spaceship_enterprise_1701a,
    spaceship_enterprise_1701b,
    spaceship_enterprise_1701c,
    spaceship_enterprise_1701d,
    spaceship_enterprise_1701e,
    spaceship_enterprise_1701j,
    spaceship_voyager_74656];


# --- Starship Classes ---

starshipclass_ufp_galaxy = [
    'Förschungsschiff', # Typ
    640, # Länge
    460, # Breite
    140, # Höhe
    42, # Decks
    1000, # Besatzung, Zivilisten miteinbezogen
    9.2, # Sichere höchstgeschwindigkeit
    9.8, # Höchstgeschwindigkeit
    10, # Phaserbänke
    2, # Torpedorampen (Photon)
    250, # Torpetod (Phtoton)
];


starshipclasses_ufp = [starshipclass_ufp_galaxy];
starshipclasses     = [starshipclasses_ufp];

# --- Database Merging ---

maindb = [
    starships,
    starshipclasses
    ];