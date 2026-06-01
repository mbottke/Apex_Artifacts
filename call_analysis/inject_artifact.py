"""Inject the schedule data JSON into the calendar artifact template -> standalone HTML."""
import json, sys
B='/home/user/Apex_Artifacts/call_analysis/'
which=sys.argv[1] if len(sys.argv)>1 else 'rebuilt'
out=sys.argv[2] if len(sys.argv)>2 else 'deliverables/26-27_Call_Calendar_apex.html'
tpl=open(B+'calendar_artifact_template.html').read()
data=open(B+f'artifact_data_{which}.json').read()
data=data.replace('</','<\\/')  # guard against </script> breaking the inline block
assert '/*__DATA__*/' in tpl, "placeholder missing"
html=tpl.replace('/*__DATA__*/',data)
open('/home/user/Apex_Artifacts/'+out,'w').write(html)
print(f"wrote {out}  ({len(html)//1024} KB)")
