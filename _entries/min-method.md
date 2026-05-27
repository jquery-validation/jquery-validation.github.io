---
title: min method
entry_name: min
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# min method

Makes the element require a given minimum.

## Description

Works with text inputs. To exclude the minimum value, add Number.MIN_VALUE to that value.

## Usage

### `min( value )`
{:.signature}

<div class="signature-body" markdown="1">

**value** *(Number)*

Minimum value required

</div>

## Examples

Makes "field" required and 13 or larger.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      min: 13
    }
  }
});
```

```html
<label for="field">Required, minimum 13: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
