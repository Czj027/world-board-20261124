"""Headline ordering, summaries and print references for the UTC edition."""

LEADS = {
    3: (
        "NORTH AMERICA  /  JUSTICE",
        "US jury convicts Huawei",
        "The Brooklyn verdict covers trade-secret conspiracy, fraud and Iran sanctions violations. Huawei is a Chinese telecom group.",
        "U.S. JUSTICE DEPARTMENT  /  REUTERS",
        "verdict",
    ),
    2: (
        "EUROPE  /  WAR IN UKRAINE",
        "Russian strike kills two in Zaporizhzhia",
        "An overnight Russian strike hit residential buildings. Ukrainian officials reported two dead and more than 40 hurt.",
        "AP  /  AL JAZEERA",
        "ukraine",
    ),
    18: (
        "MIDDLE EAST  /  ENERGY",
        "Baghdad orders oilfield takeover",
        "Iraq directed its oil ministry to manage fields under Kurdish security control. Kurdish leaders rejected the order.",
        "REUTERS  /  AL JAZEERA",
        "oil",
    ),
}

FIGURES = [
    ("10 / 12", "guilty counts in Huawei case"),
    ("$41B", "Sanofi’s Insmed deal"),
    ("+8.99%", "Taiwan index at the close"),
    ("5,258", "England heat-death estimate"),
    ("36", "satellites from Kourou"),
]

# Each feature represents a single independently numbered news story.
DESK = {
    21: ("SAUDI ARABIA", "11 hurt as Riyadh tower hit", "Officials blame Houthis."),
    22: ("CHINA", "Shanghai party chief probed", "Chen sits on the Politburo."),
    1: ("TAIWAN / S. KOREA", "Asian chip shares rebound", "Taipei and Seoul led gains."),
    10: ("FRANCE / U.S.", "Sanofi agrees $41B takeover", "$175 per Insmed share."),
    27: ("MALAYSIA", "Malaysia to send 6,803 back", "Myanmar nationals due back."),
    19: ("STRAIT OF HORMUZ", "Iran says tankers hit mines", "Mine claim is unverified."),
    14: ("SENEGAL", "Senegal regains Africa Cup title", "1–0 over Morocco restored."),
    11: ("ENGLAND", "Record heat-death estimate", "5,258 linked to summer heat."),
    24: ("SOUTH KOREA", "Seoul protests Russian air entry", "Russian attaché summoned."),
    23: ("CHINA / PAKISTAN", "China names Shenzhou-24 crew", "First Pakistani crew member."),
    31: ("FRENCH GUIANA", "Ariane 6 launches 36 satellites", "Amazon Leo reaches orbit."),
    32: ("INDONESIA", "Factory fire toll rises to 26", "Candy plant burned Nov. 21."),
}

# A large figure and its qualifier extend each visual across the desk column.
DESK_SIGNAL = {
    21: ("PIF", "HQ HIT"),
    22: ("PROBE", "POLITBURO"),
    1: ("+8.99%", "TAIEX CLOSE"),
    10: ("$175", "PER SHARE"),
    27: ("DEC.", "RETURN PLAN"),
    19: ("IRAN", "MINE CLAIM"),
    14: ("CAS", "TITLE BACK"),
    11: ("RECORD", "UKHSA EST."),
    24: ("ADIZ", "AIR ZONE"),
    23: ("PAK", "ASTRONAUT"),
    31: ("36", "IN ORBIT"),
    32: ("24 NOV", "TOLL UPDATE"),
}

WIRE = {
    7: ("02:30", "COLOMBIA", "Car bomb injures 23", "Outside Meta governor’s office"),
    4: ("21:00", "WALL STREET", "Dow closes over 50,000", "Nasdaq drops as chip stocks slide"),
    30: ("22:11", "COOK ISLANDS", "Cyclone payout announced", "$460,000 for Xavier recovery"),
    6: ("23:26", "U.S. / SPAIN", "Ábrego García leaves U.S.", "Departure reported by El País"),
}

BRIEFS = [
    [
        (5, "HAVANA", "WHO pledges $2M for Cuba vaccines"),
        (8, "BUENOS AIRES", "Brazil ends envoy’s posting"),
        (9, "SANTIAGO", "Chile mourns actor Delfina Guzmán"),
        (13, "BRUSSELS", "EU sets hybrid-car import caps"),
        (12, "GENEVA", "Gukesh and Sindarov draw opener"),
    ],
    [
        (15, "BLUE NILE", "Fighting uproots thousands"),
        (16, "SOUTH AFRICA", "Court convicts would-be recruit"),
        (17, "TIGRAY", "Amnesty urges war-crimes inquiry"),
        (20, "GAZA", "Strike kills Hamas security chief"),
        (33, "CANADA / QATAR", "Investment protection pact signed"),
    ],
    [
        (25, "BANGLADESH", "Hasina camp names Dec. 16 return"),
        (26, "HANOI", "Restaurant blast kills six"),
        (28, "SINGAPORE", "Megaspeed chip inquiry continues"),
        (29, "CANBERRA", "Online safety fines move closer"),
        (34, "SOLOMON IS.", "Move to end China pact reported"),
    ],
]

ORDER = [*LEADS, *DESK, *WIRE, *(key for column in BRIEFS for key, _, _ in column)]

DATE_NOTE = (
    "DATE CHECK",
    "24 Nov, 00:00–24:00 UTC. Nvidia’s CEO return was announced 23 Nov. Shenzhou-24 crew named 24 Nov, launch 25 Nov UTC.",
)
SOURCE_NOTE = (
    "SOURCE NOTES",
    "Lead sources are printed above. Mine strikes are an attributed claim. Full citations and UTC notes accompany the edition.",
)
