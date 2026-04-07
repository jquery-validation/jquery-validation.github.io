---
title: jQuery.validator.addMethod()
entry_name: jQuery.validator.addMethod
entry_type: method
category: validator
layout: default
---

# jQuery.validator.addMethod()

Add a custom validation method. It must consist of a name (must be a legal javascript identifier), a javascript based function and a default string message.

## Description

For simple one-off validation, you can use the bundled `pattern` method (in additional methods, source in `src/additional/pattern.js`) to validate a field against a regular expression. In general, it is a good idea to encapsulate those regular expressions inside their own method. If you need lots of slightly different expressions, try to extract a common parameter. See also a [library of regular expressions](http://regexlib.com/DisplayPatterns.aspx).

## Usage

**name** *(String)*
: The name of the method used to identify it and referencing it; this must be a valid JavaScript identifier

**method** *(Function)*
: The actual method implementation, returning true if an element is valid. First argument: Current value. Second argument: Validated element. Third argument: Parameters.

  - **value** *(String)*: the current value of the validated element
  - **element** *(Element)*: the element to be validated
  - **params** *(Object)*: parameters specified for the method, e.g. for min: 5, the parameter is 5, for range: [1, 5] it's [1, 5]

**message** *(String)* (optional)
: The default message to display for this method. Can be a function created by ''jQuery.validator.format(value)''. When undefined, an existing message is used (handy for localization), otherwise the field-specific messages have to be defined.

## Examples

### Example 1

Add a validation method that checks if a value starts with a certain domain.

```javascript
jQuery.validator.addMethod("domain", function(value, element) {
  return this.optional(element) || /^http:\/\/mycorporatedomain.com/.test(value);
}, "Please specify the correct domain for your documents");
```

### Example 2

Adds a validation method that checks if a given value equals the addition of the two parameters.

```javascript
jQuery.validator.addMethod("math", function(value, element, params) {
  return this.optional(element) || value == params[0] + params[1];
}, jQuery.validator.format("Please enter the correct value for {0} + {1}"));
```

### Example 3

Adds a custom email validation method that is less strict than the one built-in.

```javascript
jQuery.validator.addMethod("laxEmail", function(value, element) {
  // allow any non-whitespace characters as the host part
  return this.optional( element ) || /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@(?:\S{1,63})$/.test( value );
}, 'Please enter a valid email address.');
```
