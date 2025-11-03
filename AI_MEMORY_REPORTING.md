# 📋 AI Memory Reporting System

## Overview

Automated surveillance memory reporting system that SSH's 12-hour surveillance data to your local PC.

## Features

- ✅ Last 12 hours of surveillance data
- ✅ People detection counts per camera
- ✅ Detection timeline with timestamps
- ✅ System status (AI enabled/disabled)
- ✅ Camera activity breakdown
- ✅ JSON and Markdown formats

## Report Location

**Local Directory**: `/home/admin1/aimemory/`

**Files Created**:
- `surveillance_memory_report.md` - Human-readable report (latest)
- `surveillance_memory_report.json` - Machine-readable data (latest)
- `report_YYYYMMDD_HHMMSS.md` - Archived timestamped reports
- `report_YYYYMMDD_HHMMSS.json` - Archived timestamped data

## Usage

### Automated Script
```bash
cd surveillance-ai-system
./get_surveillance_memory.sh
```

This will:
1. SSH to surveillance server
2. Generate 12-hour memory report
3. Transfer reports to local directory
4. Archive with timestamp
5. Show summary

### Manual Fetch
```bash
# Generate report on server
sshpass -p 'password' ssh user@server 'python3 /tmp/generate_memory_report.py'

# Copy reports
scp user@server:/tmp/surveillance_memory_report.md ./aimemory/
scp user@server:/tmp/surveillance_memory_report.json ./aimemory/

# View report
cat ./aimemory/surveillance_memory_report.md
```

### Direct API Access
```bash
# Get events
curl http://server:8080/api/events | python3 -m json.tool

# Get statistics
curl http://server:8080/api/stats | python3 -m json.tool
```

## Report Contents

### System Status
- AI monitoring state
- Models loaded status
- Dashboard URLs

### Surveillance Summary
- Total detection events (last 12 hours)
- Total people detected
- Active cameras count
- Monitoring period

### Camera Activity
People detection count per camera

### Detection Timeline
Recent events with timestamps, camera ID, people count, and actions

## Automation

### Run Every Hour (Cron)
```bash
# Edit crontab
crontab -e

# Add line to run every hour:
0 * * * * /path/to/get_surveillance_memory.sh >> /path/to/fetch.log 2>&1
```

### Continuous Monitoring
```bash
# Watch for new events every 5 minutes
watch -n 300 './get_surveillance_memory.sh'
```

## Troubleshooting

**SSH Connection Issues**:
```bash
ping server-ip
ssh user@server 'echo Connected'
```

**No Events Reported**:
```bash
# Check AI status
curl http://server:8080/api/ai/status

# Enable AI
curl -X POST http://server:8080/api/ai/enable
```

**Disk Space Management**:
```bash
# Clean old reports (30+ days)
find ./aimemory/ -name "report_*.json" -mtime +30 -delete
```

---

*Memory reporting system ready! Run `./get_surveillance_memory.sh` anytime.*