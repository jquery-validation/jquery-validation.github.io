---
title: dateISO method
entry_name: dateISO
entry_type: method
return_type: Boolean
category: methods
layout: default
permalink: /dateISO-method/
---

# dateISO method

Makes the element require an ISO date.

## Description

Return true if the value is a valid date according to ISO date standard. Works with text inputs.

## Examples

Makes "field" required and an ISO date.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      dateISO: true
    }
  }
});
```

```html
<label for="field">Required, dateISO: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
