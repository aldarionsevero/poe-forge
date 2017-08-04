# Electron + Polymer Starter Kit
A copy of [Polymer Starter Kit](https://github.com/PolymerElements/polymer-starter-kit/), running inside [Electron](https://github.com/atom/electron).

```bash
# Clone
$ git clone https://github.com/aldarionsevero/poe-forge
$ cd poe-forge

# Install the dependencies and run
$ npm install && bower install && npm start
# Ctrl-C to stop
$ npm start # to run


To serve as web app in the browser:

Make a directory for global installations:

$ mkdir ~/.npm-global

Configure npm to use the new directory path:

$npm config set prefix '~/.npm-global'

Open or create a ~/.bashrc file and add this line:

export PATH=~/.npm-global/bin:$PATH

Back on the command line, update your system variables:

source ~/.bashrc

Install polymer and bower globaly
$ npm i -g bower polymer-cli
$ ./polymer-serve.sh
```

# Run the API locally

```Bash
$ pip install -r requeriments.txt
$ python api.py
```

## Versions
- Polymer: 1.2.0
- Polymer Starter Kit: 1.2.1
- Electron: 0.36.0
