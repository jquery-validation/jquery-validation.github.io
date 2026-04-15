# jQuery Validation Plugin - Content Repository

This repository contains the documentation and content for the [jQuery Validation Plugin](https://github.com/jquery-validation/jquery-validation) website.

## GitHub Pages Deployment

This site is automatically deployed to GitHub Pages using Jekyll.

### How it Works

- Content is written in Markdown with Jekyll front matter
- The site is built using Jekyll (configured in `_config.yml`)
- GitHub Actions automatically builds and deploys the site when changes are pushed to the `main` or `master` branch
- The workflow is defined in `.github/workflows/deploy-pages.yml`

### Local Development

To test the site locally:

1. Install Ruby 2.7 or higher and Bundler:
   ```bash
   gem install bundler
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Run Jekyll locally:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser to `http://localhost:4000/validation-content/`

**Note:** This site uses Jekyll 4.x. If you encounter issues, ensure you have Ruby 2.7 or higher installed.

### Making Changes

1. Edit or create Markdown files (`.md`) in the root directory
2. Each file should have Jekyll front matter at the top:
   ```yaml
   ---
   layout: default
   title: Your Page Title
   ---
   ```
3. Commit and push your changes
4. GitHub Actions will automatically build and deploy the site

### Content Structure

- `index.md` - Home page
- `documentation.md` - API documentation
- `contribute.md` - Contribution guide
- `reference.md` - General guidelines and reference
- `_entries/` - Markdown documentation entries (for API methods, converted from XML)
- `_layouts/` - Jekyll layout templates

### Deployment

The site is automatically deployed via GitHub Actions when:
- Changes are pushed to `main` or `master` branch
- The workflow can also be triggered manually from the Actions tab

No manual deployment is required!
