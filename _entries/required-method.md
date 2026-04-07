---
title: required method
entry_name: required
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# required method

Makes the element required.

## Description

Return false, if the element is empty (text input) or unchecked (radio/checkbox) or if nothing is selected (select). Works with text inputs, selects, checkboxes and radio buttons. To force a user to select an option from a select box, provide an empty option element like <option value="">Choose...</option> Note that white spaces are considered valid.

## Usage

### Form 1

The element is always required.

### Form 2

Makes the element required, depending on the result of the given expression.

**dependency-expression** *(String)*

An expression (String) that is evaluated in the context of the element's form, making the field required only if the expression returns more than one element. Very often your expression will use selector filters such as `#foo:checked`, `#foo:filled`, `#foo:visible`. This plugin provides [custom selectors for that purpose](/category/selectors/).

### Form 3

Makes the element required, depending on the result of the given callback.

**dependency-callback** *(Function)*

The function is executed with the element as it's only argument: If it returns true, the element is required.

## Examples

### Example 1

Makes "field" always required.

```javascript
$( "#myform" ).validate({
  rules: {
    field: {
      required: true
    }
  }
});
```

```html
<label for="field">Required: </label>
<input type="text" class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```

### Example 2

Makes the fruit select required.

```javascript
$( "#myform" ).validate({
  rules: {
    fruit: {
      required: true
    }
  }
});
```

```html
<label for="fruit">Please select a fruit</label>
<select id="fruit" name="fruit" title="Please select something!">
	<option value="">Select...</option>
	<option value="1">Banana</option>
	<option value="2">Apple</option>
	<option value="3">Peach</option>
</select>
<br/>
<input type="submit" value="Validate!">
```

### Example 3

Makes the gender radio buttons required.

```javascript
$( "#myform" ).validate({
  rules: {
    gender: {
      required: true
    }
  }
});
```

```html
<label for="gender_male">
  <input  type="radio" id="gender_male" value="m" name="gender" />
  Male
</label>
<label for="gender_female">
  <input  type="radio" id="gender_female" value="f" name="gender"/>
  Female
</label>
<label for="gender" class="error">Please select your gender</label>
<br/>
<input type="submit" value="Validate!">
```

### Example 4

Makes the agree checkbox required.

```javascript
$( "#myform" ).validate({
  rules: {
    agree: {
      required: true
    }
  }
});
```

```html
<label for="agree">Please agree to our policy</label>
<input type="checkbox" id="agree" title="Please agree to our policy!" name="agree" />
<br/>
<input type="submit" value="Validate!">
```

### Example 5

Makes details required only if #other is checked.

```javascript
$( "#myform" ).validate({
  rules: {
    details: {
      required: "#other:checked"
    }
  }
});
```

```html
<label for="other">Check to make next field required</label>
<input id="other" type="checkbox">
<br>
<input id="details" name="details">
<br>
<input type="submit" value="Validate!">
```

### Example 6

Makes "parent" required only if age is below 13.

```javascript
$( "#myform" ).validate({
  rules: {
    age: {
      required: true,
      min: 3
    },
    parent: {
      required: function(element) {
        return $("#age").val() < 13;
      }
    }
  }
});
```

```html
<label>Age </label>
<input id="age" name="age">
<br>
<label>Parent </label>
<input id="parent" name="parent">
<br>
<input type="submit" value="Validate!">
```
