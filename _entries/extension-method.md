---
title: extension method
entry_name: extension
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# extension method

Makes the element require a certain file extension.

## Description

Returns true if the value ends with one of the specified file extensions. If nothing is specified, only images are allowed (png, jpeg, gif). Works with text inputs. Part of the additional-methods.js file

## Usage

**extension** *(String)* (optional)

The allowed file extensions, seperated with "|" (or a comma, ","), defaults to "png|jpe?g|gif".

## Examples

Makes "field" required and ending with ".xls" or ".csv".

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      extension: "xls|csv"
    }
  }
});
```

```html
<label for="field">Required, only .xls and .csv files allowed: </label>
<input type="file" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
