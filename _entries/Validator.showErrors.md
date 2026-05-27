---
title: Validator.showErrors()
entry_name: Validator.showErrors
entry_type: method
category: validator
layout: default
permalink: /Validator.showErrors/
---

# Validator.showErrors()

Show the specified messages.

## Description

Keys have to refer to the names of elements, values are displayed for those elements, using the configured error placement.

## Usage

### `Validator.showErrors( errors )`
{:.signature}

<div class="signature-body" markdown="1">

**errors** *(Object)*

One or more key/value pairs of input names and messages.

</div>

## Examples

Adds and shows error message programmatically.

```javascript
var validator = $( "#myshowErrors" ).validate();
validator.showErrors({
	"firstname": "I know that your firstname is Pete, Pete!"
});
```
