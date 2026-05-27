---
title: jQuery.validator.addClassRules()
entry_name: jQuery.validator.addClassRules
entry_type: method
category: validator
layout: default
permalink: /jQuery.validator.addClassRules/
---

# jQuery.validator.addClassRules()

Add a compound class method - useful to refactor common combinations of rules into a single class.

## Usage

### `jQuery.validator.addClassRules( name, rules )`
{:.signature}

<div class="signature-body" markdown="1">

**name** *(String)*

The name of the class rule to add

**rules** *(Object)*

The compound rules (see example)

</div>

### `jQuery.validator.addClassRules( rules )`
{:.signature}

<div class="signature-body" markdown="1">

**rules** *(Object)*

A map of className-rules pairs (see example).

</div>

## Examples

### Example 1

Add a new compound rule called "name", replacing class="required" minlength="2" with class="name".

```javascript
jQuery.validator.addClassRules("name", {
  required: true,
  minlength: 2
});
```

### Example 2

Add two compound class rules for name and zip.

```javascript
jQuery.validator.addClassRules({
  name: {
    required: true,
    minlength: 2
  },
  zip: {
    required: true,
    digits: true,
    minlength: 5,
    maxlength: 5
  }
});
```
