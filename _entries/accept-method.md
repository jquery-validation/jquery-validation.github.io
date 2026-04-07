---
title: accept method
entry_name: accept
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# accept method

Makes a file upload accept only specified mime-types.

## Description

Uses the HTML5 file API to look at the type attribute of one or more selected files and validate that each matches the specified mime-type. If nothing is specified, only images are allowed (image/*). You can specify multiple mime-types by separating them with a comma, e.g. "image/x-eps,application/pdf". Works with type="file" inputs. Part of the additional-methods.js file Note: This method used to look at just the filename, specifically the file extension. That behaviour is now available as the "extension" method inside src/additional/extension.js.

## Usage

**mimetype** *(String)*
: The allowed type, seperated via ",", defaults to "image/*"

## Examples

Required, only audio files allowed:

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true,
      accept: "audio/*"
    }
  }
});
```

```html
<label for="field">Required, audio files only: </label>
<input type="file" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```
