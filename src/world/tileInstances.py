from world import tile

# grass
grs = tile.Tile(4, 0, False, False, False, False)
# stone
stn = tile.Tile(5, 0, True, True, True, True)
# grass border
g_s = tile.Tile(5, 3, True, False, False, False)
gsw = tile.Tile(4, 3, True, False, True, False)
g_w = tile.Tile(4, 2, False, True, False, False)
gnw = tile.Tile(4, 1, False, False, True, True)
g_n = tile.Tile(5, 1, False, False, False, True)
gne = tile.Tile(6, 1, False, True, False, True)
g_e = tile.Tile(6, 2, False, True, False, False)
gse = tile.Tile(6, 3, True, True, False, False)


