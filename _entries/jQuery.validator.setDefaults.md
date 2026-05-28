---
title: jQuery.validator.setDefaults()
entry_name: jQuery.validator.setDefaults
entry_type: method
category: validator
layout: default
permalink: /jQuery.validator.setDefaults/
---

# jQuery.validator.setDefaults()

Modify default settings for validation.

## Description

Accepts everything that [validate()](/validate) accepts.

## Usage

### `jQuery.validator.setDefaults( options )`
{:.signature}

<div class="signature-body" markdown="1">

**options** *(Object)*

Options to set as default.

</div>

## Examples

Sets the debug setting for all validation calls.

```javascript
jQuery.validator.setDefaults({
	debug: true
});
```
