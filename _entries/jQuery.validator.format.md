---
title: jQuery.validator.format()
entry_name: jQuery.validator.format
entry_type: method
category: validator
layout: default
---

# jQuery.validator.format()

Replaces {n} placeholders with arguments.

## Description

One or more arguments can be passed, in addition to the string template itself, to insert into the string. If you're familiar with the term, this makes this function support currying. If you don't care about that, just use the first argument.

## Usage

**template** *(String)*
: The string to format.

**argument** *(Object)*
: The first argument to insert, or an array of Strings to insert

**argumentN...** *(Object)*
: The second etc. argument to insert

## Examples

Sets the debug setting for all validation calls.

```javascript
var template = jQuery.validator.format("{0} is not a valid value");
// later, results in 'abc is not a valid value'
alert(template("abc"));
```
