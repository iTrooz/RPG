from world import tile
from world import sceneInstances


# stone
stn = tile.Tile(7, 0, True, True, True, True)
# grass
grs = tile.Tile(6, 0, False, False, False, False)
# grass border
g_s = tile.Tile(3, 0, True , False, False, False)
gsw = tile.Tile(2, 3, True , True , False, False)
g_w = tile.Tile(2, 1, False, True , False, False)
gnw = tile.Tile(2, 2, False, True , False, True )
g_n = tile.Tile(2, 0, False, False, False, True )
gne = tile.Tile(3, 2, False, False, True , True )
g_e = tile.Tile(3, 1, False, False, True , False)
gse = tile.Tile(3, 3, True , False, True , False)

ch1 = tile.Tile(8, 1, True, True, True, True)
ch1.content = {}

ch2 = ch1.copy()

# grass hidden teleporter
gt_ = grs.copy()
gt_.teleport = {"x":5, "y":5,"scene": sceneInstances.rocky_land}