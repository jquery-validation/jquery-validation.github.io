---
title: maxlength method
entry_name: maxlength
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# maxlength method

Makes the element require a given maximum length.

## Description

Return false if the element is some kind of text input and its value is too long a set of checkboxes that has too many boxes checked a select and has too many options selected Works with text inputs, selects and checkboxes.

## Usage

**length** *(Number)*

Maximum number of characters required

## Examples

Makes "field" required having at most 4 characters.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      maxlength: 4
    }
  }
});
```

```html
<label for="field">Required, maximum length 4: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
