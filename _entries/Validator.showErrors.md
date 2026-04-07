---
title: Validator.showErrors()
entry_name: Validator.showErrors
entry_type: method
category: validator
layout: default
---

# Validator.showErrors()

Show the specified messages.

## Description

Keys have to refer to the names of elements, values are displayed for those elements, using the configured error placement.

## Usage

**errors** *(Object)*
: One or more key/value pairs of input names and messages.

## Examples

Adds and shows error message programmatically.

```javascript
var validator = $( "#myshowErrors" ).validate();
validator.showErrors({
	"firstname": "I know that your firstname is Pete, Pete!"
});
```
