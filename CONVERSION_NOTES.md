# XML to Markdown Conversion Notes

## Overview

The `entries/` directory contained 39 XML files that defined the API documentation for individual validation methods, selectors, and validator functions. These have been converted to Markdown format and moved to the `_entries/` directory for use with Jekyll.

## Conversion Process

1. **Script**: `convert_entries.py` - Python script that parses XML and generates Markdown
2. **Source**: `entries/*.xml` (39 files)
3. **Output**: `_entries/*.md` (39 files)

## Conversion Details

Each XML file was transformed as follows:

### Front Matter
- `title`: From `<title>` element
- `entry_name`: From `name` attribute of root `<entry>`
- `entry_type`: From `type` attribute (method, selector, validator)
- `return_type`: From `return` attribute (if present)
- `category`: From `<category slug="">` element
- `layout`: Set to "default"

### Content Structure
- **Title**: H1 heading from `<title>`
- **Sample**: For selectors, the selector syntax from `<sample>`
- **Description**: From `<desc>` element
- **Long Description**: From `<longdesc>` element (with HTML preserved as markdown)
- **Usage/Signatures**: From `<signature>` elements with nested arguments and properties
- **Examples**: From `<example>` elements with JavaScript and HTML code blocks

## Jekyll Configuration

The `_config.yml` has been configured to:
- Define `entries` as a collection
- Output entries with permalink pattern `/:name/`
- Apply the default layout to all entries
- Exclude the old `entries/` directory and conversion script from builds

## URL Mapping

With the permalink configuration, entries are accessible at:
- `/validate/` → `_entries/validate.md`
- `/required-method/` → `_entries/required-method.md`
- `/blank-selector/` → `_entries/blank-selector.md`
- etc.

This matches the link structure already present in `documentation.md`.

## Original XML Files

The original XML files in the `entries/` directory are:
- Excluded from Jekyll processing (in `_config.yml`)
- Kept for reference
- Can be removed once the conversion is verified in production

## Testing

To verify the conversion:
1. Check that all 39 entries are present in `_entries/`
2. Verify front matter is correct for each file
3. Ensure links in `documentation.md` resolve correctly
4. Test the GitHub Pages deployment

## Files Created/Modified

**Created:**
- `_entries/*.md` (39 files)
- `convert_entries.py`
- This file (`CONVERSION_NOTES.md`)

**Modified:**
- `_config.yml` - Updated collections, permalink, and excludes

**Preserved (for reference):**
- `entries/*.xml` (39 files) - Original XML sources
