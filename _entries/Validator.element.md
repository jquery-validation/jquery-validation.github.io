---
title: Validator.element()
entry_name: Validator.element
entry_type: method
category: validator
layout: default
---

# Validator.element()

Validates a single element, returns true if it is valid, false otherwise.

## Description

This behaves as validation on blur or keyup, but returns the result.

## Usage

**element** *(Selector)*

An element to validate, must be inside the validated form.

## Examples

Triggers element validation programmatically.

```javascript
var validator = $( "#myform" ).validate();
validator.element( "#myselect" );
```
