---
title: creditcard method
entry_name: creditcard
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# creditcard method

Makes the element require a credit card number.

## Description

Return true if the value is a valid credit card number. Works with text inputs. Part of the additional-methods.js file Note: The algorithm used can't verify the validity of the number - it is just an integrity check. As with any other clientside validation, you have to implement the same or better validation on the serverside.

## Examples

Makes "field" required and credit card only.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      creditcard: true
    }
  }
});
```

```html
<label for="field">Required, creditcard (try 446-667-651): </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
