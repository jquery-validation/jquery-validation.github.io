---
title: Validator.numberOfInvalids()
entry_name: Validator.numberOfInvalids
entry_type: method
category: validator
layout: default
---

# Validator.numberOfInvalids()

Returns the number of invalid fields.

## Description

This depends on the internal validator state. It covers all fields only after validating the complete form (on submit or via $("form").valid()). After validating a single element, only that element is counted. Most useful in combination with the invalidHandler-option.

## Usage

**errors** *(Object)*
: One or more key/value pairs of input names and messages.

## Examples

Displays a summary of invalid fields after an invalid submit.

```javascript
var validator = $( "#myform" ).validate({
  invalidHandler: function() {
    $( "#summary" ).text( validator.numberOfInvalids() + " field(s) are invalid" );
  }
});
```
