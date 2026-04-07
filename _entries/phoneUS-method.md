---
title: phoneUS method
entry_name: phoneUS
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# phoneUS method

Validate for valid US phone number.

## Description

Works with text inputs. Part of the additional-methods.js file

## Examples

Makes "field" required and a US phone number.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      phoneUS: true
    }
  }
});
```

```html
<label for="field">Required, us phone number: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
