#!/bin/bash
# Automated surveillance memory report fetcher
# Run this anytime to get the last 12 hours of surveillance data

echo "🎬 Fetching surveillance memory from surveillance server..."
echo ""

# Configure these variables for your setup
SERVER_USER="your_username"
SERVER_HOST="your_server_ip"
REPORT_DIR="./aimemory"

# Create report directory if it doesn't exist
mkdir -p "$REPORT_DIR"

# Generate report on remote server
echo "Generating report on server..."
ssh "${SERVER_USER}@${SERVER_HOST}" 'python3 /tmp/generate_memory_report.py'

echo ""
echo "📥 Transferring reports to ${REPORT_DIR}/..."

# Copy reports back
scp -q "${SERVER_USER}@${SERVER_HOST}:/tmp/surveillance_memory_report.json" "${REPORT_DIR}/"
scp -q "${SERVER_USER}@${SERVER_HOST}:/tmp/surveillance_memory_report.md" "${REPORT_DIR}/"

# Add timestamp to filename
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
cp "${REPORT_DIR}/surveillance_memory_report.json" "${REPORT_DIR}/report_${TIMESTAMP}.json"
cp "${REPORT_DIR}/surveillance_memory_report.md" "${REPORT_DIR}/report_${TIMESTAMP}.md"

echo "✅ Reports saved:"
echo "   - ${REPORT_DIR}/surveillance_memory_report.md (latest)"
echo "   - ${REPORT_DIR}/surveillance_memory_report.json (latest)"
echo "   - ${REPORT_DIR}/report_${TIMESTAMP}.md (archived)"
echo "   - ${REPORT_DIR}/report_${TIMESTAMP}.json (archived)"
echo ""
echo "📊 View the report:"
echo "   cat ${REPORT_DIR}/surveillance_memory_report.md"
echo ""