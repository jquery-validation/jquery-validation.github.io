---
title: digits method
entry_name: digits
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# digits method

Makes the element require digits only.

## Description

Returns true if the value contains only digits. Works with text inputs.

## Examples

Makes "field" required and digits only.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      digits: true
    }
  }
});
```

```html
<label for="field">Required, digits: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
