---
title: range method
entry_name: range
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# range method

Makes the element require a given value range.

## Description

Works with text inputs. To exclude the maximum value, subtract Number.MIN_VALUE from that value. To exclude the minimum value, add Number.MIN_VALUE to that value.

## Usage

### `range( range )`
{:.signature}

<div class="signature-body" markdown="1">

**range** *(Array)*

Value range required

</div>

## Examples

Makes "field" required and between 13 and 23.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      range: [13, 23]
    }
  }
});
```

```html
<label for="field">Required, minimum 13, maximum 23:</label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
