#!/bin/bash

# Script to generate the OpenAPI client for LangWatch API.
# This script:
# 1. Generates the OpenAPI client using openapi-python-client
# 2. Adds generated code markers and headers
# 3. Updates documentation
# 4. Installs the generated client

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Configuration
OPENAPI_SPEC_PATH="https://github.com/langwatch/langwatch/blob/main/langwatch/src/app/api/openapiLangWatch.json"
GENERATED_DIR="scenario/_generated"
CLIENT_DIR="${GENERATED_DIR}/langwatch_api_client"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${BLUE}🔧 $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

run_command() {
    local description="$1"
    local cmd="$2"

    log_info "$description"
    if ! eval "$cmd"; then
        log_error "Failed: $description"
        exit 1
    fi
}

create_generated_marker() {
    log_info "Adding generated code markers..."

    cat > "${GENERATED_DIR}/.generated" << EOF
# This directory contains auto-generated code from openapi-python-client
# DO NOT EDIT FILES IN THIS DIRECTORY MANUALLY
#
# To regenerate:
# make generate-openapi-client
#
# Generated from: ${OPENAPI_SPEC_PATH}
# Generator: openapi-python-client
# Generated on: $(date)
EOF
}

add_generated_header() {
    local file_path="$1"
    local temp_file="${file_path}.tmp"

    cat > "$temp_file" << EOF
# AUTO-GENERATED CODE - DO NOT EDIT MANUALLY
# Generated by openapi-python-client from ${OPENAPI_SPEC_PATH}
#
# To regenerate: make generate-openapi-client

EOF

    cat "$file_path" >> "$temp_file"
    mv "$temp_file" "$file_path"
}

update_readme() {
    local readme_path="$1"
    local temp_file="${readme_path}.tmp"

    log_info "Updating README with generated code notice..."

    cat > "$temp_file" << 'EOF'
# lang-watch-api-client
**⚠️ AUTO-GENERATED CODE - DO NOT EDIT MANUALLY ⚠️**

This is an auto-generated client library for accessing LangWatch API, created using `openapi-python-client`.

## Regeneration
To regenerate this client:
```bash
make generate-openapi-client
```

## Source
Generated from: `../langwatch-saas/langwatch/langwatch/src/app/api/openapiLangWatch.json`

---

EOF

    # Append original content (skip first line)
    tail -n +2 "$readme_path" >> "$temp_file" 2>/dev/null || true
    mv "$temp_file" "$readme_path"
}

main() {
    echo "🚀 Starting OpenAPI client generation..."

    # Check if OpenAPI spec exists
    if [[ ! -f "$OPENAPI_SPEC_PATH" ]]; then
        log_error "OpenAPI spec not found at: $OPENAPI_SPEC_PATH"
        echo "Please ensure the langwatch-saas repository is available at the expected location."
        exit 1
    fi

    # Create generated directory
    mkdir -p "$GENERATED_DIR"

    # Generate the client
    run_command "Generating OpenAPI client" \
        "openapi-python-client generate --path $OPENAPI_SPEC_PATH --output-path $CLIENT_DIR --overwrite"

    # Add generated markers
    create_generated_marker

    # Add generated headers to key files
    local init_file="${CLIENT_DIR}/lang_watch_api_client/__init__.py"
    if [[ -f "$init_file" ]]; then
        add_generated_header "$init_file"
    fi

    # Update README
    local readme_file="${CLIENT_DIR}/README.md"
    if [[ -f "$readme_file" ]]; then
        update_readme "$readme_file"
    fi

    # Install the generated client
    run_command "Installing generated client" \
        "uv pip install -e $CLIENT_DIR"

    log_success "OpenAPI client generated and installed!"
    log_warning "Remember: Generated code should not be edited manually"
    echo "📁 Generated client location: $CLIENT_DIR/"
}

# Run main function
main "$@"