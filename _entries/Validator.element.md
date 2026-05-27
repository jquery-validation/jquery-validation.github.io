---
title: Validator.element()
entry_name: Validator.element
entry_type: method
category: validator
layout: default
permalink: /Validator.element/
---

# Validator.element()

Validates a single element, returns true if it is valid, false otherwise.

## Description

This behaves as validation on blur or keyup, but returns the result.

## Usage

### `Validator.element( element )`
{:.signature}

<div class="signature-body" markdown="1">

**element** *(Selector)*

An element to validate, must be inside the validated form.

</div>

## Examples

Triggers element validation programmatically.

```javascript
var validator = $( "#myform" ).validate();
validator.element( "#myselect" );
```
