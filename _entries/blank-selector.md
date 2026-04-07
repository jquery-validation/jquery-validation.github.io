---
title: :blank Selector
entry_name: blank
entry_type: selector
category: selectors
layout: default
---

# :blank Selector

**Selector:** `:blank`

Selects all elements with a blank value.

## Description

Blank means either no value at all or only whitespace. The implementation does a check like this: `jQuery.trim(value).length == 0`

## Usage


## Examples

Finds input elements with no value or just whitespace.

```javascript
$( "input:blank" ).css( "background-color", "#bbbbff" );
```

```html
<div>Mouseover to see the value of each input</div>
<input value="" title='""'>
<input value="   " title='"   "'>
<input value="abc" title='"abc"'>
```
