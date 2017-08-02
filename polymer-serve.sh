rm -rf polymer-serve
mkdir polymer-serve
cp -R bower_components/ polymer-serve/
cp bower.json polymer-serve/
cp -R app/elements polymer-serve/
cp -R app/images polymer-serve/
cp app/index.html polymer-serve/
cp app/manifest.json polymer-serve/
cp -R app/scripts polymer-serve/
cp -R app/styles polymer-serve/
cd polymer-serve/
polymer serve --open
