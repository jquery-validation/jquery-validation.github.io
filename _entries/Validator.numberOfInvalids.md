---
title: Validator.numberOfInvalids()
entry_name: Validator.numberOfInvalids
entry_type: method
category: validator
layout: default
permalink: /Validator.numberOfInvalids/
---

# Validator.numberOfInvalids()

Returns the number of invalid fields.

## Description

This depends on the internal validator state. It covers all fields only after validating the complete form (on submit or via $("form").valid()). After validating a single element, only that element is counted. Most useful in combination with the invalidHandler-option.

## Usage

### `Validator.numberOfInvalids()`
{:.signature}

<div class="signature-body" markdown="1">

This signature does not accept any arguments.

</div>

## Examples

Displays a summary of invalid fields after an invalid submit.

```javascript
var validator = $( "#myform" ).validate({
  invalidHandler: function() {
    $( "#summary" ).text( validator.numberOfInvalids() + " field(s) are invalid" );
  }
});
```
