---
title: step method
entry_name: step
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# step method

Makes the element require a given step.

## Description

Works with text inputs. No support for input types: date, datetime, datetime-local, month, time and week.

## Usage

### `step( value )`
{:.signature}

<div class="signature-body" markdown="1">

**value** *(Number)*

Step value required

</div>

## Examples

Makes "field" required and step of 10.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      step: 10
    }
  }
});
```

```html
<label for="field">Required, step 10: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
