---
title: url method
entry_name: url
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# url method

Makes the element require a valid url

## Description

Return true, if the value is a valid url. Works with text inputs.

## Examples

Makes "field" required and a url.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      url: true
    }
  }
});
```

```html
<label for="field">Required, URL: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
