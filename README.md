# Unslave
Unslave is a Modbus RTU/TCP slave emulator focused on ease of use 
and configuration.

## Configuring Unslave
Open `config.json` in any text (code) editor and 
adjust settings according to you requrements.

The default config file has some example settings to get you started.
It also has comments explaining how to change the settings.

To change logging settings, open `logger.json`.

To edit .json files it's better to use a code editor - less error prone.
Visual Studio Code or Notepad++ are good options, but there are many more.

## Usage
Run `unslave.exe` and leave it open.
If there aren't any errors in the console, you are good to go.

## HTTP API
As of version 3.0, unslave provides an HTTP API to update configuration at runtime.

Before using the API, make sure to enable it in `config.json` and specify `port` value:
	
	"api":{
		"enabled":true,
		"port":9000
	},
	...

During the first API run the application will likely ask for network access permission.

See examples of API calls below:

### Set Register Value

	PUT /slaves/1/registers/C100

	content-type:application/json

	{
		"value": true
	}

### Set Exception Response

	PUT /slaves/1/registers/C100

	content-type:application/json

	{
		"exception": 2
	}

### Set Slave Online

	PUT /slaves/1

	content-type:application/json

	{
		"isOnline": true
	}


In all API call you can use either PUT or POST to achieve the same result.

Note that any updates made via the API are temporary - they are not actually saved to `config.json`.

Visit https://unserver.xyz to learn more.

## Please Share and Give Feedback
Send your feedback or bug reports to info@unserver.xyz

