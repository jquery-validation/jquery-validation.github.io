---
title: Validator.resetForm()
entry_name: Validator.resetForm
entry_type: method
category: validator
layout: default
permalink: /Validator.resetForm/
---

# Validator.resetForm()

Resets the controlled form.

## Description

Resets input fields to their original value (requires form plugin), removes classes indicating invalid elements and hides error messages.

## Usage

### `Validator.resetForm()`
{:.signature}

<div class="signature-body" markdown="1">

This signature does not accept any arguments.

</div>

## Examples

Reset the form controlled by this validator.

```javascript
var validator = $( "#myform" ).validate();
validator.resetForm();
```
