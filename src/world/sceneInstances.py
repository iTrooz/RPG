from world.scene import Scene
forest = Scene(0) # warning non utile, PARCE QUE PYTHON FAIT *
rocky_land = Scene(1)


from world.tileInstances import *

forest.map = [
	[grs, gt_, gnw, g_n, g_n, g_n, g_n, gne, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, gsw, grs, grs, grs, grs, g_e, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, stn, gsw, grs, grs, g_s, gse, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, stn, g_w, g_e, stn, stn, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, stn, stn, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, stn, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, stn, stn, stn, stn, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
	[grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs, grs],
]

forest.map_height = len(forest.map)
forest.map_width = len(forest.map[0])

rocky_land.map = [
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, grs, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, grs, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, grs, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, grs, grs, stn, stn, stn, stn, stn, stn, stn, stn, grs, grs, stn, stn, stn, ],
	[stn, grs, grs, stn, stn, stn, stn, stn, stn, stn, grs, grs, grs, grs, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, grs, grs, grs, grs, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, grs, grs, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
	[stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, stn, ],
]
rocky_land.map_height = len(rocky_land.map)
rocky_land.map_width = len(rocky_land.map[0])

scenes = [forest, rocky_land]