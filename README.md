# Brunch with Ember Reloaded

## Getting started

Before using brunch-with-bootsraped-ember-reloaded-bower you will need to install [Brunch](http://brunch.io/).

```
brunch new gh:nenros/brunch-with-bootsraped-ember-reloaded-bower myappp
cd myapp
brunch w -s
```
Open [http://localhost:3333](http://localhost:3333) on your browser.

## Generators

This skeleton makes use of [scaffolt](https://github.com/paulmillr/scaffolt#readme) generators to help you create common files quicker. To use first install scaffolt globally with `npm install -g scaffolt`. Then you can use the following command to generate files.

```
scaffolt model <name>             →    app/models/Name.coffee
scaffolt view <name>              →    app/views/NameView.coffee
scaffolt controller <name>        →    app/controllers/NameController.coffee
scaffolt arraycontroller <name>   →    app/controllers/NamesController.coffee
scaffolt route <name>             →    app/routes/NameRoute.coffee
scaffolt template <name>          →    app/templatesname.hbs
scaffolt component <name>         →    app/components/NameComponent.coffee
                                       app/templates/components/name.hbs
```

There are more commands you can do with scaffolt and also instruction on how to create your own generators, so make sure you check out the [docs](https://github.com/paulmillr/scaffolt#readme).

## Testing

To run you will need [Karma](https://github.com/karma-runner) you will need to install [phantomjs](https://github.com/ariya/phantomjs). If you want to run your tests on other browsers consult the Karma docs.

```
brew update && brew install phantomjs
```

To run tests continiously as you write code and tests (for now) you must open two terminal windows.

```
brunch watch -s
```

```
karma start
```

## Building for production
This skeleton supports the production versions of ember and ember-data. Just build using the --production flags.

```
brunch build --production
```

You can also have modules load only when you are on a specific environment (production / development). Just add the modules you want loaded to the corresponging subdirectory of the `envs` top level directory. All modules will be imported by the module `'config/env'`.

```js
var myEnvVars = require('config/env');
myEnvVars.envFileName.property;
```


## License

All of brunch-with-ember-reloaded is licensed under the MIT license.

Copyright (c) 2013 Bartosz Markowski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
