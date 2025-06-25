# Dices REST API

Simple REST API that returns the results of dice rolls from a request. Made with Flask as my first project.

## Install & Run

```
git clone https://github.com/weedcat671/dices-rest-api-git
cd dices-rest-api
pip install -r requirements.txt
gunicorn main:app -b "0.0.0.0:8000"
```

## API Request/Response Example

Endpoint POST /roll:

JSON body for request:

```json
{
	"dices": [4, 8] // Array of dice sides
}
```

JSON body for response:

```json
{
	"results": [
		{"dice_sides": 4, "roll_result": 2},
		{"dice_sides": 8, "roll_result": 6}
	]
}
```

