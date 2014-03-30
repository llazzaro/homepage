exports.config =
    files:
      javascripts:
        joinTo:
          'js/app.js': /^(app)/
          'js/vendor.js' :  /^(vendor|bower_components)/
        pluginHelpers: 'js/app.js'

      stylesheets:
        joinTo:
          'css/vendor.css': /^(vendor|bower_components)/
          'css/app.css': /^(app)/
#            order:
#                before: [
#                    "bower_components/bootstrap/dist/css/bootstrap.css",
#                ]

      templates:
        precompile: true
        root: 'templates'
        joinTo:
          'js/app.js': /^app/

    plugins:
        #        autoReload:
        #    enabled:
        #        js: on
        #        css: on
        #        assets: off

      imageoptimizer:
        path: 'images'
        smushit: no

        coffeelint:
          pattern: /^app\/.*\.coffee$/

          options:
            indentation:
              value: 4
              level: "error"

            max_line_length:
              value: 80
              level: "error"

    conventions:
      assets: /(assets|font)/
