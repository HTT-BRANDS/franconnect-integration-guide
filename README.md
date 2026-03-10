# FranConnect Integration Guide

Password-protected setup guide for the HubSpot → FranConnect lead relay integration.

**Hosted at:** [GitHub Pages URL will appear here after deployment]

## For Team Members
Visit the GitHub Pages URL and enter the shared team password to access the guide.

## Updating the Guide
1. Edit `guide-redesigned.html` (the source file)
2. Re-encrypt: `staticrypt guide-redesigned.html -p "YOUR_PASSWORD" --template-title "HTT Brands — FranConnect Setup Guide" --template-instructions "Enter the team password to access the setup guide." --template-button "Open Guide" --template-color-primary "#0d7b70" --template-color-secondary "#1a1a2e" --remember 30 -d .`
3. Rename output: `mv guide-redesigned.html.encrypted index.html` (or however staticrypt outputs it)
4. Commit and push
