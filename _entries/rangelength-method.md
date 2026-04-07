---
title: rangelength method
entry_name: rangelength
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# rangelength method

Makes the element require a given value range.

## Description

Return false if the element is some kind of text input and its length is too short or too long a set of checkboxes that doesn't have enough, or has too many boxes checked a select that doesn't have enough, or has too many options selected Works with text inputs, selects and checkboxes.

## Usage

**range** *(Array)*

Value range required

## Examples

Makes "field" required and between 2 and 6 characters long.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      rangelength: [2, 6]
    }
  }
});
```

```html
<label for="field">Required, minimum length 2, maximum length 6: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
