"""Headline ordering, summaries and print references for the UTC edition."""

LEADS = {
    3: (
        "NORTH AMERICA  /  JUSTICE",
        "US jury convicts Huawei",
        "A Brooklyn jury convicted the Chinese telecom group on 10 of 12 counts, including trade-secret conspiracy, fraud and Iran sanctions violations.",
        "U.S. JUSTICE DEPARTMENT  /  REUTERS",
        "verdict",
    ),
    2: (
        "EUROPE  /  WAR IN UKRAINE",
        "Russian strike kills two in Zaporizhzhia",
        "An overnight strike hit residential buildings. Ukrainian officials reported two dead and more than 40 injured.",
        "AP  /  AL JAZEERA",
        "ukraine",
    ),
    18: (
        "MIDDLE EAST  /  ENERGY",
        "Baghdad orders oilfield takeover",
        "Iraq directed its federal oil ministry to manage fields under Kurdish security control. Kurdish leaders rejected the order.",
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
    21: ("SAUDI ARABIA", "11 hurt as Riyadh tower hit", "Saudi officials blame Houthis.", "11"),
    22: ("CHINA", "China probes Shanghai chief", "Chen Jining is a Politburo member.", "CC"),
    1: ("TAIWAN / SOUTH KOREA", "Asian chip shares rebound", "TAIEX +8.99% and Kospi +6.32%.", "+"),
    10: ("FRANCE / UNITED STATES", "Sanofi agrees $41B takeover", "The bid offers $175 per Insmed share.", "$"),
    27: ("MALAYSIA", "Malaysia to send 6,803 back", "Myanmar nationals due back in Dec.", "6.8K"),
    19: ("STRAIT OF HORMUZ", "Iran says tankers hit mines", "Mine claim remains unverified.", "?"),
    14: ("SENEGAL", "Senegal regains Africa Cup title", "Sports court restores win vs Morocco.", "1–0"),
    11: ("ENGLAND", "Heat deaths hit record estimate", "Health agency estimates 5,258 deaths.", "°"),
    24: ("SOUTH KOREA", "Seoul protests Russian air entry", "Moscow’s military attaché summoned.", "RU"),
    23: ("CHINA / PAKISTAN", "China names Shenzhou-24 crew", "Pakistani astronaut to fly to Tiangong.", "24"),
    31: ("FRENCH GUIANA", "Ariane 6 launches 36 satellites", "Amazon Leo payload reaches orbit.", "36"),
    32: ("INDONESIA", "Factory fire toll rises to 26", "New toll from Nov. 21 candy plant fire.", "26"),
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
    "Headlines credit original reporting and public records. Mine strikes are an attributed claim. Full source and time notes are in the public edition.",
)
