#!/usr/bin/env python3
"""
Convert XML entry files to Markdown format for Jekyll.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def clean_text(text):
    """Clean and normalize text content."""
    if not text:
        return ""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    return text


def convert_html_entities(text):
    """Convert common HTML entities."""
    if not text:
        return ""
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    return text


def extract_text_with_html(elem):
    """Extract text and HTML content from an element, preserving structure."""
    if elem is None:
        return ""
    
    # Get all text including from children
    parts = []
    if elem.text:
        parts.append(elem.text)
    
    for child in elem:
        # Handle special elements
        if child.tag == 'code':
            code_text = ''.join(child.itertext())
            parts.append(f'`{code_text}`')
        elif child.tag == 'p':
            p_text = extract_text_with_html(child)
            parts.append(f'\n\n{p_text}')
        elif child.tag == 'a':
            link_text = ''.join(child.itertext())
            href = child.get('href', '')
            parts.append(f'[{link_text}]({href})')
        else:
            parts.append(''.join(child.itertext()))
        
        if child.tail:
            parts.append(child.tail)
    
    return ''.join(parts)


def parse_signature(sig_elem):
    """Parse a signature element and return markdown."""
    lines = []
    
    # Get description if present
    desc_elem = sig_elem.find('desc')
    if desc_elem is not None:
        desc_text = extract_text_with_html(desc_elem)
        if desc_text:
            lines.append(clean_text(desc_text))
            lines.append("")
    
    # Get arguments
    for arg in sig_elem.findall('argument'):
        arg_name = arg.get('name', 'argument')
        arg_type = arg.get('type', 'Any')
        optional = arg.get('optional', 'false') == 'true'
        
        arg_desc_elem = arg.find('desc')
        arg_desc = ""
        if arg_desc_elem is not None:
            arg_desc = extract_text_with_html(arg_desc_elem)
        
        opt_str = " (optional)" if optional else ""
        lines.append(f"**{arg_name}** *({arg_type})*{opt_str}")
        if arg_desc:
            lines.append(f": {clean_text(arg_desc)}")
        lines.append("")
        
        # Handle nested properties
        for prop in arg.findall('property'):
            prop_name = prop.get('name', 'property')
            prop_type = prop.get('type', 'Any')
            prop_desc_elem = prop.find('desc')
            prop_desc = ""
            if prop_desc_elem is not None:
                prop_desc = extract_text_with_html(prop_desc_elem)
            
            lines.append(f"  - **{prop_name}** *({prop_type})*: {clean_text(prop_desc)}")
        
        if arg.findall('property'):
            lines.append("")
    
    return '\n'.join(lines)


def parse_example(example_elem):
    """Parse an example element and return markdown."""
    lines = []
    
    # Get description
    desc_elem = example_elem.find('desc')
    if desc_elem is not None:
        desc_text = extract_text_with_html(desc_elem)
        if desc_text:
            lines.append(clean_text(desc_text))
            lines.append("")
    
    # Get code
    code_elem = example_elem.find('code')
    if code_elem is not None:
        code_text = code_elem.text or ""
        # Handle CDATA
        if code_text:
            lines.append("```javascript")
            lines.append(code_text.strip())
            lines.append("```")
            lines.append("")
    
    # Get HTML
    html_elem = example_elem.find('html')
    if html_elem is not None:
        html_text = html_elem.text or ""
        if html_text:
            lines.append("```html")
            lines.append(html_text.strip())
            lines.append("```")
            lines.append("")
    
    return '\n'.join(lines)


def convert_xml_to_markdown(xml_path):
    """Convert an XML entry file to Markdown format."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Extract metadata
    entry_name = root.get('name', '')
    entry_type = root.get('type', 'method')
    return_type = root.get('return', '')
    
    # Extract title
    title_elem = root.find('title')
    title = title_elem.text if title_elem is not None else entry_name
    
    # Extract description
    desc_elem = root.find('desc')
    desc = extract_text_with_html(desc_elem) if desc_elem is not None else ""
    
    # Extract long description
    longdesc_elem = root.find('longdesc')
    longdesc = extract_text_with_html(longdesc_elem) if longdesc_elem is not None else ""
    
    # Extract sample (for selectors)
    sample_elem = root.find('sample')
    sample = sample_elem.text if sample_elem is not None else ""
    
    # Extract category
    category_elem = root.find('category')
    category = category_elem.get('slug', 'methods') if category_elem is not None else 'methods'
    
    # Start building markdown
    lines = []
    
    # Front matter
    lines.append("---")
    lines.append(f"title: {title}")
    lines.append(f"entry_name: {entry_name}")
    lines.append(f"entry_type: {entry_type}")
    if return_type:
        lines.append(f"return_type: {return_type}")
    lines.append(f"category: {category}")
    lines.append("layout: default")
    lines.append("---")
    lines.append("")
    
    # Title
    lines.append(f"# {title}")
    lines.append("")
    
    # Sample (for selectors)
    if sample:
        lines.append(f"**Selector:** `{sample}`")
        lines.append("")
    
    # Description
    if desc:
        lines.append(clean_text(desc))
        lines.append("")
    
    # Long description
    if longdesc:
        lines.append("## Description")
        lines.append("")
        lines.append(clean_text(longdesc))
        lines.append("")
    
    # Signatures
    signatures = root.findall('signature')
    if signatures:
        if len(signatures) == 1:
            lines.append("## Usage")
            lines.append("")
            lines.append(parse_signature(signatures[0]))
        else:
            lines.append("## Usage")
            lines.append("")
            for i, sig in enumerate(signatures, 1):
                if len(signatures) > 1:
                    lines.append(f"### Form {i}")
                    lines.append("")
                lines.append(parse_signature(sig))
    
    # Examples
    examples = root.findall('example')
    if examples:
        lines.append("## Examples")
        lines.append("")
        for i, example in enumerate(examples, 1):
            if len(examples) > 1:
                lines.append(f"### Example {i}")
                lines.append("")
            lines.append(parse_example(example))
    
    return '\n'.join(lines)


def main():
    """Main conversion function."""
    entries_dir = Path('/home/runner/work/validation-content/validation-content/entries')
    output_dir = Path('/home/runner/work/validation-content/validation-content/_entries')
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Convert each XML file
    xml_files = sorted(entries_dir.glob('*.xml'))
    print(f"Found {len(xml_files)} XML files to convert")
    
    for xml_file in xml_files:
        print(f"Converting {xml_file.name}...")
        try:
            markdown_content = convert_xml_to_markdown(xml_file)
            
            # Create output filename
            output_file = output_dir / xml_file.with_suffix('.md').name
            
            # Write markdown file
            output_file.write_text(markdown_content)
            print(f"  -> {output_file.name}")
        except Exception as e:
            print(f"  ERROR: {e}")
    
    print(f"\nConversion complete! {len(xml_files)} files converted to {output_dir}")


if __name__ == '__main__':
    main()
