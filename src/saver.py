import utils
import json

def save(fname="../saves/save.json"):
	f = open(fname, "w")
	saveobj = {}
	saveobj["ticks"] = utils.ticks
	saveobj["scene"] = utils.actual_scene.id
	saveobj["player"] = {}
	saveobj["player"]["x"] = utils.player.x
	saveobj["player"]["y"] = utils.player.y
	f.write(json.dumps(saveobj))



def restore(fname="../saves/save.json"):

	f = open(fname, "r")
	saveobj = json.loads(f.read())
	utils.ticks = saveobj["ticks"]
	utils.actual_scene = utils.searchScene(saveobj["scene"])
	utils.player.x = saveobj["player"]["x"]
	utils.player.y = saveobj["player"]["y"]