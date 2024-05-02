#Input either the Atomic Number, Element Abbreviation, Element Name, Electron Configuration, or Abbreviated Electron Configuration and 
#the program will output the name, Abbrev. Name, Row/Column number, Atomic Radius, Atomic Weight, and Electron Configuration. 
print('Input the Atomic Num., Element Abbrev., Element Name, Electron Config., or Abbrev. Electron Config.')
user = input('> ')
hydrogen = ['H','Hydrogen','1s1','1']
helium = ['He','Helium','1s2','2']
lithium = ['Li','Lithium','1s2 2s1','3']
beryllium = ['Be','Beryllium','1s2 2s2','4']
boron = ['Boron','B','5','1s2 2s2 2p1']
carbon = ['6','carbon','C','1s2 2s2 2p2']
nitrogen = ['7','nitrogen','N','1s2 2s2 2p3']
oxygen = ['8','oxygen','O','1s2 2s2 2p4']
fluorine = ['9','F','fluorine','1s2 2s2 2p5']
neon = ['10','Ne','neon','1s2 2s2 2p6']
sodium = ['11','Na','sodium','1s2 2s2 2p6 3s1','[Ne] 3s1']
magnesium = ['12','Mg','magnesium','1s2 2s2 2p6 3s2','[Ne] 3s2']
aluminum = ['13','Al','aluminum','1s2 2s2 2p6 3s2 3p1','[Ne 3s2 3p1]']
silicon = ['14','Si','silicon','1s2 2s2 2p6 3s2 3p2']
phosphorus = ['15','P','phosphorus','1s2 2s2 2p6 3s2 3p3','[Ne] 3s2 3p3']
sulfur = ['16','S','sulfur','1s2 2s2 2p6 3s2 3p4','[Ne] 3s2 3p4']
chlorine = ['17','Cl','chlorine','1s2 2s2 2p6 3s2 3p5','[Ne] 3s2 3p5']
argon = ['18','Ar','argon','1s2 2s2 2p6 3s2 3p6','[Ne] 3s2 3p6']
potassium = ['19','K','potassium','1s2 2s2 2p6 3s2 3p6 4s1','[Ar] 4s1']
calcium = ['20','Ca','calcium','1s2 2s2 2p6 3s2 3p6 4s2','[Ar] 4s2']
scandium = ['21','Sc','scandium','1s2 2s2 2p6 3s2 3p6 4s2 3d1','[Ar] 4s2 3d1']
titanium = ['22','Ti','titanium','1s2 2s2 2p6 3s2 3p6 4s2 3d2','[Ar] 4s2 3d2']
vanadium = ['23','V','vanadium','1s2 2s2 2p6 3s2 3p6 4s2 3d3','[Ar] 4s2 3d3']

if user in hydrogen:
    print('Hydrogen: H')
    print('Atomic Number: 1')
    print('Row 1; Column IA')
    print('Atomic Radius: 0.32 A')
    print('Atomic Weight: 1.00794(7) u')
    print('Electron Configuration: 1s1')
elif user in helium:
    print('Helium: He')
    print('Atomic Number: 2')
    print('Row 1; Column VIIIA')
    print('Atomic Radius: 0.37 A')
    print('Atomic Weight: 4.002602(2) u')
    print('Electron Configuration: 1s2')
elif user in lithium:
    print('Lithium: Li')
    print('Atomic Number: 3')
    print('Row: 2; Column IA')
    print('Atomic Radius: 1.30 A')
    print('Atomic Weight: 6.941(2) u')
    print('Electron Configuration: 1s2 2s1')
elif user in beryllium:
    print('Beryllium: Be')
    print('Atomic Number: 4')
    print('Row: 2; Column: IIA')
    print('Atomic Radius: 0.99 A')
    print('Atomic Weight: 9.0121182(3) u')
    print('Electron Configuration: 1s2 2s2')
elif user in boron:
    print('Boron: B')
    print('Atomic Number: 5')
    print('Row: 2; Column: IIIA')
    print('Atomic Radius: 0.84 A')
    print('Atomic Weight: 10.811(7) u')
    print('Electron Configuration: 1s2 2s2 2p1')
elif user in carbon:
    print('Carbon: C')
    print('Atomic Number: 6')
    print('Row: 2; Column: IVA')
    print('Atomic Radius: 0.75 A')
    print('Atomic Weight: 12.0107(8) u')
    print('Electron Configuration: 1s2 2s2 2p2')
elif user in nitrogen:
    print('Nitrogen: N')
    print('Atomic Number: 7')
    print('Row: 2; Column: VA')
    print('Atomic Radius: 0.71 A')
    print('Atomic Weight: 14.0067(2) u')
    print('Electron Configuration: 1s2 2s2 2p3')
elif user in oxygen:
    print('Oxygen: O')
    print('Atomic Number: 8')
    print('Row: 2; Column: VIA')
    print('Atomic Radius: 0.64 A')
    print('Atomic Weight: 15.9994(3) u')
    print('Electron Configuration: 1s2 2s2 2p4')
elif user in fluorine:
    print('Fluorine: F')
    print('Atomic Number: 9')
    print('Row: 2; Column: VIIA')
    print('Atomic Radius: 0.60 A')
    print('Atomic Weight: 18.99840352(5) u')
    print('Electron Configuration: 1s2 2s2 2p5')
elif user in neon:
    print('Neon: Ne')
    print('Atomic Number: 10')
    print('Row: 2; Column: VIIIA')
    print('Atomic Radius: 0.62 A')
    print('Atomic Weight: 20.1797(6) u')
    print('Electron Configuration: 1s2 2s2 2p6')
elif user in sodium:
    print('Sodium: Na')
    print('Atomic Number: 11')
    print('Row: 3; Column: IA')
    print('Atomic Radius: 1.60 A')
    print('Atomic Weight: 22.98976928(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s1')
    print('Abbreviated Electron Configuration: [Ne] 3s1')
elif user in magnesium:
    print('Magnesium: Mg')
    print('Atomic Number: 12')
    print('Row: 3; Column: IIA')
    print('Atomic Radius: 1.40 A')
    print('Atomic Weight: 24.3050(6)')
    print('Electron Configuration: 1s2 2s2 2p6 3s2')
    print('Abbreviated Electron Configuration: [Ne] 3s2')
elif user in aluminum:
    print('Aluminum: Al')
    print('Atomic Number: 13')
    print('Row: 3; Column: IIIA')
    print('Atomic Radius: 1.24 A')
    print('Atomic Weight: 26.9815386(8) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p1')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p1')
elif user in silicon:
    print('Silicon: Si')
    print('Atomic Number: 14')
    print('Row: 3; Column: IVA')
    print('Atomic Radius: 1.14 A')
    print('Atomic Weight: 28.0855(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p2')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p2')
elif user in phosphorus:
    print('Phosphorus: P')
    print('Atomic Number: 15')
    print('Row: 3; Column: VA')
    print('Atomic Radius: 1.09 A')
    print('Atomic Weight: 30.973762(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p3')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p3')
elif user in sulfur:
    print('Sulfur: S')
    print('Atomic Number: 16')
    print('Row: 3; Column: VIA')
    print('Atomic Radius: 1.00 A')
    print('Atomic Weight: 32.065(5) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p4')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p4')
elif user in chlorine:
    print('Chlorine: Cl')
    print('Atomic Number: 17')
    print('Row: 3; Column: VIIA')
    print('Atomic Radius: 1.00 A')
    print('Atomic Weight: 35.453(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p5')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p5')
elif user in argon:
    print('Argon: Ar')
    print('Atomic Number: 18')
    print('Row: 3; Column: VIIIA')
    print('Atomic Radius: 1.01 A')
    print('Atomic Weight: 39.948(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6')
    print('Abbreviated Electron Configuration: [Ne] 3s2 3p6')
elif user in potassium:
    print('Potassium: K')
    print('Atomic Number: 19')
    print('Row: 4; Column: IA')
    print('Atomic Radius: 2.00 A')
    print('Atomic Weight: 39.0983(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s1')
    print('Abbreviated Electron Configuration: [Ar] 4s1')
elif user in calcium:
    print('Calcium: Ca')
    print('Atomic Number: 20')
    print('Row: 4; Column: IIA')
    print('Atomic Radius: 1.74 A')
    print('Atomic Weight: 40.078(4) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2')
    print('Abbreviated Electron Configuration: [Ar] 4s2')
elif user in scandium:
    print('Scandium: Sc')
    print('Atomic Number: 21')
    print('Row: 4; Column IIIB')
    print('Atomic Radius: 1.59 A')
    print('Atomic Weight: 44.955912(6) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d1')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d1')
elif user in titanium:
    print('Titanium: Ti')
    print('Atomic Number: 22')
    print('Row: 4; Column IVA')
    print('Atomic Radius: 1.48 A')
    print('Atomic Weight: 47.867(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d2')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d2')
elif user in vanadium:
    print('Vanadium: V')
    print('Atomic Number: 23')
    print('Row: 4; Column: VB')
    print('Atomic Radius: 1.44 A')
    print('Atomic Weight: 50.9415(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d3')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d3')
elif user == str(24) or user == 'Cr' or user.lower() == 'chromium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d4' or \
        user == '[Ar] 4s2 3d4':
    print('Chromium: Cr')
    print('Atomic Number: 24')
    print('Row: 4; Column: VIB')
    print('Atomic Radius: 1.30 A')
    print('Atomic Weight: 51.9961(6) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d4')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d4')
elif user == str(25) or user == 'Mn' or user.lower() == 'manganese' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d5' or \
        user == '[Ar] 4s2 3d5':
    print('Manganese: Mn')
    print('Atomic Number: 25')
    print('Row: 4; Column: VIIB')
    print('Atomic Radius: 1.29 A')
    print('Atomic Weight: 54.938045 u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d5')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d5')
elif user == str(26) or user == 'Fe' or user.lower() == 'iron' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d6' or \
        user == '[Ar] 4s2 3d6':
    print('Iron: Fe')
    print('Atomic Number: 26')
    print('Row: 4; Column: VIIIB')
    print('Atomic Radius: 1.24 A')
    print('Atomic Weight: 55.845(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d6')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d6')
elif user == str(27) or user == 'Co' or user.lower() == 'cobalt' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d7' or \
        user == '[Ar] 4s2 3d7':
    print('Cobalt: Co')
    print('Atomic Number: 27')
    print('Row: 4; Column: VIIIB')
    print('Atomic Radius: 1.18 A')
    print('Atomic Weight: 58.933195(5) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d7')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d7')
elif user == str(28) or user == 'Ni' or user.lower() == 'nickel' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d8' or \
        user == '[Ar] 4s2 3d8':
    print('Nickel: Ni')
    print('Atomic Number: 28')
    print('Row: 4; Column: VIIIB')
    print('Atomic Radius: 1.17 A')
    print('Atomic Weight: 58.6934(4) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d8')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d8')
elif user == str(29) or user == 'Cu' or user.lower() == 'copper' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d9' or \
        user == '[Ar] 4s2 3d9':
    print('Copper: Cu')
    print('Atomic Number: 29')
    print('Row: 4; Column: IB')
    print('Atomic Radius: 1.22 A')
    print('Atomic Weight: 63.546(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d9')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d9')
elif user == str(30) or user == 'Zn' or user.lower() == 'zinc' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10' or \
        user == '[Ar] 4s2 3d10':
    print('Zinc: Zn')
    print('Atomic Number: 30')
    print('Row: 4; Column: IIB')
    print('Atomic Radius: 1.20 A')
    print('Atomic Weight: 65.38(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10')
elif user == str(31) or user == 'Ga' or user.lower() == 'gallium' or user == '1s2 2s2 2p6 3s2 4s2 3d10 4p1' or \
        user == '[Ar] 4s2 3d10 4p1':
    print('Gallium: Ga')
    print('Atomic Number: 31')
    print('Row: 4; Column: IIIA')
    print('Atomic Radius: 1.23 A')
    print('Atomic Weight: 69.723(1)')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p1')
elif user == str(32) or user == 'Ge' or user.lower() == 'germanium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2' or \
        user == '[Ar] 4s2 3d10 4p2':
    print('Germanium: Ge')
    print('Atomic Number: 32')
    print('Row: 4; Column: IVA')
    print('Atomic Radius: 1.20 A')
    print('Atomic Weight: 72.64(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p2')
elif user == str(33) or user == 'As' or user.lower() == 'arsenic' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3' or \
        user == '[Ar] 4s2 3d10 4p3':
    print('Arsenic: As')
    print('Atomic Number: 33')
    print('Row: 4; Column: VA')
    print('Atomic Radius: 1.20 A')
    print('Atomic Weight: 74.92160(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p3')
elif user == str(34) or user == 'Se' or user.lower() == 'selenium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4' or \
        user == '[Ar] 4s2 3d10 4p4':
    print('Selenium: Se')
    print('Atomic Number: 34')
    print('Row 4; Column VIA')
    print('Atomic Radius: 1.18 A')
    print('Atomic Weight: 78.96(3)')
    print('Electron Configuration: 1s2 2s2 2p6 3p6 4s2 3d10 4p4')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p4')
elif user == str(35) or user == 'Br' or user.lower() == 'bromine' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5' or \
        user == '[Ar] 4s2 3d10 4p5':
    print('Bromine: Br')
    print('Atomic Number: 35')
    print('Row 4; Column VIIA')
    print('Atomic Radius: 1.17 A')
    print('Atomic Weight: 79.904(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p5')
elif user == str(36) or user == 'Kr' or user.lower() == 'krypton' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6' or \
        user == '[Ar] 4s2 3d10 4p6':
    print('Krypton: Kr')
    print('Atomic Number: 36')
    print('Row 4; Column VIIIA')
    print('Atomic Radius: 1.16 A')
    print('Atomic Weight: 83.798(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6')
    print('Abbreviated Electron Configuration: [Ar] 4s2 3d10 4p6')
elif user == str(37) or user == 'Rb' or user.lower() == 'rubidium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1' or\
        user == '[Kr] 5s1':
    print('Rubidium: Rb')
    print('Atomic Number: 37')
    print('Row 5; Column IA')
    print('Atomic Radius: 2.15 A')
    print('Atomic Weight: 85.4678(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1')
    print('Abbreviated Electron Configuration: [Kr] 5s1')
elif user == str(38) or user == 'Sr' or user.lower() == 'strontium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
        or user == '[Kr] 5s2':
    print('Strontium: Sr')
    print('Atomic Number: 38')
    print('Row 5; Column IIA')
    print('Atomic Radius: 1.90 A')
    print('Atomic Weight: 87.62(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2')
    print('Abbreviated Electron Configuration: [Kr] 5s2')
elif user == str(39) or user == 'Y' or user.lower() == 'yttrium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1' \
        or user == '[Kr] 5s2 4d1':
    print('Yttrium: Y')
    print('Atomic Number: 39')
    print('Row 5; Column IIIB')
    print('Atomic Radius: 1.76 A')
    print('Atomic Weight: 88.90585(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d1')
elif user == str(40) or user == 'Zr' or user.lower() == 'zirconium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                               '4d2' \
        or user == '[Kr] 5s2 4d2':
    print('Zirconium: Zr')
    print('Atomic Number: 40')
    print('Row 5; Column IVB')
    print('Atomic Radius: 1.64 A')
    print('Atomic Weight: 91.224(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d2')
elif user == str(41) or user == 'Nb' or user.lower() == 'niobium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3'\
         or user == '[Kr] 5s2 4d3':
    print('Niobium: Nb')
    print('Atomic Number: 41')
    print('Row 5; Column VB')
    print('Atomic Radius: 1.56 A')
    print('Atomic Weight: 92.90638(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d3')
elif user == str(42) or user == 'Mo' or user.lower() == 'molybdenum' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                                '4d4'\
         or user == '[Kr] 5s2 4d4':
    print('Molybdenum: Mo')
    print('Atomic Number: 42')
    print('Row 5; Column VIB')
    print('Atomic Radius: 1.46 A')
    print('Atomic Weight: 95.96(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d4')
elif user == str(43) or user == 'Tc' or user.lower() == 'technetium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                                '4d5'\
         or user == '[Kr] 5s2 4d5':
    print('Technetium: Tb')
    print('Atomic Number: 43')
    print('Row 5; Column VIIB')
    print('Atomic Radius: 1.38 A')
    print('Atomic Weight: [97.9072] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d5')
elif user == str(44) or user == 'Ru' or user.lower() == 'ruthenium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                               '4d6'\
         or user == '[Kr] 5s2 4d6':
    print('Ruthenium: Ru')
    print('Atomic Number: 44')
    print('Row 5; Column VIIIB')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: 101.07 u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d6')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d6')
elif user == str(45) or user == 'Rh' or user.lower() == 'rhodium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7'\
         or user == '[Kr] 5s2 4d7':
    print('Rhodium; Rh')
    print('Atomic Number: 45')
    print('Row 5; Column VIIIB')
    print('Atomic Radius: 1.34 A')
    print('Atomic Weight: 102.90550(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d7')
elif user == str(46) or user == 'Pd' or user.lower() == 'palladium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                               '4d8' \
         or user == '[Kr] 5s2 4d8':
    print('Palladium: Pd')
    print('Atomic Number: 46')
    print('Row 5; Column VIIIB')
    print('Atomic Radius: 1.30 A')
    print('Atomic Weight: 106.42(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d8')
elif user == str(47) or user == 'Ag' or user.lower() == 'silver' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d9':
    print('Silver: Ag')
    print('Atomic Number: 47')
    print('Row 5; Column IB')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: 107.8682(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d9')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d9')
elif user == str(48) or user == 'Cd' or user.lower() == 'cadmium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10' \
        or user == '[Kr] 5s2 4d10':
    print('Cadmium: Cd')
    print('Atomic Number: 48')
    print('Row 5; Column IIB')
    print('Atomic Radius: 1.40 A')
    print('Atomic Weight: 112.411(8) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10')
elif user == str(49) or user == 'In' or user.lower() == 'indium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10'\
                                                                            ' 5p1'\
         or user == '[Kr] 5s2 4d10 5p1':
    print('Indium: In')
    print('Atomic Number: 49')
    print('Row 5; Column IIIA')
    print('Atomic Radius: 1.42 A')
    print('Atomic Weight: 114.818(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p1')
elif user == str(50) or user == 'Sn' or user.lower() == 'tin' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10' \
                                                                         ' 5p2' \
        or user == '[Kr] 5s2 4d10 5p2':
    print('Tin: Sn')
    print('Atomic Number: 50')
    print('Row 5; Column IVA')
    print('Atomic Radius: 1.40 A')
    print('Atomic Weight: 118.710(7) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p2')
elif user == str(51) or user == 'Sb' or user.lower() == 'antimony' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                              ' 4d10 5p3'\
         or user == '[Kr] 5s2 4d10 5p3':
    print('Antimony: Sb')
    print('Atomic Number: 51')
    print('Row 5; Column VA')
    print('Atomic Radius: 1.40 A')
    print('Atomic Weight: 121.760(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p3')
elif user == str(52) or user == 'Te' or user.lower() == 'tellurium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                               ' 4d10 5p4'\
         or user == '[Kr] 5s2 4d10 5p4':
    print('Tellurium: Te')
    print('Atomic Number: 52')
    print('Row 5; Column VIA')
    print('Atomic Radius: 1.37 A')
    print('Atomic Weight: 127.60(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p4')
elif user == str(53) or user == 'I' or user.lower() == 'iodine' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10' \
                                                                           ' 5p5'\
         or user == '[Kr] 5s2 4d10 5p5':
    print('Iodine: I')
    print('Atomic Number: 53')
    print('Row 5; Column VIIA')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: 126.90447(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p5')
elif user == str(54) or user == 'Xe' or user.lower() == 'xenon' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10' \
                                                                           ' 5p6'\
         or user == '[Kr] 5s2 4d10 5p6':
    print('Xenon: Xe')
    print('Atomic Number: 54')
    print('Row 5; Column VIIIA')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: 131.293(6) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6')
    print('Abbreviated Electron Configuration: [Kr] 5s2 4d10 5p6')
elif user == str(55) or user == 'Cs' or user.lower() == 'caesium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s1'\
         or user == '[Xe] 6s1':
    print('Caesium: Cs')
    print('Atomic Number: 55')
    print('Row 6; Column IA')
    print('Atomic Radius: 2.38 A')
    print('Atomic Weight: 132.9054519(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1')
    print('Abbreviated Electron Configuration: [Xe] 6s1')
elif user == str(56) or user == 'Ba' or user.lower() == 'barium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                            '4d10 5p6 6s2'\
         or user == '[Xe] 6s2':
    print('Barium: Ba')
    print('Atomic Number: 56')
    print('Row 6; Column IIA')
    print('Atomic Radius: 2.06 A')
    print('Atomic Weight: 137.327(7) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2')
    print('Abbreviated Electron Configuration: [Xe] 6s2')
elif user == str(57) or user == 'La' or user.lower() == 'lanthanum' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                               '4d10 5p6 6s2 5d1'\
         or user == '[Xe] 6s2 4f1':
    print('Lanthanum: La')
    print('Atomic Number: 57')
    print('Row 6; Column IVB')
    print('Atomic Radius: 1.94 A')
    print('Atomic Weight: 138.90547(7) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f1')
elif user == str(58) or user == 'Ce' or user.lower() == 'cerium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                            '4d10 5p6 6s2 5d1'\
         or user == '[Xe] 6s2 4f2':
    print('Cerium: Ce')
    print('Atomic Number: 58')
    print('Row 6; Column VB')
    print('Atomic Radius: 1.84 A')
    print('Atomic Weight: 140.116(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f2')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f2')
elif user == str(59) or user == 'Pr' or user.lower() == 'praseodymium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6' \
                                                                                  ' 5s2 4d10 5p6 6s2 5d1 4f1'\
         or user == '[Xe] 6s2 4f3':
    print('Praseodymium: Pr')
    print('Atomic Number: 59')
    print('Row 6; Column VIB')
    print('Atomic Radius: 1.90 A')
    print('Atomic Weight: 140.90765(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f3')
elif user == str(60) or user == 'Nd' or user.lower() == 'neodymium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                               '4d10 5p6 6s2 4f4'\
         or user == '[Xe] 6s2 4f4':
    print('Neodymium: Nd')
    print('Atomic Number: 60')
    print('Row 6; Column VIIB')
    print('Atomic Radius: 1.88 A')
    print('Atomic Weight: 144.242(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f4')
elif user == str(61) or user == 'Pm' or user.lower() == 'promethium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                                ' 4d10 5p6 6s2 4f5' \
        or user == '[Xe] 6s2 4f5':
    print('Promethium: Pm')
    print('Atomic Number: 61')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.86 A')
    print('Atomic Weight: [144.9127] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f5')
elif user == str(62) or user == 'Sm' or user.lower() == 'samarium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 4f6' \
        or user == '[Xe] 6s2 4f6':
    print('Samarium: Sm')
    print('Atomic Number: 62')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.85 A')
    print('Atomic Weight: 150.36(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f6')
elif user == str(63) or user == 'Eu' or user.lower() == 'europium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 4f7' \
        or user == '[Xe] 6s2 4f7':
    print('Europium: Eu')
    print('Atomic Number: 63')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.83 A')
    print('Atomic Weight: 151.964(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f7')
elif user == str(64) or user == 'Gd' or user.lower() == 'gadolinium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2' \
                                                                                ' 4d10 5p6 6s2 4f8' \
        or user == '[Xe] 6s2 4f8':
    print('Gadolinium: Gd')
    print('Atomic Number: 64')
    print('Row 6; Column IB')
    print('Atomic Radius: 1.82 A')
    print('Atomic Weight: 157.25(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f8')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f8')
elif user == str(65) or user == 'Tb' or user.lower() == 'terbium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 4f9' \
        or user == '[Xe] 6s2 4f9':
    print('Terbium: Tb')
    print('Atomic Number: 65')
    print('Row 6; Column IIB')
    print('Atomic Radius: 1.81 A')
    print('Atomic Weight: 158.92535(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f9')
elif user == str(66) or user == 'Dy' or user.lower() == 'dysprosium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 '\
                                                                                '4d10 5p6 6s2 4f10' \
        or user == '[Xe] 6s2 4f10':
    print('Dysprosium: Dy')
    print('Atomic Number: 66')
    print('Row 6; Column IIIA')
    print('Atomic Radius: 1.80 A')
    print('Atomic Weight: 162.500(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 3d10 4p6 5s2 4d10 5p6 6s2 4f10')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f10')
elif user == str(67) or user == 'Ho' or user.lower() == 'holmium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 4f11' \
        or user == '[Xe] 6s2 4f11':
    print('Holmium: Ho')
    print('Atomic Number: 67')
    print('Row 6; Column IVA')
    print('Atomic Radius: 1.79 A')
    print('Atomic Weight: 164.93032(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f11')
elif user == str(68) or user == 'Er' or user.lower() == 'erbium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                            '4d10 5p6 6s2 4f12' \
        or user == '[Xe] 6s2 4f12':
    print('Erbium: Er')
    print('Atomic Number: 68')
    print('Row 6; Column VA')
    print('Atomic Radius: 1.77 A')
    print('Atomic Weight: 167.259(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f12')
elif user == str(69) or user == 'Tm' or user.lower() == 'thulium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 4f13' \
        or user == '[Xe] 6s2 4f13':
    print('Thulium: Tm')
    print('Atomic Number: 69')
    print('Row 6; Column VIA')
    print('Atomic Radius: 1.77 A')
    print('Atomic Weight: 168.93421(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f13')
elif user == str(70) or user == 'Yb' or user.lower() == 'ytterbium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                               '4d10 5p6 6s2 4f14' \
        or user == '[Xe] 6s2 4f14':
    print('Ytterbium: Yb')
    print('Atomic Number: 70')
    print('Row 6; Column VIIA')
    print('Atomic Radius: 1.78 A')
    print('Atomic Weight: 173.0545(5) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 4f14')
elif user == str(71) or user == 'Lu' or user.lower() == 'lutetium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d1 4f14' \
        or user == '[Xe] 6s2 5d1 4f14':
    print('Lutetium: Lu')
    print('Atomic Number: 71')
    print('Row 6; Column VIIIA')
    print('Atomic Radius: 1.74 A')
    print('Atomic Weight: 174.9668(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d1 4f14')
elif user == str(72) or user == 'Hf' or user.lower() == 'hafnium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d2 4f14' \
        or user == '[Xe] 6s2 5d2 4f14':
    print('Hafnium: Hf')
    print('Atomic Number: 72')
    print('Row 6; Column IVB')
    print('Atomic Radius: 1.64 A')
    print('Atomic Weight: 178.49(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d2 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d2 4f14')
elif user == str(73) or user == 'Ta' or user.lower() == 'tantalum' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d3 4f14' \
        or user == '[Xe] 6s2 5d3 4f14':
    print('Tantalum: Ta')
    print('Atomic Number: 73')
    print('Row 6; Column VB')
    print('Atomic Radius: 1.58 A')
    print('Atomic Weight: 180.94.788(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d3 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d3 4f15')
elif user == str(74) or user == 'W' or user.lower() == 'tungsten' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d4 4f14' \
        or user == '[Xe] 6s2 5d4 4f14':
    print('Tungsten: W')
    print('Atomic Number: 74')
    print('Row 6; Column VIB')
    print('Atomic Radius: 1.50 A')
    print('Atomic Weight: 183.849(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d4 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d4 4f14')
elif user == str(75) or user == 'Re' or user.lower() == 'rhenium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d5 4f14' \
        or user == '[Xe] 6s2 5d5 4f14':
    print('Rhenium: Re')
    print('Atomic Number: 75')
    print('Row 6; Column VIIB')
    print('Atomic Radius: 1.41 A')
    print('Atomic Weight: 186.207(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d5 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d5 4f14')
elif user == str(76) or user == 'Os' or user.lower() == 'osmium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                            '4d10 5p6 6s2 5d6 4f14' \
        or user == '[Xe] 6s2 5d6 4f14':
    print('Osmium: Os')
    print('Atomic Number: 76')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: 190.23(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d6 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d6 4f14')
elif user == str(77) or user == 'Ir' or user.lower() == 'iridium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d7 4f14' \
        or user == '[Xe] 6s2 5d7 4f14':
    print('Iridium: Ir')
    print('Atomic Number: 77')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.32 A')
    print('Atomic Weight: 192.217(3) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d7 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d7 4f14')
elif user == str(78) or user == 'Pt' or user.lower() == 'platinum' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s1 5d9 4f14' \
        or user == '[Xe] 6s1 5d9 4f14':
    print('Platinum: Pt')
    print('Atomic Number: 78')
    print('Row 6; Column VIIIB')
    print('Atomic Radius: 1.30 A')
    print('Atomic Weight: 195.084(9) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 5d9 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s1 5d9 4f14')
elif user == str(79) or user == 'Au' or user.lower() == 'gold' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                          '4d10 5p6 6s1 5d10 4f14' \
        or user == '[Xe] 6s1 5d10 4f14':
    print('Gold: Au')
    print('Atomic Number: 79')
    print('Row 6; Column IB')
    print('Atomic Radius: 1.30 A')
    print('Atomic Weight: 196.966569(4) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 5d10 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s1 5d10 4f14')
elif user == str(80) or user == 'Hg' or user.lower() == 'mercury' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d10 4f14' \
        or user == '[Xe] 6s2 5d10 4f14':
    print('Mercury: Hg')
    print('Atomic Number: 80')
    print('Row 6; Column IIB')
    print('Atomic Radius: 1.32 A')
    print('Atomic Weight: 200.59(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14')
elif user == str(81) or user == 'Tl' or user.lower() == 'thallium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d10 4f14 6p1' \
        or user == '[Xe] 6s2 5d10 4f14 6p1':
    print('Thallium: Tl')
    print('Atomic Number: 81')
    print('Row 6; Column IIIA')
    print('Atomic Radius: 1.44 A')
    print('Atomic Weight: 204.3833(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p1')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p1')
elif user == str(82) or user == 'Pb' or user.lower() == 'Lead' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                          '4d10 5p6 6s2 5d10 4f14 6p2' \
        or user == '[Xe] 6s2 5d10 4f14 6p2':
    print('Lead: Pb')
    print('Atomic Number: 82')
    print('Row 6; Column IVA')
    print('Atomic Radius: 1.45 A')
    print('Atomic Weight: 207.2(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p2')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p2')
elif user == str(83) or user == 'Bi' or user.lower() == 'bismuth' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d10 4f14 6p3' \
        or user == '[Xe] 6s2 5d10 4f14 6p3':
    print('Bismuth: Bi')
    print('Atomic Number: 83')
    print('Row 6; Column VA')
    print('Atomic Radius: 1.50 A')
    print('Atomic Weight: 208.98040(1) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p3')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p3')
elif user == str(84) or user == 'Po' or user.lower() == 'Polonium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d10 4f14 6p4' \
        or user == '[Xe] 6s2 5d10 4f14 6p4':
    print('Polonium')
    print('Atomic Number: 84')
    print('Row 6; Column VIA')
    print('Atomic Radius: 1.42 A')
    print('Atomic Weight: [208.9824] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p4')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p4')
elif user == str(85) or user == 'At' or user.lower() == 'astatine' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d10 4f14 6p5' \
        or user == '[Xe] 6s2 5d10 4f14 6p5':
    print('Astatine: At')
    print('Atomic Number: 85')
    print('Row 6; Column VIIA')
    print('Atomic Radius: 1.48 A')
    print('Atomic Weight: [209.9871] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p5')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p5')
elif user == str(86) or user == 'Rn' or user.lower() == 'radon' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                           '4d10 5p6 6s2 5d10 4f14 6p6' \
        or user == '[Xe] 6s2 5d10 4f14 6p6':
    print('Radon: Rn')
    print('Atomic Number: 86')
    print('Row 6; Column VIIIA')
    print('Atomic Radius: 1.46 A')
    print('Atomic Weight: [222.0176] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6')
    print('Abbreviated Electron Configuration: [Xe] 6s2 5d10 4f14 6p6')
elif user == str(87) or user == 'Fr' or user.lower() == 'francium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d10 4f14 6p6 7s1' \
        or user == '[Rn] 7s1':
    print('')
    print('Atomic Number: 87')
    print('Row 7; Column IA')
    print('Atomic Radius: 2.42 A')
    print('Atomic Weight: [223.0197] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s1')
    print('Abbreviated Electron Configuration: [Rn] 7s1')
elif user == str(88) or user == 'Ra' or user.lower() == 'radium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                            '4d10 5p6 6s2 5d10 4f14 6p6 7s2' \
        or user == '[Rn] 7s2':
    print('Radium: Ra')
    print('Atomic Number: 88')
    print('Row 7; Column IIA')
    print('Atomic Radius: 2.11 A')
    print('Atomic Weight: [226.0254] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2')
    print('Abbreviated Electron Configuration: [Rn] 7s2')
elif user == str(89) or user == 'Ac' or user.lower() == 'actinium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                              '4d10 5p6 6s2 5d10 4f14 6p6 7s2 6d1' \
        or user == '[Rn] 7s2 6d1':
    print('Actinium: Ac')
    print('Atomic Number: 89')
    print('Row 7; Column IVB')
    print('Atomic Radius: 2.01 A')
    print('Atomic Weight: [227.0277] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 6d1')
    print('Abbreviated Electron Configuration: [Rn] 7s2 6d1')
elif user == str(90) or user == 'Th' or user.lower() == 'thorium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                             '4d10 5p6 6s2 5d10 4f14 6p6 7s2 6d2' \
        or user == '[Rn] 7s2 6d2':
    print('Thorium: Th')
    print('Atomic Number: 90')
    print('Row 7; Column VB')
    print('Atomic Radius: 1.90 A')
    print('Atomic Weight: 232.03806(2) u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 6d2')
    print('Abbreviated Electron Configuration: [Rn] 7s2 6d2')
elif user == str(91) or user == 'Pa' or user.lower() == 'protactinium':
    print('Protactinium')
    print('Atomic Number: 91')
    print('Row 7; Column VIB')
    print('Atomic Radius: 1.84 A')
    print('Atomic Weight: 231.03588(2) u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(92) or user == 'U' or user.lower() == 'uranium':
    print('Uranium: U')
    print('Atomic Number: 92')
    print('Row 7; Column VIIB')
    print('Atomic Radius: 1.83 A')
    print('Atomic Weight: 238.02891(3) u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(93) or user == 'Np' or user.lower() == 'neptunium':
    print('Neptunium: Np')
    print('Atomic Number: 93')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.80 A')
    print('Atomic Weight: [237.0482] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(94) or user == 'Pu' or user.lower() == 'plutonium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f6' \
        or user == '[Rn] 7s2 5f6':
    print('Plutonium: Pu')
    print('Atomic Number: 94')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.80 A')
    print('Atomic Weight: [244.0642] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f6')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f6')
elif user == str(95) or user == 'Am' or user.lower() == 'americium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f7' \
        or user == '[Rn] 7s2 5f7':
    print('Americium: Am')
    print('Atomic Number: 95')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.73 A')
    print('Atomic Weight: [243.0614] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f7')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f7')
elif user == str(96) or user == 'Cm' or user.lower() == 'curium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f7 6d1' \
        or user == '[Rn] 7s2 5f7 6d1':
    print('Curium: Cm')
    print('Atomic Number: 96')
    print('Row 7; Column IB')
    print('Atomic Radius: 1.68 A')
    print('Atomic Weight: [247.0704] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f7 6d1')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f7 6d1')
elif user == str(97) or user == 'Bk' or user.lower() == 'berkelium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f8 6d1' \
        or user == '[Rn] 7s2 5f8 6d1':
    print('Berkelium: Bk')
    print('Atomic Number: 97')
    print('Row 7; Column IIB')
    print('Atomic Radius: 1,68 A')
    print('Atomic Weight: [247.0703] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f8 6d1')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f8 6d1')
elif user == str(98) or user == 'Cf' or user.lower() == 'californium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                                 '5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f10' \
        or user == '[Rn] 7s2 5f10':
    print('Californium: Cf')
    print('Atomic Number: 98')
    print('Row 7; Column IIIA')
    print('Atomic Radius: 1.68 A')
    print('Atomic Weight: [251.0796] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f10')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f10')
elif user == str(99) or user == 'Es' or user.lower() == 'einsteinium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                                 '5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f11' \
        or user == '[Rn] 7s2 5f11':
    print('Einsteinium')
    print('Atomic Number: 99')
    print('Row 7; Column IVA')
    print('Atomic Radius: 1.65 A')
    print('Atomic Weight: [252.0830] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f11')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f11')
elif user == str(100) or user == 'Fm' or user.lower() == 'fermium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                    '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f12' \
        or user == '[Rn] 7s2 5f12':
    print('Fermium: Fm')
    print('Atomic Number: 100')
    print('Row 7; Column VA')
    print('Atomic Radius: 1.67 A')
    print('Atomic Weight: [257.0951] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f12')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f12')
elif user == str(101) or user == 'Md' or user.lower() == 'mendelevium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                                  '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f13' \
        or user == '[Rn] 7s2 5f13':
    print('Mendelevium: Md')
    print('Atomic Number: 101')
    print('Row 7; Column VIA')
    print('Atomic Radius: 1.73 A')
    print('Atomic Weight: [258.0984] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f13')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f13')
elif user == str(102) or user == 'No' or user.lower() == 'nobelium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14' \
        or user == '[Rn] 7s2 5f14':
    print('Nobelium: No')
    print('Atomic Number: 102')
    print('Row 7; Column VIIA')
    print('Atomic Radius: 1.76 A')
    print('Atomic Weight: [259.1010] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14')
elif user == str(103) or user == 'Lr' or user.lower() == 'lawrencium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 7p1 ?' \
        or user == '[Rn] 7s2 5f14 7p1 ?':
    print('Lawrencium: Lr')
    print('Atomic Number: 103')
    print('Row 7; Column VIIIA')
    print('Atomic Radius: 1.61 A')
    print('Atomic Weight: [262.1097] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 7p1 ?')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 7p1 ?')
elif user == str(104) or user == 'Rf' or user.lower() == 'rutherfordium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10' \
                                                                     ' 4p6 5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d2' \
        or user == '[Rn] 7s2 5f14 6d2':
    print('Rutherfordium: Rf')
    print('Atomic Number: 104')
    print('Row 7; Column IVB')
    print('Atomic Radius: 1.57 A')
    print('Atomic Weight: [261.1088] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d2')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d2')
elif user == str(105) or user == 'Db' or user.lower() == 'Dubnium':
    print('Dubnium: Db')
    print('Atomic Number: 104')
    print('Row 7; Column VB')
    print('Atomic Radius: 1.49 A')
    print('Atomic Weight: [262.1141] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(106) or user == 'Sg' or user.lower() == 'seaborgium':
    print('Seaborgium: Sg')
    print('Atomic Number: 104')
    print('Row 7; Column VIB')
    print('Atomic Radius: 1.43 A')
    print('Atomic Weight: [266.1219] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(107) or user == 'Bh' or user.lower() == 'bohrium':
    print('Bohrium: Bh')
    print('Atomic Number: 107')
    print('Row 7; Column VIIB')
    print('Atomic Radius: 1.41 A')
    print('Atomic Weight: [272] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(108) or user == 'Hs' or user.lower() == 'hassium':
    print('Hassium: Hs')
    print('Atomic Number: 108')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.34 A')
    print('Atomic Weight: [277] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(109) or user == 'Mt' or user.lower() == 'meitnerium':
    print('Meitnerium: Mt')
    print('Atomic Number: 109')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.29 A')
    print('Atomic Weight: [276] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(110) or user == 'Ds' or user.lower() == 'darmstadtium':
    print('Darmstadtium')
    print('Atomic Number: 110')
    print('Row 7; Column VIIIB')
    print('Atomic Radius: 1.28 A')
    print('Atomic Weight: [281] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(111) or user == 'Rg' or user.lower() == 'roentgenium':
    print('Roentgenium: Rg')
    print('Atomic Number: 111')
    print('Row 7; Column IB')
    print('Atomic Radius: 1.21 A')
    print('Atomic Weight: [280] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(112) or user == 'Cn' or user.lower() == 'copernicium':
    print('Copernicium: Cn')
    print('Atomic Number: 112')
    print('Row 7; Column IIB')
    print('Atomic Radius: 1.22 A')
    print('Atomic Weight: [285] u')
    print('Electron Configuration: ?')
    print('Abbreviated Electron Configuration: ?')
elif user == str(113) or user == 'Nh' or user.lower() == 'nihonium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 ' \
                                                                               '4d10 5p6 6s2 5d10 4f14 6p6 7s2 ' \
                                                                               '5f14 6d10 7p1' \
        or user == '[Rn] 7s2 5f14 6d10 7p1':
    print('Nihonium: Nh')
    print('Atomic Number: 113')
    print('Row 7; Column IIIA')
    print('Atomic Radius: 1.36 A')
    print('Atomic Weight: [286] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p1')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p1')
elif user == str(114) or user == 'Fl' or user.lower() == 'flerovium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p2' \
        or user == '[Rn] 7s2 5f14 6d10 7p2':
    print('Flerovium: Fl')
    print('Atomic Number: 114')
    print('Row 7; Column IVA')
    print('Atomic Radius: 1.43 A')
    print('Atomic Weight: [289] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p2')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p2')
elif user == str(115) or user == 'Mc' or user.lower() == 'moscovium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p3' \
        or user == '[Rn] 7s2 5f14 6d10 7p3':
    print('Moscovium: Mc')
    print('Atomic Number: 114')
    print('Row 7; Column VA')
    print('Atomic Radius: 1.62 A')
    print('Atomic Weight: [289] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p3')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p3')
elif user == str(116) or user == 'Lv' or user.lower() == 'livermorium' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p4' \
        or user == '[Rn] 7s2 5f14 6d10 7p4':
    print('Livermorium: Lv')
    print('Atomic Number: 116')
    print('Row 7; Column VIA')
    print('Atomic Radius: 1.75 A')
    print('Atomic Weight: [293] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p4')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p4')
elif user == str(117) or user == 'Ts' or user.lower() == 'tennessine' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p5' \
        or user == '[Rn] 7s2 5f14 6d10 7p5':
    print('Tennessine: Ts')
    print('Atomic Number: 117')
    print('Row 7; Column VIIA')
    print('Atomic Radius: 1.65 A')
    print('Atomic Weight: [294] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p5')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p5')
elif user == str(118) or user == 'Og' or user.lower() == 'oganesson' or user == '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 ' \
                                                                     '5s2 ' \
                                                                     '4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p6' \
        or user == '[Rn] 7s2 5f14 6d10 7p6':
    print('Oganesson: Og')
    print('Atomic Number: 118')
    print('Row 7; Column VIIIA')
    print('Atomic Radius: 1.57 A')
    print('Atomic Weight: [294] u')
    print('Electron Configuration: 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d10 4f14 6p6 7s2 5f14 6d10 7p6')
    print('Abbreviated Electron Configuration: [Rn] 7s2 5f14 6d10 7p6')
else:
    print("I don't quite understand that")