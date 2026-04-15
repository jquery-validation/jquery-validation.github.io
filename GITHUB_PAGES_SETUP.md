# GitHub Pages Setup Instructions

This document explains how to enable GitHub Pages for this repository.

## Automatic Deployment

The repository is configured to automatically deploy to GitHub Pages using GitHub Actions. The workflow is defined in `.github/workflows/deploy-pages.yml`.

**Jekyll Version:** This site uses Jekyll 4.x, which is automatically handled by the GitHub Actions workflow.

## Enabling GitHub Pages

To enable GitHub Pages for this repository, a repository administrator needs to:

1. Go to the repository **Settings** page
2. Navigate to **Pages** in the left sidebar
3. Under **Build and deployment**:
   - **Source**: Select "GitHub Actions"
4. Save the changes

## After Enabling

Once GitHub Pages is enabled:

1. The workflow will automatically run when changes are pushed to `main` or `master` branch
2. You can also manually trigger the workflow from the **Actions** tab
3. The site will be available at: `https://jquery-validation.github.io/validation-content/`
   - Or at your custom domain if configured

## Testing the Deployment

After enabling GitHub Pages and pushing changes:

1. Go to the **Actions** tab in the repository
2. You should see the "Deploy to GitHub Pages" workflow running
3. Once complete, visit the deployed site URL
4. Verify that the content displays correctly

## Troubleshooting

If the deployment fails:

1. Check the workflow logs in the **Actions** tab
2. Verify that GitHub Pages is enabled with "GitHub Actions" as the source
3. Ensure the branch being deployed (main or master) exists and has the latest changes
4. Check that all required files are present: `_config.yml`, `_layouts/default.html`, and content files

## Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to the repository root with your domain name
2. Configure your DNS settings to point to GitHub Pages
3. Enable HTTPS in the Pages settings (recommended)

For more information, see: https://docs.github.com/en/pages
