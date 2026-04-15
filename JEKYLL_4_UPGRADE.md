# Jekyll 4 Upgrade Notes

## Summary

This repository has been updated from Jekyll 3.9 to Jekyll 4.3.

## Changes Made

### 1. Gemfile Updates
- **Jekyll**: Updated from `~> 3.9` to `~> 4.3`
- **webrick**: Added `~> 1.8` (required for Jekyll 4 on Ruby 3.0+)
- **jekyll-feed**: Updated from `~> 0.12` to `~> 0.17`

### 2. Configuration Updates (_config.yml)
Added explicit kramdown configuration for Jekyll 4:
```yaml
kramdown:
  input: GFM
  syntax_highlighter: rouge
```

### 3. Documentation Updates
- Updated README.md to specify Ruby 2.7+ requirement
- Updated GITHUB_PAGES_SETUP.md to note Jekyll 4 usage

## Key Differences in Jekyll 4

### Breaking Changes Addressed
1. **Kramdown Settings**: Jekyll 4 requires explicit configuration for kramdown input format and syntax highlighter
2. **Ruby Version**: Jekyll 4 requires Ruby 2.7.0 or higher
3. **Webrick**: No longer bundled with Ruby 3.0+, must be added as a dependency

### Compatibility
- All existing content and layouts are compatible with Jekyll 4
- GitHub Actions workflow (`actions/jekyll-build-pages@v1`) automatically uses the latest Jekyll version
- No changes needed to existing markdown files or layouts

## Testing Locally

To test the site with Jekyll 4:

```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Access at http://localhost:4000/validation-content/
```

## Deployment

The GitHub Actions workflow will automatically use Jekyll 4 when building and deploying the site. No changes to the workflow were necessary as it automatically detects the Jekyll version from the Gemfile.

## Rollback (if needed)

To rollback to Jekyll 3, simply revert the Gemfile to:
```ruby
gem "jekyll", "~> 3.9"
# Remove webrick line
gem "jekyll-feed", "~> 0.12"
```

And remove the kramdown configuration from _config.yml.
