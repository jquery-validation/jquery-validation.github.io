---
title: email method
entry_name: email
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# email method

Makes the element require a valid email

## Description

Return true if the value is a valid email address. Works with text inputs. IMPORTANT NOTE: As of version 1.12.0 we started using the same regular expression that the HTML5 specification suggests for browsers to use. We will follow their lead and use the same check. In case you need to adjust the built-in validation regular expression patterns, please use the $.validator.methods property. If you have different requirements, please consider using a custom method.

## Examples

Makes "field" required and an email address.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      email: true
    }
  }
});
```

```html
<label for="field">Required, email: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
