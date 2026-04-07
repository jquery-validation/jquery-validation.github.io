---
title: .rules()
entry_name: rules
entry_type: method
return_type: Object
category: plugin
layout: default
---

# .rules()

Read, add and remove rules for an element.

## Description

Returns the validations rules for the first selected element or Adds the specified rules and returns all rules for the first matched element. Requires that the parent form is validated, that is, $( "form" ).validate() is called first or Removes the specified rules and returns all rules for the first matched element. There are several ways to specify validation rules. Validation methods with parameters can be specified as attributes (recommended) Validation methods without parameters can be specified as classes on the element Both can be specified using the rules-option of the validate()-method Both rules and messages can be specified using data attributes, using data-msg (a generic, not-method specific message), data-msg-[method] and data-rule-[method]. When setting, the rules can also contain a messages-object, specifying custom messages for existing or added rules.

## Usage

### Form 1

Read rules for the first element

### Form 2

Add rules

**"add"** *(String)*

**rules** *(Object)*
: The rules to add. Accepts the same format as the rules-option of the validate-method.

### Form 3

Remove rules

**"remove"** *(String)*

**rules** *(Object)*
: The space-seperated names of rules to remove and return. If left unspecified, removes and returns all rules. Manipulates only rules specified via rules-option or via rules("add").

## Examples

### Example 1

Adds minlength: 2 to an element which is already required.

```javascript
$( "#myinput" ).rules( "add", {
	minlength: 2
});
```

### Example 2

Adds required and minlength: 2 to an element and specifies custom messages for both.

```javascript
$( "#myinput" ).rules( "add", {
	required: true,
	minlength: 2,
	messages: {
		required: "Required input",
		minlength: jQuery.validator.format("Please, at least {0} characters are necessary")
	}
});
```

### Example 3

Removes all static rules from an element.

```javascript
$( "#myinput" ).rules( "remove" );
```

### Example 4

Removes min and max rules from an element.

```javascript
$( "#myinput" ).rules( "remove", "min max" );
```
