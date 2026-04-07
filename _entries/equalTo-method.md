---
title: equalTo method
entry_name: equalTo
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# equalTo method

Requires the element to be the same as another one

## Description

Returns true if the value has the same value as the element specified by the first parameter.

## Usage

**other** *(Selector)*

The selector for the element to compare the current values

## Examples

Makes "field" required to be the same as #other

```javascript
$( "#myform" ).validate({
  rules: {
    password: "required",
    password_again: {
      equalTo: "#password"
    }
  }
});
```

```html
<label for="password">Password</label>
<input id="password" name="password" />
<br/>
<label for="password_again">Again</label>
<input class="left" id="password_again" name="password_again" />
<br>
<input type="submit" value="Validate!">
```
