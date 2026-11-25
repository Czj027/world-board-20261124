"""Six hand-drawn desk illustrations in the front page's 150 × 50 units."""

INK = "#202928"
RUST = "#b93b2f"
PETROL = "#006f5e"
SLATE = "#254f91"
OCHRE = "#8a5612"
PAPER = "#fff5e4"


def riyadh(c):
    c.rect(0, 0, 150, 50, "#f4debc")
    c.disk(49, 27, 19, "#e4c8a8")
    c.line([(5, 21), (20, 21)], "#c3a881", 1)
    c.line([(61, 16), (83, 16)], "#c3a881", 1)
    c.polygon([(0, 39), (8, 39), (8, 30), (15, 27), (21, 30), (21, 39),
               (26, 39), (26, 24), (35, 20), (39, 24), (39, 44), (0, 44)], "#7c7765")
    c.polygon([(54, 44), (54, 32), (63, 27), (67, 29), (67, 35), (72, 35),
               (72, 23), (77, 20), (85, 25), (85, 44)], "#827865")
    c.line([(12, 32), (12, 38)], "#bea887", 1)
    c.line([(76, 26), (76, 39)], "#c6af8d", 1)
    # The faceted crown and taper distinguish the PIF tower in the district skyline.
    c.polygon([(34, 44), (36, 20), (43, 9), (51, 5), (56, 12), (60, 44)], INK)
    c.polygon([(42, 15), (51, 7), (50, 31), (44, 44), (36, 44)], "#666457")
    c.polygon([(52, 9), (55, 14), (58, 44), (51, 44), (49, 25)], "#a69b80")
    c.line([(38, 24), (49, 16), (55, 18)], "#d0bb95", 0.8)
    c.line([(37, 32), (49, 24), (56, 26)], "#c7b594", 0.8)
    c.line([(36, 40), (48, 32), (57, 34)], "#c7b594", 0.8)
    c.rect(0, 44, 85, 6, INK)
    c.text(5, 5, "PIF TOWER", size=7, fill=INK, face="condensed")
    c.line([(5, 14), (28, 14), (35, 19)], OCHRE, 0.8)
    c.rect(86, 0, 64, 50, "#fbe0ce")
    c.rect(86, 0, 2, 50, RUST)
    c.text(93, 5, "11", size=29, fill=RUST, face="condensed")
    c.text(117, 19, "INJURED", size=8.5, fill=INK, face="condensed")
    c.line([(93, 32), (144, 32)], "#c7ab9c", 0.8)
    c.text(93, 35, "SAUDI OFFICIALS", size=8, fill=INK, face="condensed")
    c.text(93, 43, "BLAME HOUTHIS", size=7.5, fill=RUST, face="condensed")


def shanghai(c):
    c.rect(0, 0, 150, 50, "#dbeaf8")
    c.disk(38, 23, 19, "#bad2eb")
    c.polygon([(0, 42), (0, 35), (7, 35), (7, 29), (11, 29), (11, 37),
               (21, 37), (21, 34), (29, 34), (29, 31), (39, 31), (39, 34),
               (47, 34), (47, 28), (59, 28), (59, 36), (67, 36), (67, 31),
               (78, 33), (78, 42)], "#8497aa")
    # Oriental Pearl, World Financial Center, and the twisting Shanghai Tower.
    c.line([(18, 8), (18, 41)], SLATE, 2)
    c.disk(18, 19, 3.5, RUST)
    c.disk(18, 29, 5.4, SLATE)
    c.line([(15, 32), (11, 41)], SLATE, 1.3)
    c.line([(21, 32), (25, 41)], SLATE, 1.3)
    c.polygon([(27, 41), (29, 13), (44, 13), (46, 41)], SLATE)
    c.polygon([(32, 16), (41, 16), (40, 21), (33, 21)], "#d3dfe5")
    c.line([(32, 25), (31, 39)], "#afc0ce", 0.8)
    c.line([(41, 25), (42, 39)], "#afc0ce", 0.8)
    c.polygon([(47, 41), (47, 26), (49, 13), (53, 6), (58, 5), (62, 9),
               (63, 22), (66, 41)], "#31475a")
    c.polygon([(53, 8), (58, 7), (57, 16), (55, 26), (56, 41), (49, 41),
               (50, 21)], "#7b95a9")
    c.line([(50, 18), (57, 16), (61, 13)], "#c5d4db", 0.8)
    c.line([(50, 26), (57, 23), (62, 19)], "#a9bfcc", 0.8)
    c.line([(49, 34), (58, 31), (64, 27)], "#a9bfcc", 0.8)
    c.rect(0, 41, 77, 9, "#b9cace")
    c.line([(4, 45), (30, 45)], "#728d97", 0.9)
    c.line([(35, 47), (61, 47)], "#728d97", 0.9)
    c.polygon([(79, 4), (140, 4), (145, 9), (145, 46), (79, 46)], "#aab7c3")
    c.polygon([(75, 2), (134, 2), (142, 10), (142, 43), (75, 43)], PAPER)
    c.polygon([(134, 2), (134, 10), (142, 10)], "#c6d0d6")
    c.rect(81, 8, 43, 10, RUST)
    c.text(84, 9.5, "INVESTIGATION", size=7.2, fill=PAPER, face="condensed")
    c.text(81, 21, "CHEN JINING", size=12.4, fill=INK, face="condensed")
    c.line([(81, 33), (136, 33)], "#b8b6aa", 0.7)
    c.text(81, 36, "SHANGHAI PARTY CHIEF", size=6.7, fill=SLATE, face="condensed")


def chips(c):
    c.rect(0, 0, 150, 50, "#d1ebdb")
    c.rect(0, 0, 43, 50, "#b9dfcd")
    c.line([(0, 9), (11, 9), (15, 13)], "#76a199", 1)
    c.line([(28, 38), (34, 44), (43, 44)], "#76a199", 1)
    c.line([(30, 11), (35, 6), (42, 6)], "#76a199", 1)
    c.line([(0, 43), (7, 43), (13, 37)], "#76a199", 1)
    c.rect(10, 13, 23, 24, INK)
    c.rect(13, 16, 17, 18, PETROL)
    c.rect(17, 20, 9, 10, "#c7d8ac")
    c.rect(19, 22, 5, 6, "#729a71")
    for x in (13, 18, 24, 29):
        c.line([(x, 10), (x, 13)], PETROL, 1.3)
        c.line([(x, 37), (x, 40)], PETROL, 1.3)
    for y in (16, 22, 28, 34):
        c.line([(7, y), (10, y)], PETROL, 1.3)
        c.line([(33, y), (36, y)], PETROL, 1.3)
    c.text(48, 4, "CLOSING GAINS", size=8.8, fill=INK, face="condensed")
    c.line([(48, 14), (145, 14)], "#acbfb3", 0.8)
    c.line([(76, 17), (76, 45)], "#768f82", 0.8)
    # Both bars use the same scale, starting from zero.
    units_per_point = 4.85
    for y, label, gain, color in ((18, "TAIEX", 8.99, PETROL), (34, "KOSPI", 6.32, SLATE)):
        c.text(48, y + 1, label, size=8.5, fill=INK, face="condensed")
        c.rect(76, y, gain * units_per_point, 8, color)
        c.text(145, y + 1, f"+{gain:.2f}%", size=8.1, fill=color, face="condensed", anchor="rt")


def insmed(c):
    c.rect(0, 0, 150, 50, "#fcdfbe")
    c.polygon([(8, 12), (54, 3), (62, 39), (16, 47)], "#c6ad8b")
    c.polygon([(5, 8), (55, 5), (58, 42), (8, 45)], "#f4ebdc")
    c.polygon([(12, 7), (65, 7), (71, 13), (71, 44), (12, 44)], "#faf4e7")
    c.polygon([(65, 7), (65, 13), (71, 13)], "#d9c7ad")
    c.text(16, 12, "SANOFI", size=9.4, fill=INK, face="condensed")
    c.line([(17, 23), (41, 23)], "#aa987d", 0.8)
    c.text(16, 27, "INSMED", size=9.4, fill=INK, face="condensed")
    c.line([(17, 39), (34, 39)], "#aa987d", 0.8)
    # A lung research motif sits on the proposed acquisition papers.
    c.polygon([(53, 19), (49, 21), (45, 29), (45, 36), (49, 39), (54, 36),
               (55, 27), (55, 21)], "#bc7d70")
    c.polygon([(61, 19), (64, 21), (68, 29), (68, 36), (64, 39), (60, 36),
               (59, 27), (59, 21)], "#bc7d70")
    c.line([(57, 16), (57, 25), (52, 30), (50, 33)], RUST, 1.4)
    c.line([(57, 25), (62, 30), (64, 33)], RUST, 1.4)
    c.rect(76, 0, 74, 50, "#dde8db")
    c.rect(76, 0, 2, 50, PETROL)
    c.text(83, 3, "$41B", size=26, fill=PETROL, face="condensed")
    c.text(84, 27, "ALL-CASH BID", size=8.4, fill=INK, face="condensed")
    c.line([(84, 35), (144, 35)], "#9fb5a7", 0.8)
    c.text(84, 38, "$175 / SHARE", size=9.3, fill=PETROL, face="condensed")


def malaysia(c):
    c.rect(0, 0, 150, 50, "#d9ecdf")
    mainland = "#d3c4a4"
    # North-up locator from the Bay of Bengal to northern Borneo.
    c.polygon([(8, 0), (77, 0), (72, 7), (69, 12), (64, 16), (62, 21), (56, 25),
               (50, 25), (44, 22), (39, 23), (36, 27), (38, 32), (43, 36),
               (46, 41), (44, 45), (41, 42), (37, 39), (33, 33), (30, 27),
               (25, 24), (23, 20), (19, 20), (16, 15), (13, 12), (17, 8),
               (14, 6), (7, 5)], mainland)
    c.polygon([(30, 2), (34, 4), (34, 9), (39, 11), (37, 15), (39, 19),
               (35, 19), (34, 23), (34, 29), (36, 33), (33, 32), (30, 27),
               (29, 22), (25, 24), (23, 20), (19, 20), (16, 15), (20, 12),
               (23, 6), (27, 5)], OCHRE)
    c.polygon([(34, 36), (39, 35), (43, 36), (46, 41), (44, 45), (41, 42),
               (37, 39)], PETROL)
    c.polygon([(23, 34), (28, 35), (31, 39), (38, 43), (42, 49), (36, 49),
               (31, 46), (27, 40), (23, 38)], mainland)
    c.polygon([(61, 46), (65, 42), (70, 40), (74, 39), (78, 35), (82, 34),
               (86, 39), (83, 44), (80, 49), (65, 49)], mainland)
    c.polygon([(64, 44), (68, 41), (74, 39), (78, 35), (82, 34), (86, 39),
               (81, 40), (78, 39), (73, 44), (68, 43)], PETROL)
    for segment in ([(33, 39), (29, 36)], [(24, 33), (21, 30)], [(19, 27), (19, 24)]):
        c.line(segment, RUST, 1.3)
    c.polygon([(16, 25), (18, 19), (22, 24)], RUST)
    c.line([(35, 12), (45, 12)], OCHRE, 0.8)
    c.text(47, 8, "MYANMAR", size=8.3, fill=OCHRE, face="condensed")
    c.line([(43, 38), (49, 32), (54, 32)], PETROL, 0.8)
    c.text(54, 28, "MALAYSIA", size=8.3, fill=PETROL, face="condensed")
    c.rect(91, 0, 59, 50, "#eee3d0")
    c.rect(91, 0, 2, 50, OCHRE)
    c.text(98, 3, "6,803", size=23, fill=OCHRE, face="condensed")
    c.text(98, 24, "MYANMAR NATIONALS", size=6.2, fill=INK, face="condensed")
    c.rect(98, 35, 47, 10, OCHRE)
    c.text(101, 36.5, "DEC. RETURN PLAN", size=6.25, fill=PAPER, face="condensed")


def hormuz(c):
    c.rect(0, 0, 150, 50, "#c7e9ed")
    coast = "#cbb994"
    # An approximate north-up shoreline and the Musandam peninsula.
    c.polygon([(0, 0), (95, 0), (95, 30), (87, 30), (82, 28), (73, 28),
               (67, 25), (63, 22), (61, 17), (58, 13), (53, 12), (47, 9),
               (40, 8), (34, 10), (27, 14), (19, 16), (13, 19), (6, 19),
               (0, 21)], coast)
    c.polygon([(0, 49), (0, 46), (8, 44), (15, 44), (21, 41), (29, 41),
               (36, 38), (41, 34), (42, 27), (46, 26), (47, 23), (51, 22),
               (51, 26), (55, 26), (52, 29), (53, 34), (56, 38), (57, 43),
               (62, 49)], coast)
    c.polygon([(32, 16), (38, 12), (45, 12), (51, 14), (49, 17),
               (41, 18), (36, 17)], "#a8956d")
    c.line([(37, 39), (43, 41), (56, 41)], "#a29073", 0.7)
    c.text(8, 5, "IRAN", size=9.5, fill=INK, face="condensed")
    c.text(9, 41.5, "UAE", size=8, fill=INK, face="condensed")
    c.text(42, 42, "OMAN", size=7.5, fill=INK, face="condensed")
    c.text(65, 7, "STRAIT OF", size=7.8, fill=PETROL, face="condensed")
    c.text(65, 15, "HORMUZ", size=9.6, fill=PETROL, face="condensed")
    c.line([(64, 20), (58, 20), (54, 22)], PETROL, 0.9)
    c.line([(5, 27), (20, 27)], "#a4c3be", 0.85)
    c.line([(11, 32), (27, 32)], "#a4c3be", 0.85)
    c.line([(66, 35), (91, 35)], "#a4c3be", 0.85)
    c.line([(74, 41), (91, 41)], "#a4c3be", 0.85)
    c.rect(95, 0, 55, 50, "#f0e4d9")
    c.rect(95, 0, 2, 50, RUST)
    c.polygon([(101, 16), (145, 16), (140, 21), (107, 21)], PETROL)
    c.rect(109, 10, 7, 6, PETROL)
    c.rect(110, 8, 3, 2, PETROL)
    c.line([(117, 13), (138, 13)], PETROL, 1)
    for x in (119, 126, 133):
        c.rect(x, 12, 4, 2, PETROL)
    c.line([(103, 24), (142, 24)], "#b9ac9e", 0.8)
    c.text(101, 28, "IRAN'S MINE CLAIM", size=6.4, fill=INK, face="condensed")
    c.text(101, 38, "UNVERIFIED", size=10.3, fill=RUST, face="condensed")


DESK_ART_A = {21: riyadh, 22: shanghai, 1: chips, 10: insmed, 27: malaysia, 19: hormuz}
