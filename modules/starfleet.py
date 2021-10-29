import mhn;
from starfleet_functions import *;
import starfleet_maindb as db;

def library(name):
    output='\n';
    
    if name == 'MHN' or name == 'Medizinisches Holografisches Notfallprogramm' or name == 'mhn'or name == 'Medizinisch Holografisches Notfallprogramm':
        output = mhn.v1()+'\n';
        output += mhn.v2();
        
    elif is_name('uss_enterprise', name):
        for listitem in db.spaceship_enterprise:
            output += listitem;
            
    elif is_name('uss_prometheus', name):
        for listitem in db.spaceship_prometheus:
            output += listitem;
            
    elif is_name('uss_voyager', name):
        for listitem in db.spaceship_voyager:
            output += listitem;
    elif is_class('ufp_galaxy', name):
        output += db_entry_shipclass_UFP_decode(db.maindb[1][0][0]);

    elif name == 'NX-59650' or name == 'NX-74913':
        output += db_entry_ship_decode(db.spaceship_prometheus_59650, mhn.v2());

    elif name == 'NCC-1701' or name == 'NCC 1701':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701, 'Nicht Installiert');

    elif name == 'NCC-1701-A' or name == 'NCC 1701 A' or name == 'NCC-1701 A':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701a, 'Nicht Installiert');

    elif name == 'NCC-1701-B' or name == 'NCC 1701 B' or name == 'NCC-1701 B':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701b, 'Nicht Installiert');

    elif name == 'NCC-1701-C' or name == 'NCC 1701 C' or name == 'NCC-1701 C':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701c, 'Nicht Installiert');

    elif name == 'NCC-1701-D' or name == 'NCC 1701 D' or name == 'NCC-1701 D':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701d, 'Nicht Installiert');

    elif name == 'NCC-1701-E' or name == 'NCC 1701 E' or name == 'NCC-1701 E':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701e, mhn.v1());

    elif name == 'NCC-1701-J' or name == 'NCC 1701 J' or name == 'NCC-1701 J':
        output += db_entry_ship_decode(db.spaceship_enterprise_1701j, 'Unbekannt');

    elif name == 'NCC-74656' or name == 'NCC 74656':
        output += db_entry_ship_decode(db.spaceship_voyager_74656, 'Unbekannt');

    elif is_cmd('quit', name):
        return 'cmd(_close_)';
        
    elif is_cmd('help', name):
        output += 'Um eine Liste der Schiffe zu erhalten, die den selben namen tragen, geben sie bitte den Namen ein.' + '\n';
        output += 'Um alle Informationen über ein bestimmtes Schiff zu erhalten, geben sie bitte die Registriernummer des Schiffes an.' + '\n';
    
    elif is_cmd('db_print', name):
        print('db' + str(db.maindb));
        output = 'Output to Large, wrote into Console';
    else:
        output += 'Zugriff nicht möglich!'+'\n';
        
    return output;

