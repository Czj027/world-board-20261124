"""Editorial drawings on the 150 by 50 logical desk canvas."""

from math import cos, pi, sin


INK = "#202928"
RUST = "#b93b2f"
PETROL = "#006f5e"
SLATE = "#254f91"
OCHRE = "#8a5612"
PAPER = "#fff5e4"
RULE = "#c4b6a2"


def senegal_ruling(c):
    c.rect(0, 0, 150, 50, "#f5e6cf")
    c.rect(0, 0, 100, 50, "#c8e7ce")
    for x in range(0, 100, 20):
        c.rect(x, 0, 10, 50, "#d9eed7")
    field_lines = "#769486"
    c.line([(4, 4), (96, 4), (96, 46), (4, 46), (4, 4)], field_lines, 0.7)
    c.line([(50, 4), (50, 46)], field_lines, 0.7)
    c.disk(50, 25, 15, "#c8e7ce", field_lines)
    c.line([(4, 13), (13, 13), (13, 37), (4, 37)], field_lines, 0.7)
    c.line([(96, 13), (87, 13), (87, 37), (96, 37)], field_lines, 0.7)

    c.rect(10, 10, 80, 30, "#263a33")
    c.rect(10, 40, 80, 1.5, "#5b7566")
    for x, color in zip((14, 19, 24), ("#398369", "#e4bd5a", "#b95048")):
        c.rect(x, 16, 5, 9, color)
    c.polygon([(21.5, 18.5), (22, 20), (23.6, 20), (22.3, 20.9), (22.8, 22.5),
               (21.5, 21.6), (20.2, 22.5), (20.7, 20.9), (19.4, 20), (21, 20)], "#286e54")
    c.rect(71, 16, 15, 9, "#b95048")
    c.polygon([(78.5, 18), (79.1, 20), (81.2, 20), (79.5, 21.2), (80.1, 23.1),
               (78.5, 22), (76.9, 23.1), (77.5, 21.2), (75.8, 20), (77.9, 20)], "#345946")
    c.text(11.8, 28, "SEN", size=9.4, fill=PAPER)
    c.text(70.2, 28, "MAR", size=9.4, fill=PAPER)
    c.text(50, 17, "1–0", size=22, fill=PAPER, face="condensed", anchor="mt")

    c.polygon([(111, 4), (136, 4), (143, 11), (143, 35), (111, 35)], PAPER)
    c.line([(111, 35), (111, 4), (136, 4), (143, 11), (143, 35), (111, 35)], RULE, 0.7)
    c.polygon([(136, 4), (136, 11), (143, 11)], "#d7c6ad")
    c.text(127, 12, "CAS", size=15, fill=RUST, face="condensed", anchor="mt")
    c.line([(118, 28), (136, 28)], RULE, 0.9)
    c.line([(118, 31), (131, 31)], RULE, 0.9)
    c.line([(113, 25), (99, 25)], RUST, 1.6)
    c.polygon([(98, 25), (104, 21.5), (104, 28.5)], RUST)
    c.text(126, 38.5, "RESTORED", size=10.4, fill=RUST, face="condensed", anchor="mt")


def england_heat(c):
    c.rect(0, 0, 150, 50, "#f9e1bc")
    c.rect(91, 0, 59, 50, "#eee0cc")
    c.text(7, 6, "SUMMER 2026", size=11, fill=INK, face="condensed")
    start, span = 10, 73
    for tick in range(4):
        x = start + span * tick / 3
        c.line([(x, 20), (x, 37)], "#cbb491", 0.8)
    c.rect(start, 23, span * 5258 / 6000, 10, RUST)
    c.line([(start, 35), (start + span, 35)], OCHRE, 0.8)
    c.text(start, 38, "0", size=8.5, fill=OCHRE, anchor="mt")
    c.text(start + span, 38, "6k", size=8.5, fill=OCHRE, anchor="mt")
    c.text(96, 5, "5,258", size=24, fill=RUST, face="condensed")
    c.text(96, 29, "EST. DEATHS", size=10.2, fill=INK, face="condensed")
    c.text(96, 41, "UKHSA RECORD", size=8.3, fill=OCHRE, face="condensed")


def seoul_summons(c):
    c.rect(0, 0, 150, 50, "#d9e8f7")
    c.rect(0, 0, 62, 50, "#c7e6e3")
    for radius in (9, 16, 23):
        ring = [(31 + radius * cos(step * pi / 20), 26 + radius * sin(step * pi / 20))
                for step in range(41)]
        c.line(ring, "#9fb6ad", 0.7)
    c.line([(31, 5), (31, 48)], "#a4b9af", 0.7)
    c.line([(8, 26), (54, 26)], "#a4b9af", 0.7)
    c.disk(31, 26, 1.4, PETROL)
    c.rect(4, 5, 30, 11, "#c7e6e3")
    c.text(6, 6, "ADIZ", size=10.3, fill=PETROL)
    c.polygon([(47, 11), (48, 12), (46.5, 18.5), (54, 27), (53, 29), (44, 25),
               (42, 30), (44.2, 33.3), (43.4, 35), (39.5, 32.7), (35, 33),
               (35.4, 31), (38, 29), (39, 23.5), (29, 23), (29.4, 21),
               (41, 18.3), (45, 12)], SLATE)
    c.line([(63, 0), (63, 50)], "#a9b1b8", 0.9)
    c.text(70, 6, "SEOUL · NOV 24", size=8.6, fill=SLATE)
    c.text(70, 19, "RUSSIAN ATTACHÉ", size=11.4, fill=INK, face="condensed")
    c.text(70, 32, "SUMMONED", size=16, fill=SLATE, face="condensed")


def _crew_member(c, x, suit, panel):
    c.polygon([(x - 9, 36), (x - 8, 30), (x - 5, 28), (x + 5, 28),
               (x + 8, 30), (x + 9, 36)], suit)
    c.disk(x, 24, 6.2, PAPER, suit)
    c.polygon([(x - 4.3, 23), (x + 4.3, 23), (x + 4.4, 26), (x + 2.7, 27.7),
               (x - 2.7, 27.7), (x - 4.4, 26)], suit)
    c.line([(x - 4, 32.5), (x + 4, 32.5)], panel, 0.8)


def shenzhou_crew(c):
    c.rect(0, 0, 150, 50, "#dce6ed")
    c.rect(0, 0, 86, 50, "#e2edf5")
    c.text(6, 5, "CREW NAMED", size=11.2, fill=INK, face="condensed")
    for x, country, suit, panel in (
        (16, "CHN", SLATE, "#dedfdc"),
        (42, "CHN", SLATE, "#dedfdc"),
        (68, "PAK", PETROL, "#cedfd5"),
    ):
        c.rect(x - 11, 17, 22, 20, panel)
        _crew_member(c, x, suit, panel)
        c.text(x, 40, country, size=9.5, fill=suit, anchor="mt")
    c.line([(86, 0), (86, 50)], "#b8b6aa", 0.8)

    c.text(118, 5, "TIANGONG", size=11.2, fill=SLATE, face="condensed", anchor="mt")
    c.line([(93, 23), (143, 23)], SLATE, 1.1)
    for x in (93, 127):
        c.rect(x, 18, 16, 10, SLATE)
        for offset in (4, 8, 12):
            c.line([(x + offset, 18), (x + offset, 28)], "#adb8c6", 0.7)
        c.line([(x, 23), (x + 16, 23)], "#adb8c6", 0.7)
    c.polygon([(110, 20), (125, 20), (127, 23), (125, 26), (110, 26), (108, 23)], "#556365")
    c.rect(115, 16, 6, 14, SLATE)
    c.rect(113, 20, 10, 6, "#f3eee3")
    c.line([(118, 20), (118, 26)], SLATE, 0.8)
    c.text(118, 32, "MUHAMMAD", size=8.8, fill=PETROL, face="condensed", anchor="mt")
    c.text(118, 41, "ZEESHAN ALI", size=9.3, fill=PETROL, face="condensed", anchor="mt")


def ariane_deployment(c):
    c.rect(0, 0, 150, 50, "#d9ecf3")
    c.rect(0, 0, 59, 50, "#c6daef")
    c.text(5, 5, "ARIANE 6", size=10.5, fill=SLATE, face="condensed")
    c.line([(37, 40), (46, 40), (46, 16)], "#6b7a86", 1.1)
    c.line([(39, 32), (46, 32), (42, 26), (46, 21)], "#90a0ae", 0.8)
    c.polygon([(25, 34), (28, 20), (32, 14), (36, 20), (39, 34)], SLATE)
    c.polygon([(28, 34), (29, 23), (32, 16.8), (35, 23), (36, 34)], PAPER)
    c.rect(28, 34, 8, 2, SLATE)
    c.polygon([(29, 36), (35, 36), (32, 42)], RUST)
    c.line([(7, 38), (18, 38)], "#a0aeb9", 1)
    c.text(5, 41, "KOUROU", size=8.7, fill=INK, face="condensed")
    c.line([(49, 27), (63, 27)], SLATE, 1.2)
    c.polygon([(65, 27), (59, 23.5), (59, 30.5)], SLATE)

    # One glyph per satellite in the confirmed payload.
    for row in range(6):
        for column in range(6):
            x, y = 72 + 6.6 * column, 8 + 6.8 * row
            c.line([(x - 2.2, y), (x + 2.2, y)], SLATE, 1.25)
            c.rect(x - 0.85, y - 1.35, 1.7, 2.7, PETROL)
    c.line([(111, 6), (111, 44)], "#a6afbb", 0.8)
    c.text(129.5, 4, "36", size=24, fill=SLATE, face="condensed", anchor="mt")
    c.text(129.5, 29, "LEO", size=11, fill=INK, face="condensed", anchor="mt")
    c.text(129.5, 41, "DEPLOYED", size=9, fill=PETROL, face="condensed", anchor="mt")


def cikande_factory(c):
    c.rect(0, 0, 150, 50, "#f9dfc5")
    c.text(6, 5, "NOV 21 · FIRE", size=10, fill=RUST, face="condensed")
    c.polygon([(64, 26), (60, 21), (61, 17), (57, 14), (62, 10), (69, 11),
               (68, 7), (75, 6), (81, 10), (81, 16), (75, 17), (72, 22), (73, 27)],
              "#c5b3a4")
    c.polygon([(64, 24), (65, 20), (63, 16), (67, 14), (71, 16), (69, 19),
               (71, 23), (70, 27)], "#a98d7d")
    c.polygon([(8, 38), (8, 28), (23, 21), (23, 28), (38, 21), (38, 28),
               (53, 21), (53, 28), (64, 28), (64, 23), (71, 23), (72, 38)],
              "#655750")
    for x in (14, 25, 36, 47, 58):
        c.rect(x, 31, 6, 3, "#d9c1ad")
    c.line([(6, 38), (78, 38)], RUST, 0.8)
    c.text(6, 41, "CIKANDE", size=9.2, fill=INK, face="condensed")

    c.rect(86, 4, 60, 42, "#f4e9de")
    c.line([(86, 4), (146, 4)], RUST, 1.2)
    c.line([(86, 46), (146, 46)], "#c7b1a4", 0.9)
    c.text(91, 9, "NOV 24 · TOLL", size=9.8, fill=RUST, face="condensed")
    c.text(91, 21, "26", size=26, fill=RUST, face="condensed")
    c.text(119, 33, "DEAD", size=10, fill=INK, face="condensed")


DESK_ART_B = {
    11: england_heat,
    14: senegal_ruling,
    23: shenzhou_crew,
    24: seoul_summons,
    31: ariane_deployment,
    32: cikande_factory,
}
