html_substr = (str, start, length) ->
  countTags = 0
  returnString = ""
  writeLetters = 0
  until ((writeLetters >= length) and (countTags is 0))
    letter = str.charAt(start + writeLetters)
    countTags++  if letter is "<"
    countTags--  if letter is ">"
    returnString += letter
    writeLetters++
  returnString

Ember.Handlebars.helper "if_even", (number) ->
  if (number % 2) is 0
    "even"
  else
    "odd"

Ember.Handlebars.helper "trim", (body) ->
  trimmedBody = html_substr(body, 0, 450)
  new Handlebars.SafeString(trimmedBody)
