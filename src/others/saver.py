import utils
import json

def save(fname="../saves/save.json"):
	f = open(fname, "w")
	
	saveobj = {}
	saveobj["world_ticks"] = utils.play_state.world_ticks
	saveobj["scene"] = utils.play_state.actual_scene.id
	saveobj["player"] = {}
	saveobj["player"]["x"] = utils.play_state.player.x
	saveobj["player"]["y"] = utils.play_state.player.y
	saveobj["player"]["mpixel"] = utils.play_state.player.moving_pixel
	f.write(json.dumps(saveobj))



def restore(fname="../saves/save.json"):
	f = open(fname, "r")
	
	saveobj = json.loads(f.read())
	utils.play_state.world_ticks = saveobj["world_ticks"]
	utils.play_state.actual_scene = utils.searchScene(saveobj["scene"])
	utils.play_state.player.x = saveobj["player"]["x"]
	utils.play_state.player.y = saveobj["player"]["y"]
	utils.play_state.player.moving_pixel = saveobj["player"]["mpixel"]