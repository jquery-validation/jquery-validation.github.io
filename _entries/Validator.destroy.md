---
title: Validator.destroy()
entry_name: Validator.destroy
entry_type: method
category: validator
layout: default
---

# Validator.destroy()

Destroys this instance of validator freeing up resources and unregistering events.

## Description

This is only useful, when you need to clean up after the validator in a Single Page Application.

## Usage


## Examples

Destroying an instance of validator.

```javascript
/*
 * On SPA page start.
 */
var validator = $( "#myform" ).validate();

/*
 * Just before SPA page's navigation away.
 */
validator.destroy();

/*
 * After this point the #myForm form is back to its original boring state.
 */
```
