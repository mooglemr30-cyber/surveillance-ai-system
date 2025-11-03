# 📊 24-Hour Event Analysis & Customer Insights

Automated daily analysis of customer interactions with actionable business recommendations.

## Overview

**Schedule**: Daily at 11:59 PM  
**Purpose**: Analyze 24 hours of surveillance events and generate business insights  
**Output**: JSON reports with recommendations

## What Gets Analyzed

- **Customer Traffic**: Total people, hourly patterns, peak vs quiet hours
- **Camera Performance**: Activity distribution, coverage effectiveness
- **Customer Behavior**: Actions detected, dwell patterns, engagement
- **Business Insights**: Staffing needs, operational opportunities

## Report Example

```json
{
  "timestamp": "2025-11-03T23:59:00",
  "summary": {
    "total_events": 247,
    "total_people": 389,
    "active_cameras": 16,
    "avg_people_per_event": 1.57
  },
  "peak_hours": [
    [14, 67],  // 2 PM: 67 people
    [11, 52],  // 11 AM: 52 people
    [16, 48]   // 4 PM: 48 people
  ],
  "recommendations": [
    {
      "priority": "HIGH",
      "category": "Staffing",
      "issue": "Peak hours: 14:00, 11:00, 16:00",
      "recommendation": "Ensure adequate staffing during peak",
      "action": "Schedule staff for peak hours"
    }
  ]
}
```

## Recommendation Priorities

- 🔴 **HIGH**: Immediate action (staffing, system issues)
- 🟠 **MEDIUM**: Important improvements (coverage, operations)
- 🟢 **LOW**: Nice to have (monitoring, optimization)
- 🔵 **INFO**: Informational insights (behavior, trends)

## Using Reports

**View Latest Report**:
```bash
ssh pearce@192.168.1.29 'cat /home/pearce/surveillance_dashboard/reports/analysis_*.json | tail -1'
```

**Run Manual Analysis**:
```bash
ssh pearce@192.168.1.29
cd /home/pearce/surveillance_dashboard
./venv/bin/python3 analyze_24h_events.py
```

**Download Reports**:
```bash
scp pearce@192.168.1.29:/home/pearce/surveillance_dashboard/reports/*.json ~/reports/
```

## Configuration

**Cron Schedule** (11:59 PM daily):
```bash
59 23 * * * /home/pearce/surveillance_dashboard/venv/bin/python3 \
  /home/pearce/surveillance_dashboard/analyze_24h_events.py
```

**Modify Schedule**:
```bash
crontab -e
# Examples:
# Every 12 hours: 0 */12 * * *
# Twice daily: 0 8,20 * * *
```

## Actionable Insights

### Staffing Optimization
- Review peak hour recommendations
- Adjust schedules for following week
- Track service quality improvements

### Layout Optimization
- Identify high-traffic areas
- Analyze browsing patterns
- Test layout changes

### Coverage Improvements
- Study successful camera placements
- Identify under-covered areas
- Balance coverage

## Best Practices

**Daily Review**:
1. Check report at 9 AM
2. Note HIGH priority items
3. Compare weekly trends
4. Plan monthly strategic reviews

**Data Retention**:
- Keep 90 days of reports
- Archive quarterly summaries
- Document actions taken

**Continuous Improvement**:
1. Test recommendations
2. Measure impact
3. Iterate and refine
4. Update criteria

## Troubleshooting

**No Events**:
```bash
# Check AI enabled
curl http://192.168.1.29:8080/api/stats | grep ai_enabled

# Check events file
tail -f /home/pearce/surveillance_dashboard/knowledge_base/events.json
```

**Script Issues**:
```bash
# Verify cron
crontab -l | grep analyze

# Check logs
tail -100 /home/pearce/surveillance_dashboard/reports/analysis.log

# Test manually
cd /home/pearce/surveillance_dashboard && ./analyze_24h_events.py
```

## Summary

✅ Automated daily at 11:59 PM  
✅ Customer traffic analysis  
✅ Business recommendations  
✅ Peak hour identification  
✅ Coverage optimization  
✅ Behavior insights  
✅ JSON format for integration

**Reports**: `/home/pearce/surveillance_dashboard/reports/`  
**Script**: `/home/pearce/surveillance_dashboard/analyze_24h_events.py`  
**Status**: ✅ Operational
