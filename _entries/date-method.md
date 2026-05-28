---
title: "[DEPRECATED] date method"
entry_name: date
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# [DEPRECATED] date method

Makes the element require a date.

## Description

Return true if the value is a valid date. Uses JavaScript's built-in Date to test if the date is valid, and therefore does no sanity checks. Only the format must be valid, not the actual date, eg 30/30/2008 is a valid date. DEPRECATION warning: This method is deprecated and will be removed in version 2.0.0.Please don't use it, since it relies on the Date constructor, which behaves very differently across browsers and locales. Use dateISO instead or one of the locale specific methods (in localizations/ and additional-methods.js).

## Examples

Makes "field" required and a date.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      date: true
    }
  }
});
```

```html
<label for="field">Required, date: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
