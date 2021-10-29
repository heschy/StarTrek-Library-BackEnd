def db_entry_ship_decode(database, emh):
    output = '';
    output += 'Name: '                                                + database[0] + '\n';
    output += 'Klasse: '                                              + database[1] + '\n';
    output += 'Registriernummer(n): '                                 + database[2] + '\n';
    output += 'Captain: '                                             + database[3] + '\n';
    output += 'Zeitraum: '                                            + database[4] + '\n';
    output += 'Emergency Medical Hologramm (EMH): '  + emh + '\n';
    return output;

def db_entry_shipclass_UFP_decode(database):

    # Alle Einträge im Array in Strings konvertieren.

    for i in range(len(database)):
        database[i] = str(database[i]);

    output = '';
    output += 'Galaxy Klasse - Vereinigte Föderation der Planeten\n';
    output += 'Typ: '                                  + database[0] + '\n';
    output += 'Länge in Metern: ca.'                   + database[1] + '\n';
    output += 'Breite in Metern: ca.'                  + database[2] + '\n';
    output += 'Höhe in Metern: '                       + database[3] + '\n';
    output += 'Anzahl der Decks: '                     + database[4] + '\n';
    output += 'Besatzung (Zivilisten miteinbezogen): ' + database[5] + '\n';
    output += 'Sichere Höchstgeschwindigkeit: '        + database[6] + '\n';
    output += 'Höchstgeschwindigkeit: '                + database[7] + '\n';
    output += 'Anzahl der Phaserbänke: '               + database[8] + '\n';
    output += 'Anzahl der Photonentorpedorampen: '     + database[9] + '\n';
    output += 'Anzahl der Photonentorpedos: '          + database[10] + '\n';
    return output;
    
def is_class(class_name ,str):
    if class_name == 'ufp_galaxy':
        if str == 'Galaxy Class' or str == 'galaxy class' or str == 'Galaxy class':
            return True;
        else: return False;
    else: return False;

def is_name(name, str):
    if name == 'uss_enterprise':
        if str == 'USS Enterprise' or str == 'USS enterprise' or str == 'uss enterprise' or str == 'enterprise' or str == 'Enterprise':
            return True;
        else : return False;
    elif name == 'uss_prometheus':
        if str == 'USS Prometheus' or str == 'USS prometheus' or str == 'uss prometheus' or str == 'prometheus' or str == 'Prometheus':
            return True;
        else : return False;
    elif name == 'uss_voyager':
        if str == 'USS Voyager' or str == 'USS voyager' or str == 'uss voyager' or str == 'voyager' or str == 'Voyager':
            return True;
        else : return False;
    else: return False;

def is_cmd(cmd,str):
    if cmd == 'quit':
        if str == 'exit' or str == cmd or str == 'stop': return True;
        else: return False;
    elif cmd == 'help':
        if str == cmd or str == 'info': return True;
        else: return False;
    elif cmd == 'db_print':
        if str == 'db' or str == cmd or str == 'print_db' or str == 'print db' or str == 'database' or str == 'print_database' or str == 'print database': return True;
        else: return False;
