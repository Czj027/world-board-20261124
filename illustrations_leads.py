"""Original front-page vignettes drawn on a 300 by 95 logical canvas."""

INK = "#202928"
RUST = "#b93b2f"
PETROL = "#006f5e"
SLATE = "#254f91"
OCHRE = "#8a5612"
PAPER = "#fff1d8"


def _court_figure(c, x, y, jacket, skin, scale=1):
    def points(coords):
        return [(x + a * scale, y + b * scale) for a, b in coords]

    c.polygon(points([(-8, 19), (-7, 12), (-4, 9), (3, 9), (7, 12), (9, 19)]), jacket)
    c.polygon(points([(-4, 7), (-4, 3), (-2, 1), (2, 0), (4, 2), (4, 8), (2, 10), (-2, 10)]), skin)
    c.polygon(points([(-4, 5), (-5, 2), (-3, -1), (1, -2), (4, 1), (4, 3), (-1, 2), (-3, 4)]), jacket)
    c.line(points([(-3, 11), (0, 15), (3, 11)]), "#c1a98c", .65)


def verdict(c):
    c.rect(0, 0, 300, 95, "#f0dec2")
    c.rect(147, 0, 153, 95, "#f2e9da")

    # Courtroom interior, with light from the side windows falling across the floor.
    c.polygon([(0, 0), (112, 0), (147, 25), (147, 72), (105, 62), (0, 72)], "#b5aaa1")
    c.polygon([(0, 0), (39, 10), (39, 53), (0, 65)], "#899192")
    c.polygon([(39, 10), (111, 7), (111, 54), (39, 53)], "#c5b9a8")
    c.polygon([(111, 7), (147, 24), (147, 68), (111, 54)], "#9e968b")
    for top, bottom in [((0, 3), (39, 14)), ((0, 45), (39, 42)), ((111, 9), (147, 26)), ((111, 14), (147, 30))]:
        c.line([top, bottom], "#696a66", .7)
    for left, right, top, bottom in [(6, 17, 13, 43), (22, 33, 17, 41)]:
        c.polygon([(left, bottom), (left, top + 3), (left + 3, top), (right - 2, top + 2), (right, bottom - 2)], "#ede4ce")
        c.line([(left + 5, top + 1), (left + 5, bottom - 1)], "#a69883", .8)
        c.line([(left, top + 12), (right, top + 14)], "#a69883", .7)
    for x in (45, 58, 94, 107, 121, 132, 141):
        top = 12 if x <= 107 else 15 + (x - 111) * .49
        bottom = 50 if x <= 107 else 53 + (x - 111) * .35
        c.line([(x, top), (x - .5, bottom)], "#8b8077", .8)
        c.line([(x + 2.5, top + 1), (x + 2, bottom - 2)], "#d0bfb0", .6)
    c.rect(67, 13, 17, 19, "#96887a")
    c.rect(68.2, 14.2, 14.6, 16.6, "#b8a896")
    c.polygon([(71, 27), (75, 22), (78, 22), (81, 27)], "#857568")
    c.disk(76.5, 20.2, 1.8, "#857568")
    c.polygon([(0, 64), (52, 53), (108, 52), (147, 64), (147, 95), (0, 95)], "#ac9680")
    c.polygon([(4, 77), (34, 65), (61, 62), (42, 77)], "#d0b79a")
    for x0, x1 in [(12, 63), (36, 72), (66, 82), (97, 91), (124, 101), (143, 108)]:
        c.line([(x0, 80), (x1, 55)], "#887866", .6)
    c.line([(0, 73), (45, 61), (121, 60), (147, 68)], "#c0a990", .8)

    # Judge, bench, counsel at the lectern, and the seated jury box in perspective.
    c.polygon([(69, 43), (69, 32), (72, 29), (80, 29), (83, 32), (83, 42)], "#655b51")
    _court_figure(c, 76, 31, INK, "#ab8069", .78)
    c.polygon([(51, 45), (102, 45), (107, 48), (49, 48)], "#e3c6a8")
    c.polygon([(49, 48), (107, 48), (106, 59), (50, 59)], "#725449")
    c.rect(53, 50, 49, 6, "#9f7761")
    for x in (55, 62, 69, 76, 83, 90, 97):
        c.line([(x, 51), (x - .2, 55)], "#b6957b", .55)
    c.line([(50, 58), (106, 58)], "#493f3a", 1)
    for x, y, scale, jacket, skin in [(117, 47, .63, "#4a5255", "#bd987b"),
                                      (127, 51, .68, "#303d3e", "#9b755f"),
                                      (138, 56, .75, "#4b4a4c", "#c89b7a")]:
        _court_figure(c, x, y, jacket, skin, scale)
    c.polygon([(110, 58), (145, 70), (145, 78), (111, 67)], "#6c5246")
    c.line([(109, 57.5), (146, 69.5)], "#d2b79d", 1.35)
    c.polygon([(21, 59), (32, 55), (39, 58), (39, 74), (29, 77), (21, 74)], "#5d4c43")
    c.line([(22, 59), (30, 62), (38, 58)], "#cda987", 1)
    _court_figure(c, 46, 51, "#465354", "#ae8b71", 1.13)
    c.line([(43, 65), (37, 62), (33, 63)], "#465354", 2.8)
    c.line([(50, 72), (50, 77)], "#354145", 2.3)
    c.line([(43, 72), (42, 77)], "#354145", 2.3)
    c.rect(0, 79, 147, 16, "#d8c7b3")
    c.text(10, 84, "BROOKLYN FEDERAL COURT", 8, INK, "mono")

    # Each box represents one count. The boxes encode the totals only.
    c.line([(147, 0), (147, 95)], "#9b8875", .75)
    c.rect(148, 0, 152, 47, "#a62e26")
    c.text(157, 6, "JURY VERDICT", 9, "#ffe2b4", "mono")
    c.text(156, 17, "10 / 12", 29, PAPER, "condensed")
    c.text(226, 29, "GUILTY", 14, PAPER, "condensed")
    for i in range(12):
        x = 158 + 11.1 * i
        c.rect(x, 52, 8.2, 8.2, RUST if i < 10 else "#bea991")
        if i < 10:
            c.line([(x + 1.4, 56), (x + 3.3, 58), (x + 6.6, 54)], PAPER, .95)
        else:
            c.rect(x + .8, 52.8, 6.6, 6.6, "#f2e9da")
    c.line([(157, 67), (289, 67)], "#bca892", .7)
    c.text(157, 72, "Trade secrets, fraud", 11, INK, "semibold")
    c.text(157, 83, "and sanctions violations", 11, INK, "semibold")


def _apartments(c, front, side, roof, facade, shadow, coping, windows):
    c.polygon(side, shadow)
    c.polygon(front, facade)
    c.polygon(roof, coping)
    for x, y, color in windows:
        w, h = 4.3, 5.1
        c.rect(x, y, w, h, color)
        c.line([(x + 2.1, y + .2), (x + 2.1, y + h - .2)], facade, .53)


def ukraine(c):
    c.rect(0, 0, 300, 95, "#1b3657")
    c.polygon([(0, 0), (197, 0), (197, 76), (0, 76)], "#344958")
    c.polygon([(0, 40), (25, 33), (46, 37), (61, 31), (82, 36), (108, 31),
               (139, 36), (154, 32), (178, 37), (197, 32), (197, 76), (0, 76)], "#536575")
    c.polygon([(0, 47), (33, 46), (61, 48), (88, 44), (111, 44), (133, 40),
               (153, 43), (178, 39), (197, 40), (197, 56), (0, 64)], "#637983")
    c.line([(0, 50), (36, 49), (72, 52), (95, 47), (125, 47)], "#81939a", .7)
    c.line([(112, 45), (143, 46), (162, 43), (193, 44)], "#94a0a3", .65)
    c.polygon([(0, 62), (29, 57), (87, 54), (134, 51), (197, 52), (197, 95), (0, 95)], "#354549")
    c.polygon([(0, 89), (44, 75), (79, 69), (138, 65), (197, 65), (197, 71),
               (132, 72), (84, 77), (60, 85), (37, 95), (0, 95)], "#6b7775")
    c.line([(2, 89), (44, 76), (79, 70), (136, 65), (194, 66)], "#99a09a", .65)
    c.line([(36, 93), (60, 83), (80, 77), (101, 73)], "#aaa196", .7)

    # Layered apartment facades, roofs, and the foreground street suggest a neighborhood.
    dark, lit = "#3d4d58", "#d9bb81"
    _apartments(c,
                [(109, 30), (133, 27), (133, 56), (109, 60)],
                [(133, 27), (147, 34), (146, 59), (133, 56)],
                [(109, 30), (121, 25), (138, 26), (133, 27)],
                "#839094", "#596e7a", "#9ca8a4",
                [(114, 34, lit), (123, 33, dark), (114, 44, dark), (123, 43, dark),
                 (114, 52, dark), (123, 51, "#cda575")])
    _apartments(c,
                [(73, 37), (110, 32), (111, 65), (73, 71)],
                [(110, 32), (121, 37), (121, 66), (111, 65)],
                [(73, 37), (83, 31), (111, 28), (121, 37), (110, 32)],
                "#8e9188", "#5b6864", "#abb0a1",
                [(x, y - (x - 77) * .14, lit if (x, y) in {(86, 43), (103, 52), (77, 61)} else dark)
                 for x in (77, 86, 95, 103) for y in (43, 52, 61)])
    _apartments(c,
                [(12, 43), (52, 35), (52, 74), (12, 81)],
                [(52, 35), (68, 43), (68, 75), (52, 74)],
                [(12, 43), (26, 37), (52, 33), (68, 43), (52, 35)],
                "#a1a097", "#68716d", "#bec1b2",
                [(x, y - (x - 17) * .18, lit if (x, y) in {(17, 52), (46, 61), (27, 70)} else dark)
                 for x in (17, 27, 37, 46) for y in (52, 61, 70)])
    c.line([(13, 62), (51, 54)], "#b4b4a7", .85)
    c.line([(52, 54), (67, 60)], "#929487", .85)
    c.line([(74, 57), (110, 51)], "#b2b0a0", .7)
    c.rect(142, 42, 3.5, 18, "#6f7d7c")
    c.polygon([(135, 60), (159, 53), (182, 59), (180, 74), (136, 75)], "#4d5f62")
    c.line([(128, 63), (157, 53), (183, 59)], "#97a09a", 1.1)
    c.rect(153, 63, 8, 5, "#be9d6a")
    c.rect(165, 62, 6, 4, "#33494f")
    for x, y, scale in [(8, 74, 1), (59, 74, .82), (124, 69, 1), (182, 71, .8)]:
        branch = [(x + a * scale, y + b * scale) for a, b in
                  [(0, 0), (0, -9), (-4, -14), (-1, -9), (1, -16), (0, -9), (4, -12)]]
        c.line(branch, "#293d3f", 1.05)
    c.line([(88, 70), (88, 60), (91, 58), (96, 58)], "#293a3e", .75)
    c.line([(91, 58.5), (95, 58.5)], "#e0bb83", .8)
    c.rect(0, 80, 197, 15, "#1b3657")
    c.text(9, 84, "DNIPRO RIVER • ZAPORIZHZHIA", 8, "#f3e9d9", "mono")

    c.rect(195, 0, 105, 95, "#213d69")
    c.line([(195, 0), (195, 95)], "#8093aa", .85)
    c.text(204, 8, "OVERNIGHT STRIKE", 8, "#dceaff", "mono")
    c.text(204, 23, "2", 25, "#ffd480", "condensed")
    c.text(228, 31, "KILLED", 12, PAPER, "condensed")
    c.line([(204, 53), (289, 53)], "#7287a6", .7)
    c.text(204, 60, "40+", 25, "#ffd480", "condensed")
    c.text(244, 69, "WOUNDED", 12, PAPER, "condensed")


def oil(c):
    c.rect(0, 0, 300, 95, "#f5e3bc")
    c.rect(146, 0, 154, 95, "#efe4ce")

    def map_point(lon, lat):
        return 12 + (lon - 38.6) * 10.25, 8 + (37.35 - lat) * 9.05

    # Schematic national outline and Tigris, with the two cities geographically placed.
    border = [(42.36, 37.10), (43.08, 37.28), (43.73, 37.16), (44.05, 37.32),
              (44.79, 37.15), (44.79, 36.80), (44.26, 36.38), (45.05, 35.92),
              (45.52, 35.82), (46.25, 35.30), (46.12, 35.06), (45.48, 34.42),
              (45.68, 34.08), (46.11, 33.80), (46.46, 33.33), (47.25, 32.51),
              (47.80, 31.74), (47.70, 31.00), (48.59, 29.94), (48.13, 29.98),
              (47.67, 30.10), (47.12, 30.09), (46.50, 29.12), (44.71, 29.18),
              (42.95, 30.77), (39.50, 32.15), (38.80, 33.37), (39.20, 34.51),
              (40.99, 34.53), (41.31, 36.37)]
    silhouette = [map_point(lon, lat) for lon, lat in border]
    c.polygon(silhouette, "#d8c8a6")
    c.line([*silhouette, silhouette[0]], "#958263", .9)
    tigris = [(42.36, 37.10), (42.56, 36.98), (42.76, 36.73), (43.11, 36.34),
              (43.24, 35.98), (43.40, 35.57), (43.65, 35.22), (43.62, 34.91),
              (43.73, 34.58), (43.68, 34.31), (43.97, 34.06), (44.23, 33.79),
              (44.19, 33.56), (44.37, 33.32), (45.00, 32.81), (45.81, 32.48),
              (46.29, 32.28), (46.82, 31.92), (47.02, 31.52), (47.25, 31.17),
              (47.47, 30.98)]
    c.line([map_point(lon, lat) for lon, lat in tigris], "#6c9190", 1.4)
    c.line([map_point(lon, lat) for lon, lat in [(40.99, 34.53), (41.88, 34.37),
            (42.40, 34.05), (42.81, 34.14), (43.18, 33.72), (43.68, 33.43),
            (43.76, 33.17), (44.32, 32.81), (44.55, 32.14), (45.19, 31.54),
            (45.79, 31.13), (46.67, 30.92), (47.47, 30.98)]], "#8faaa1", .95)
    c.text(33, 39, "IRAQ", 11, OCHRE, "condensed")
    erbil_x, erbil_y = map_point(44.01, 36.19)
    baghdad_x, baghdad_y = map_point(44.37, 33.32)
    for x, y, label, color, label_y in [(erbil_x, erbil_y, "ERBIL", PETROL, 15),
                                       (baghdad_x, baghdad_y, "BAGHDAD", RUST, 44)]:
        c.disk(x, y, 3.3, PAPER, color)
        c.disk(x, y, 1.45, color)
        c.line([(x + 3, y), (92, y), (97, label_y + 4)], color, .8)
        c.text(100, label_y, label, 9, color, "condensed")
    c.text(12, 84, "TIGRIS", 8, PETROL, "mono")
    c.line([(46, 87), (68, 87), (102, 72)], "#6c9190", .65)

    # The landscape is a separate vignette, with the order and response beneath it.
    c.line([(146, 0), (146, 95)], "#a69477", .7)
    c.polygon([(147, 48), (178, 43), (195, 30), (209, 35), (226, 21), (247, 13),
               (267, 29), (280, 25), (300, 42), (300, 62), (147, 62)], "#c2aa78")
    c.polygon([(147, 56), (169, 53), (194, 48), (210, 43), (223, 47),
               (249, 37), (270, 42), (288, 39), (300, 44), (300, 62), (147, 62)], "#ac936a")
    c.line([(178, 47), (197, 36), (208, 38), (227, 24), (243, 19)], "#e2ce9e", .75)
    c.line([(251, 18), (267, 31), (281, 29), (298, 42)], "#e2ce9e", .75)
    c.line([(151, 57), (172, 56), (193, 52), (211, 49), (225, 52), (245, 46),
            (257, 47), (276, 45), (297, 48)], "#d4bc88", .8)
    c.line([(162, 59), (192, 57), (221, 58), (257, 52), (298, 55)], "#745f45", .65)
    c.text(155, 9, "OILFIELDS UNDER", 8, INK, "mono")
    c.text(155, 20, "KURDISH SECURITY", 8, PETROL, "mono")
    c.text(155, 31, "CONTROL", 8, PETROL, "mono")

    c.line([(221, 56), (291, 56)], "#5f5443", 1.1)
    c.polygon([(254, 54), (260, 33), (263, 33), (268, 54)], "#584c40")
    c.polygon([(257.5, 52), (261.3, 38), (265.1, 52)], "#bba176")
    c.line([(258.5, 48), (264.5, 48)], "#716049", .8)
    c.line([(258, 51), (264, 45)], "#716049", .7)
    c.polygon([(246, 36), (244, 34), (275, 27), (278, 30), (262, 34)], INK)
    c.polygon([(275, 27), (280, 27), (283, 30), (283, 36), (281, 38), (277, 33)], INK)
    c.line([(282, 35), (282, 55)], "#5e5042", .85)
    c.line([(247, 35), (244, 48)], "#5e5042", 1.2)
    c.disk(244, 48.8, 3.1, "#5e5042")
    c.rect(228, 49, 11, 6.5, "#8a6f54")
    c.polygon([(228, 49), (231, 47), (237, 47), (239, 49)], "#bda580")

    c.rect(146, 62, 154, 16, "#a7322b")
    c.rect(146, 78, 154, 17, "#076a5d")
    c.line([(156, 72), (169, 72), (166, 69)], PAPER, 1)
    c.line([(169, 72), (166, 75)], PAPER, 1)
    c.line([(169, 87), (156, 87), (159, 84)], PAPER, 1)
    c.line([(156, 87), (159, 90)], PAPER, 1)
    c.text(175, 65, "Federal order issued", 11, PAPER, "semibold")
    c.text(175, 80, "Kurdish leaders reject", 11, PAPER, "semibold")


LEAD_ART = {"verdict": verdict, "ukraine": ukraine, "oil": oil}
