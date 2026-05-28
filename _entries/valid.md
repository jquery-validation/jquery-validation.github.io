---
title: .valid()
entry_name: valid
entry_type: method
return_type: Boolean
category: plugin
layout: default
---

# .valid()

Checks whether the selected form is valid or whether all selected elements are valid.

## Description

[validate()](/validate) needs to be called on the form before checking it using this method.

## Usage

### `.valid()`
{:.signature}

<div class="signature-body" markdown="1">

This signature does not accept any arguments.

</div>

## Examples

Sets up validation for a form, then checks if the form is valid when clicking a button.

```javascript
var form = $( "#myform" );
form.validate();
$( "button" ).click(function() {
	alert( "Valid: " + form.valid() );
});
```

```html
<form id="myform">
	<input type="text" name="name" required>
	<br>
	<button type="button">Validate!</button>
</form>
```
