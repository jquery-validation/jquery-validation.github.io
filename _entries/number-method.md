---
title: number method
entry_name: number
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# number method

Makes the element require a decimal number.

## Description

Returns true if the value contains a valid decimal number. Works with text inputs.

## Examples

Makes "field" required and a decimal number only.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      number: true
    }
  }
});
```

```html
<label for="field">Required, decimal number: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
