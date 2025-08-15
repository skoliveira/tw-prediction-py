# GSI SETUP

This guide will walk you through the process of setting up Game State Integration (GSI) for Dota 2.

### Step 1: Create the file `gamestate_integration_prediction.cfg`

```
"Dota 2 Integration Configuration"
				{
					"uri"          "http://localhost:2322/"
					"timeout"       "5.0"
					"buffer"        "1.0"
					"throttle"      "1.0"
					"heartbeat"     "5.0"
					"data"
					{
						"buildings"     "1"
						"provider"      "1"
						"map"           "1"
						"player"        "1"
						"hero"          "1"
						"abilities"     "1"
						"items"         "1"
						"draft"         "1"
					}
				}
```

### Step 2: Place this file into your Dota 2 installation directory

The file path should look like this:

`...\dota 2 beta\game\dota\cfg\gamestate_integration\gamestate_integration_prediction.cfg`

**Note:** You might have to create the `gamestate_integration` folder if it doesn't already exist.

### Step 3: Add `-gamestateintegration` to your Dota 2 launch options

[Click here to see how to add launch options](https://dotatooltips.b-cdn.net/assets/dota2tooltips_gsi_launch_option.png)

### Step 4: Restart Dota 2

Restart Dota 2, and you're done! Now, viewers can choose predictions.
