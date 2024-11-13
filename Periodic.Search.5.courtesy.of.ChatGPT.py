# Define the elements with relevant data in a dictionary format
periodic_elements = {
    'H': {
        'name': 'Hydrogen',
        'atomic_number': 1,
        'row_column': 'Row 1; Column IA',
        'atomic_radius': '0.32 A',
        'atomic_weight': '1.00794(7) u',
        'electron_configuration': '1s1',
        'abbreviated_electron_configuration': '1s1'
    },
    'He': {
        'name': 'Helium',
        'atomic_number': 2,
        'row_column': 'Row 1; Column VIIIA',
        'atomic_radius': '0.37 A',
        'atomic_weight': '4.002602(2) u',
        'electron_configuration': '1s2',
        'abbreviated_electron_configuration': '1s2'
    },
    'Li': {
        'name': 'Lithium',
        'atomic_number': 3,
        'row_column': 'Row 2; Column IA',
        'atomic_radius': '1.30 A',
        'atomic_weight': '6.941(2) u',
        'electron_configuration': '1s2 2s1',
        'abbreviated_electron_configuration': '[He] 2s1'
    },
    'Be': {
        'name': 'Beryllium',
        'atomic_number': 4,
        'row_column': 'Row 2; Column IIA',
        'atomic_radius': '0.93 A',
        'atomic_weight': '9.0122(1) u',
        'electron_configuration': '1s2 2s2',
        'abbreviated_electron_configuration': '[He] 2s2'
    },
    'B': {
        'name': 'Boron',
        'atomic_number': 5,
        'row_column': 'Row 2; Column IIIA',
        'atomic_radius': '0.82 A',
        'atomic_weight': '10.81(3) u',
        'electron_configuration': '1s2 2s2 2p1',
        'abbreviated_electron_configuration': '[He] 2s2 2p1'
    },
    'C': {
        'name': 'Carbon',
        'atomic_number': 6,
        'row_column': 'Row 2; Column IVA',
        'atomic_radius': '0.77 A',
        'atomic_weight': '12.011(7) u',
        'electron_configuration': '1s2 2s2 2p2',
        'abbreviated_electron_configuration': '[He] 2s2 2p2'
    },
    'N': {
        'name': 'Nitrogen',
        'atomic_number': 7,
        'row_column': 'Row 2; Column VA',
        'atomic_radius': '0.75 A',
        'atomic_weight': '14.007(2) u',
        'electron_configuration': '1s2 2s2 2p3',
        'abbreviated_electron_configuration': '[He] 2s2 2p3'
    },
    'O': {
        'name': 'Oxygen',
        'atomic_number': 8,
        'row_column': 'Row 2; Column VIA',
        'atomic_radius': '0.60 A',
        'atomic_weight': '15.999(4) u',
        'electron_configuration': '1s2 2s2 2p4',
        'abbreviated_electron_configuration': '[He] 2s2 2p4'
    },
    'F': {
        'name': 'Fluorine',
        'atomic_number': 9,
        'row_column': 'Row 2; Column VIIA',
        'atomic_radius': '0.64 A',
        'atomic_weight': '18.998403163(6) u',
        'electron_configuration': '1s2 2s2 2p5',
        'abbreviated_electron_configuration': '[He] 2s2 2p5'
    },
    'Ne': {
        'name': 'Neon',
        'atomic_number': 10,
        'row_column': 'Row 2; Column VIIIA',
        'atomic_radius': '0.38 A',
        'atomic_weight': '20.1797(6) u',
        'electron_configuration': '1s2 2s2 2p6',
        'abbreviated_electron_configuration': '[He] 2s2 2p6'
    },
    'Na': {
        'name': 'Sodium',
        'atomic_number': 11,
        'row_column': 'Row 3; Column IA',
        'atomic_radius': '1.54 A',
        'atomic_weight': '22.98976928 u',
        'electron_configuration': '1s2 2s2 2p6 3s1',
        'abbreviated_electron_configuration': '[Ne] 3s1'
    },
    'Mg': {
        'name': 'Magnesium',
        'atomic_number': 12,
        'row_column': 'Row 3; Column IIA',
        'atomic_radius': '1.30 A',
        'atomic_weight': '24.305(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2',
        'abbreviated_electron_configuration': '[Ne] 3s2'
    },
    'Al': {
        'name': 'Aluminum',
        'atomic_number': 13,
        'row_column': 'Row 3; Column IIIA',
        'atomic_radius': '1.18 A',
        'atomic_weight': '26.9815385(8) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p1',
        'abbreviated_electron_configuration': '[Ne] 3s2 3p1'
    },
    'Si': {
        'name': 'Silicon',
        'atomic_number': 14,
        'row_column': 'Row 3; Column IVA',
        'atomic_radius': '1.11 A',
        'atomic_weight': '28.085(7) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p2',
        'abbreviated_electro
    },
    'P': {
        'name': 'Phosphorus',
        'atomic_number': 15,
        'row_column': 'Row 3; Column VA',
        'atomic_radius': '1.07 A',
        'atomic_weight': '30.973761998(5) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p3',
        'abbreviated_electron_configuration': '[Ne] 3s2 3p3'
    },
    'S': {
        'name': 'Sulfur',
        'atomic_number': 16,
        'row_column': 'Row 3; Column VIA',
        'atomic_radius': '1.04 A',
        'atomic_weight': '32.06(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p4',
        'abbreviated_electron_configuration': '[Ne] 3s2 3p4'
    },
    'Cl': {
        'name': 'Chlorine',
        'atomic_number': 17,
        'row_column': 'Row 3; Column VIIA',
        'atomic_radius': '0.99 A',
        'atomic_weight': '35.45(6) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p5',
        'abbreviated_electron_configuration': '[Ne] 3s2 3p5'
    },
    'Ar': {
        'name': 'Argon',
        'atomic_number': 18,
        'row_column': 'Row 3; Column VIIIA',
        'atomic_radius': '0.71 A',
        'atomic_weight': '39.948(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6',
        'abbreviated_electron_configuration': '[Ne] 3s2 3p6'
    },
    'K': {
        'name': 'Potassium',
        'atomic_number': 19,
        'row_column': 'Row 4; Column IA',
        'atomic_radius': '2.27 A',
        'atomic_weight': '39.0983(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s1',
        'abbreviated_electron_configuration': '[Ar] 4s1'
    },
    'Ca': {
        'name': 'Calcium',
        'atomic_number': 20,
        'row_column': 'Row 4; Column IIA',
        'atomic_radius': '1.97 A',
        'atomic_weight': '40.078(4) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2',
        'abbreviated_electron_configuration': '[Ar] 4s2'
    },
    'Sc': {
        'name': 'Scandium',
        'atomic_number': 21,
        'row_column': 'Row 4; Column IIIB',
        'atomic_radius': '1.44 A',
        'atomic_weight': '44.955908(5) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d1',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d1'
    },
    'Ti': {
        'name': 'Titanium',
        'atomic_number': 22,
        'row_column': 'Row 4; Column IVB',
        'atomic_radius': '1.32 A',
        'atomic_weight': '47.867(5) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d2',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d2'
    },
    'V': {
        'name': 'Vanadium',
        'atomic_number': 23,
        'row_column': 'Row 4; Column VB',
        'atomic_radius': '1.28 A',
        'atomic_weight': '50.9415(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d3',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d3'
    },
    'Cr': {
        'name': 'Chromium',
        'atomic_number': 24,
        'row_column': 'Row 4; Column VIB',
        'atomic_radius': '1.28 A',
        'atomic_weight': '52.00(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d4',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d4'
    },
    'Mn': {
        'name': 'Manganese',
        'atomic_number': 25,
        'row_column': 'Row 4; Column VIIB',
        'atomic_radius': '1.26 A',
        'atomic_weight': '54.938044(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d5',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d5'
    },
    'Fe': {
        'name': 'Iron',
        'atomic_number': 26,
        'row_column': 'Row 4; Column VIIB',
        'atomic_radius': '1.18 A',
        'atomic_weight': '55.845(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d6',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d6'
    },
    'Co': {
        'name': 'Cobalt',
        'atomic_number': 27,
        'row_column': 'Row 4; Column VIIIB',
        'atomic_radius': '1.17 A',
        'atomic_weight': '58.933194(4) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d7',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d7'
    },
    'Ni': {
        'name': 'Nickel',
        'atomic_number': 28,
        'row_column': 'Row 4; Column VIII',
        'atomic_radius': '1.16 A',
        'atomic_weight': '58.6934(4) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d8',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d8'
    },
    'Cu': {
        'name': 'Copper',
        'atomic_number': 29,
        'row_column': 'Row 4; Column IB',
        'atomic_radius': '1.28 A',
        'atomic_weight': '63.546(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10'
    },
    'Zn': {
        'name': 'Zinc',
        'atomic_number': 30,
        'row_column': 'Row 4; Column IIB',
        'atomic_radius': '1.31 A',
        'atomic_weight': '65.38(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10'
    },
    'Ga': {
        'name': 'Gallium',
        'atomic_number': 31,
        'row_column': 'Row 4; Column IIIA',
        'atomic_radius': '1.26 A',
        'atomic_weight': '69.723(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p1'
    },
    'Ge': {
        'name': 'Germanium',
        'atomic_number': 32,
        'row_column': 'Row 4; Column IVA',
        'atomic_radius': '1.22 A',
        'atomic_weight': '72.63(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p2'
    },
    'As': {
        'name': 'Arsenic',
        'atomic_number': 33,
        'row_column': 'Row 4; Column VA',
        'atomic_radius': '1.19 A',
        'atomic_weight': '74.921595(6) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p3'
    },
    'Se': {
        'name': 'Selenium',
        'atomic_number': 34,
        'row_column': 'Row 4; Column VIA',
        'atomic_radius': '1.16 A',
        'atomic_weight': '78.971(8) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p4'
    },
    'Br': {
        'name': 'Bromine',
        'atomic_number': 35,
        'row_column': 'Row 4; Column VIIA',
        'atomic_radius': '1.14 A',
        'atomic_weight': '79.904(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p5'
    },
    'Kr': {
        'name': 'Krypton',
        'atomic_number': 36,
        'row_column': 'Row 4; Column VIIIA',
        'atomic_radius': '0.88 A',
        'atomic_weight': '83.798(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6',
        'abbreviated_electron_configuration': '[Ar] 4s2 3d10 4p6'
    },
    'Rb': {
        'name': 'Rubidium',
        'atomic_number': 37,
        'row_column': 'Row 5; Column IA',
        'atomic_radius': '2.65 A',
        'atomic_weight': '85.4678(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1',
        'abbreviated_electron_configuration': '[Kr] 5s1'
    },
    'Sr': {
        'name': 'Strontium',
        'atomic_number': 38,
        'row_column': 'Row 5; Column IIA',
        'atomic_radius': '2.15 A',
        'atomic_weight': '87.62(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2',
        'abbreviated_electron_configuration': '[Kr] 5s2'
    },
    'Y': {
        'name': 'Yttrium',
        'atomic_number': 39,
        'row_column': 'Row 5; Column IIIB',
        'atomic_radius': '1.22 A',
        'atomic_weight': '88.90584(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d1'
    },
    'Zr': {
        'name': 'Zirconium',
        'atomic_number': 40,
        'row_column': 'Row 5; Column IVB',
        'atomic_radius': '1.34 A',
        'atomic_weight': '91.224(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d2'
    },
    'Nb': {
        'name': 'Niobium',
        'atomic_number': 41,
        'row_column': 'Row 5; Column VB',
        'atomic_radius': '1.30 A',
        'atomic_weight': '92.90637(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d3'
    },
    'Mo': {
        'name': 'Molybdenum',
        'atomic_number': 42,
        'row_column': 'Row 5; Column VIB',
        'atomic_radius': '1.30 A',
        'atomic_weight': '95.95(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d4'
    },
    'Tc': {
        'name': 'Technetium',
        'atomic_number': 43,
        'row_column': 'Row 5; Column VIIB',
        'atomic_radius': '1.29 A',
        'atomic_weight': '98(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d5'
    },
    'Ru': {
        'name': 'Ruthenium',
        'atomic_number': 44,
        'row_column': 'Row 5; Column VIIIB',
        'atomic_radius': '1.25 A',
        'atomic_weight': '101.07(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d7'
    },
    'Rh': {
        'name': 'Rhodium',
        'atomic_number': 45,
        'row_column': 'Row 5; Column VIII',
        'atomic_radius': '1.24 A',
        'atomic_weight': '102.90550(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d8'
    },
    'Pd': {
        'name': 'Palladium',
        'atomic_number': 46,
        'row_column': 'Row 5; Column IX',
        'atomic_radius': '1.20 A',
        'atomic_weight': '106.42(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10'
    },
    'Ag': {
        'name': 'Silver',
        'atomic_number': 47,
        'row_column': 'Row 5; Column IBA',
        'atomic_radius': '1.44 A',
        'atomic_weight': '107.8682(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10',
        'abbreviated_electron_configuration': '[Kr] 5s1 4d10'
    },
    'Cd': {
        'name': 'Cadmium',
        'atomic_number': 48,
        'row_column': 'Row 5; Column IIB',
        'atomic_radius': '1.44 A',
        'atomic_weight': '112.414(4) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10'
    },
    'In': {
        'name': 'Indium',
        'atomic_number': 49,
        'row_column': 'Row 5; Column IIIA',
        'atomic_radius': '1.54 A',
        'atomic_weight': '114.818(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10 5p1'
    },
    'Sn': {
        'name': 'Tin',
        'atomic_number': 50,
        'row_column': 'Row 5; Column IVA',
        'atomic_radius': '1.41 A',
        'atomic_weight': '118.710(7) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10 5p2'
    },
    'Sb': {
        'name': 'Antimony',
        'atomic_number': 51,
        'row_column': 'Row 5; Column VA',
        'atomic_radius': '1.39 A',
        'atomic_weight': '121.760(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10 5p3'
    },
    'I': {
        'name': 'Iodine',
        'atomic_number': 53,
        'row_column': 'Row 5; Column VIIA',
        'atomic_radius': '1.33 A',
        'atomic_weight': '126.90447(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10 5p5'
    },
    'Xe': {
        'name': 'Xenon',
        'atomic_number': 54,
        'row_column': 'Row 5; Column VIIIA',
        'atomic_radius': '1.16 A',
        'atomic_weight': '131.293(6) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6',
        'abbreviated_electron_configuration': '[Kr] 5s2 4d10 5p6'
    },
    'Cs': {
        'name': 'Cesium',
        'atomic_number': 55,
        'row_column': 'Row 6; Column IA',
        'atomic_radius': '2.62 A',
        'atomic_weight': '132.90545196(6) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1',
        'abbreviated_electron_configuration': '[Xe] 6s1'
    },
    'Ba': {
        'name': 'Barium',
        'atomic_number': 56,
        'row_column': 'Row 6; Column IIA',
        'atomic_radius': '2.17 A',
        'atomic_weight': '137.327(7) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2',
        'abbreviated_electron_configuration': '[Xe] 6s2'
    },
    'La': {
        'name': 'Lanthanum',
        'atomic_number': 57,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.74 A',
        'atomic_weight': '138.90547(7) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1',
        'abbreviated_electron_configuration': '[Xe] 6s2 5d1'
    },
    'Ce': {
        'name': 'Cerium',
        'atomic_number': 58,
        'row_column': 'Row 6; Column IVB',
        'atomic_radius': '1.61 A',
        'atomic_weight': '140.116(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f1'
    },
    'Pr': {
        'name': 'Praseodymium',
        'atomic_number': 59,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.49 A',
        'atomic_weight': '140.90766(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f3'
    },
    'Nd': {
        'name': 'Neodymium',
        'atomic_number': 60,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.42 A',
        'atomic_weight': '144.242(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f4'
    },
    'Pm': {
        'name': 'Promethium',
        'atomic_number': 61,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.38 A',
        'atomic_weight': '145(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f5'
    },
    'Sm': {
        'name': 'Samarium',
        'atomic_number': 62,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.34 A',
        'atomic_weight': '150.36(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f6'
    },
    'Eu': {
        'name': 'Europium',
        'atomic_number': 63,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.30 A',
        'atomic_weight': '151.964(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f7'
    },
    'Gd': {
        'name': 'Gadolinium',
        'atomic_number': 64,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.26 A',
        'atomic_weight': '157.25(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f7 5d1'
    },
    'Tb': {
        'name': 'Terbium',
        'atomic_number': 65,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.23 A',
        'atomic_weight': '158.92535(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f9'
    },
    'Dy': {
        'name': 'Dysprosium',
        'atomic_number': 66,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.22 A',
        'atomic_weight': '162.500(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f10'
    },
    'Ho': {
        'name': 'Holmium',
        'atomic_number': 67,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.22 A',
        'atomic_weight': '164.93033(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f11'
    },
    'Er': {
        'name': 'Erbium',
        'atomic_number': 68,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.21 A',
        'atomic_weight': '167.259(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f12'
    },
    'Tm': {
        'name': 'Thulium',
        'atomic_number': 69,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.19 A',
        'atomic_weight': '168.93422(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f13'
    },
    'Yb': {
        'name': 'Ytterbium',
        'atomic_number': 70,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.18 A',
        'atomic_weight': '173.04(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14'
    },
    'Lu': {
        'name': 'Lutetium',
        'atomic_number': 71,
        'row_column': 'Row 6; Column IIIB',
        'atomic_radius': '1.17 A',
        'atomic_weight': '174.9668(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d1'
    },
    'Hf': {
        'name': 'Hafnium',
        'atomic_number': 72,
        'row_column': 'Row 6; Column IVB',
        'atomic_radius': '1.56 A',
        'atomic_weight': '178.49(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d2'
    },
    'Ta': {
        'name': 'Tantalum',
        'atomic_number': 73,
        'row_column': 'Row 6; Column VB',
        'atomic_radius': '1.47 A',
        'atomic_weight': '180.94788(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d3'
    },
    'W': {
        'name': 'Tungsten',
        'atomic_number': 74,
        'row_column': 'Row 6; Column VIB',
        'atomic_radius': '1.37 A',
        'atomic_weight': '183.84(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d4'
    },
    'Re': {
        'name': 'Rhenium',
        'atomic_number': 75,
        'row_column': 'Row 6; Column VIIB',
        'atomic_radius': '1.34 A',
        'atomic_weight': '186.207(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d5'
    },
    'Os': {
        'name': 'Osmium',
        'atomic_number': 76,
        'row_column': 'Row 6; Column VIIIB',
        'atomic_radius': '1.32 A',
        'atomic_weight': '190.23(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d6'
    },
    'Ir': {
        'name': 'Iridium',
        'atomic_number': 77,
        'row_column': 'Row 6; Column VIII',
        'atomic_radius': '1.28 A',
        'atomic_weight': '192.217(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d7'
    },
    'Pt': {
        'name': 'Platinum',
        'atomic_number': 78,
        'row_column': 'Row 6; Column IIB',
        'atomic_radius': '1.38 A',
        'atomic_weight': '195.084(9) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d8',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d8'
    },
    'Au': {
        'name': 'Gold',
        'atomic_number': 79,
        'row_column': 'Row 6; Column IBA',
        'atomic_radius': '1.44 A',
        'atomic_weight': '196.966569(4) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10',
        'abbreviated_electron_configuration': '[Xe] 6s1 4f14 5d10'
    },
    'Hg': {
        'name': 'Mercury',
        'atomic_number': 80,
        'row_column': 'Row 6; Column IIB',
        'atomic_radius': '1.44 A',
        'atomic_weight': '200.592(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10'
    },
    'Tl': {
        'name': 'Thallium',
        'atomic_number': 81,
        'row_column': 'Row 6; Column IIIA',
        'atomic_radius': '1.47 A',
        'atomic_weight': '204.38(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p1',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p1'
    },
    'Pb': {
        'name': 'Lead',
        'atomic_number': 82,
        'row_column': 'Row 6; Column IVA',
        'atomic_radius': '1.54 A',
        'atomic_weight': '207.2(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p2'
    },
    'Bi': {
        'name': 'Bismuth',
        'atomic_number': 83,
        'row_column': 'Row 6; Column VA',
        'atomic_radius': '1.56 A',
        'atomic_weight': '208.98040(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p3'
    },
    'Po': {
        'name': 'Polonium',
        'atomic_number': 84,
        'row_column': 'Row 6; Column VIA',
        'atomic_radius': '1.59 A',
        'atomic_weight': '208.98243(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p4'
    },
    'At': {
        'name': 'Astatine',
        'atomic_number': 85,
        'row_column': 'Row 6; Column VIIA',
        'atomic_radius': '1.60 A',
        'atomic_weight': '209(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p5'
    },
    'Rn': {
        'name': 'Radon',
        'atomic_number': 86,
        'row_column': 'Row 6; Column VIIIA',
        'atomic_radius': '1.60 A',
        'atomic_weight': '222(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6',
        'abbreviated_electron_configuration': '[Xe] 6s2 4f14 5d10 6p6'
    },
    'Fr': {
        'name': 'Francium',
        'atomic_number': 87,
        'row_column': 'Row 7; Column IA',
        'atomic_radius': '2.60 A',
        'atomic_weight': '223(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1',
        'abbreviated_electron_configuration': '[Rn] 7s1'
    },
    'Ra': {
        'name': 'Radium',
        'atomic_number': 88,
        'row_column': 'Row 7; Column IIA',
        'atomic_radius': '2.45 A',
        'atomic_weight': '226(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2'
    },
    'Ac': {
        'name': 'Actinium',
        'atomic_number': 89,
        'row_column': 'Row 7; Column IIIB',
        'atomic_radius': '2.40 A',
        'atomic_weight': '227(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2'
    },
    'Th': {
        'name': 'Thorium',
        'atomic_number': 90,
        'row_column': 'Row 7; Column IVB',
        'atomic_radius': '2.24 A',
        'atomic_weight': '232.0377(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f1'
    },
    'Pa': {
        'name': 'Protactinium',
        'atomic_number': 91,
        'row_column': 'Row 7; Column VIB',
        'atomic_radius': '2.24 A',
        'atomic_weight': '231.03588(2) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f2'
    },
    'U': {
        'name': 'Uranium',
        'atomic_number': 92,
        'row_column': 'Row 7; Column VIB',
        'atomic_radius': '2.19 A',
        'atomic_weight': '238.02891(3) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f3'
    },
    'Np': {
        'name': 'Neptunium',
        'atomic_number': 93,
        'row_column': 'Row 7; Column VIIB',
        'atomic_radius': '2.19 A',
        'atomic_weight': '237(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f4'
    },
    'Pu': {
        'name': 'Plutonium',
        'atomic_number': 94,
        'row_column': 'Row 7; Column VIIB',
        'atomic_radius': '2.20 A',
        'atomic_weight': '244(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f6'
    },
    'Am': {
        'name': 'Americium',
        'atomic_number': 95,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '2.10 A',
        'atomic_weight': '243(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f7'
    },
    'Cm': {
        'name': 'Curium',
        'atomic_number': 96,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '2.00 A',
        'atomic_weight': '247(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f8'
    },
    'Bk': {
        'name': 'Berkelium',
        'atomic_number': 97,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.90 A',
        'atomic_weight': '247(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f9'
    },
    'Cf': {
        'name': 'Californium',
        'atomic_number': 98,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.80 A',
        'atomic_weight': '251(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f10'
    },
    'Es': {
        'name': 'Einsteinium',
        'atomic_number': 99,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.70 A',
        'atomic_weight': '252(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f11'
    },
    'Fm': {
        'name': 'Fermium',
        'atomic_number': 100,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.60 A',
        'atomic_weight': '257(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f12'
    },
    'Md': {
        'name': 'Mendelevium',
        'atomic_number': 101,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.60 A',
        'atomic_weight': '258(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f13'
    },
    'No': {
        'name': 'Nobelium',
        'atomic_number': 102,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.60 A',
        'atomic_weight': '259(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14'
    },
    'Lr': {
        'name': 'Lawrencium',
        'atomic_number': 103,
        'row_column': 'Row 7; Column IIIA',
        'atomic_radius': '1.60 A',
        'atomic_weight': '262(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d1'
    },
    'Rf': {
        'name': 'Rutherfordium',
        'atomic_number': 104,
        'row_column': 'Row 7; Column IVB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '267(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d2'
    },
    'Db': {
        'name': 'Dubnium',
        'atomic_number': 105,
        'row_column': 'Row 7; Column VB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '270(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d3'
    },
    'Sg': {
        'name': 'Seaborgium',
        'atomic_number': 106,
        'row_column': 'Row 7; Column VIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '271(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d4'
    },
    'Bh': {
        'name': 'Bohrium',
        'atomic_number': 107,
        'row_column': 'Row 7; Column VIIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '270(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d5'
    },
    'Hs': {
        'name': 'Hassium',
        'atomic_number': 108,
        'row_column': 'Row 7; Column VIIIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '277(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d6'
    },
    'Mt': {
        'name': 'Meitnerium',
        'atomic_number': 109,
        'row_column': 'Row 7; Column VIII',
        'atomic_radius': '1.50 A',
        'atomic_weight': '278(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d7'
    },
    'Ds': {
        'name': 'Darmstadtium',
        'atomic_number': 110,
        'row_column': 'Row 7; Column IIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '281(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d8'
    },
    'Rg': {
        'name': 'Roentgenium',
        'atomic_number': 111,
        'row_column': 'Row 7; Column IIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '280(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d9'
    },
    'Cn': {
        'name': 'Copernicium',
        'atomic_number': 112,
        'row_column': 'Row 7; Column IIB',
        'atomic_radius': '1.50 A',
        'atomic_weight': '285(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10'
    },
    'Nh': {
        'name': 'Nihonium',
        'atomic_number': 113,
        'row_column': 'Row 7; Column IIIA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '284(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p1'
    },
    'Fl': {
        'name': 'Flerovium',
        'atomic_number': 114,
        'row_column': 'Row 7; Column IVA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '289(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p2'
    },
    'Mc': {
        'name': 'Moscovium',
        'atomic_number': 115,
        'row_column': 'Row 7; Column VA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '290(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p3'
    },
    'Lv': {
        'name': 'Livermorium',
        'atomic_number': 116,
        'row_column': 'Row 7; Column VIA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '293(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p4'
    },
    'Ts': {
        'name': 'Tennessine',
        'atomic_number': 117,
        'row_column': 'Row 7; Column VIIA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '294(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p5'
    },
    'Og': {
        'name': 'Oganesson',
        'atomic_number': 118,
        'row_column': 'Row 7; Column VIIIA',
        'atomic_radius': '1.50 A',
        'atomic_weight': '294(1) u',
        'electron_configuration': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2',
        'abbreviated_electron_configuration': '[Rn] 7s2 5f14 6d10 7p6'
    }
}


# Function to search for elements based on user input
def search_element(user_input):
    # Convert user input to uppercase to handle case-insensitivity
    user_input = user_input.strip().upper()
    
    # Check if the user input matches any element's symbol, name, electron config, or atomic number
    for symbol, details in periodic_elements.items():
        # Match based on element symbol, name, and electron configuration (abbreviated or full)
        if user_input == symbol or user_input == details['name'].lower() or user_input == details['electron_configuration'] or user_input == details['abbreviated_electron_configuration']:
            print(f"Element: {details['name']} ({symbol})")
            print(f"Atomic Number: {details['atomic_number']}")
            print(f"Row/Column: {details['row_column']}")
            print(f"Atomic Radius: {details['atomic_radius']}")
            print(f"Atomic Weight: {details['atomic_weight']}")
            print(f"Electron Configuration: {details['electron_configuration']}")
            return  # Exit after displaying the element details
    print("Element not found. Please check your input.")

# Main function to prompt the user for input
def main():
    print("Input the Atomic Number, Element Abbrev., Element Name, Electron Config., or Abbreviated Electron Config.")
    user_input = input('> ').strip()
    search_element(user_input)

# Run the program
if __name__ == "__main__":
    main()
