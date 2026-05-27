---
title: Validator.form()
entry_name: Validator.form
entry_type: method
category: validator
layout: default
permalink: /Validator.form/
---

# Validator.form()

Validates the form, returns true if it is valid, false otherwise.

## Description

This behaves as a normal submit event, but returns the result.

## Usage

### `Validator.form()`
{:.signature}

<div class="signature-body" markdown="1">

This signature does not accept any arguments.

</div>

## Examples

Triggers form validation programmatically.

```javascript
var validator = $( "#myform" ).validate();
validator.form();
```
