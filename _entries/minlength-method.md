---
title: minlength method
entry_name: minlength
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# minlength method

Makes the element require a given minimum length.

## Description

Return false if the element is some kind of text input and its value is too short a set of checkboxes that doesn't have enough boxes checked a select and doesn't have enough options selected Works with text inputs, selects and checkboxes.

## Usage

### `minlength( length )`
{:.signature}

<div class="signature-body" markdown="1">

**length** *(Number)*

Minimum number of characters required

</div>

## Examples

Makes "field" required having at least 3 characters.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      minlength: 3
    }
  }
});
```

```html
<label for="field">Required, minimum length 3: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
