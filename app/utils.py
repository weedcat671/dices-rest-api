from random import randint

def roll_dices(dices: list[int]) -> list[(int, int)]:
	for i in range(len(dices)):
		if type(dices[i]) is int and dices[i] > 1:
			dices[i] = (dices[i], randint(1, dices[i]))
		else:
			return None
	return dices

def make_roll_response(request_data: dict) -> (int, dict):
	if not "dices" in request_data:
		return 400, {"error": {"code": "MISSING_REQUIRED_DATA", "message": "Missing 'dices' field in request."}}
	if not type(request_data["dices"]) is list:
		return 400, {"error": {"code": "DATA_TYPE_MISMATCH", "message": "Invalid type of 'dices' field."}}

	rolled_dices = roll_dices(request_data["dices"])

	if rolled_dices is None:
		return 400, {"error": {"code": "VALIDATION_ERROR", "message": "Invalid data in 'dices' field."}}

	response_data = {"results": []}
	for dice in rolled_dices:
		response_data["results"].append({"dice_sides": dice[0], "roll_result": dice[1]})

	return 200, response_data