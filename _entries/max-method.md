---
title: max method
entry_name: max
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# max method

Makes the element require a given maximum.

## Description

Works with text inputs. To exclude the maximum value, subtract Number.MIN_VALUE from that value.

## Usage

**value** *(Number)*

Maximum value required

## Examples

Makes "field" required and 23 or smaller.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      max: 23
    }
  }
});
```

```html
<label for="field">Required, maximum value 23: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
