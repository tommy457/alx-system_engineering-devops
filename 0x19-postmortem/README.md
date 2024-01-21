**Issue Summary:**
- Duration: From 4:00 AM to 4:03 AM (GMT+00).
- Impact: 100% down, the application server went down.
- Root Cause: typo in some file extension.

**Timeline:**
- Issue detected: At 4:00 AM, engineer noticed something on Datadog monitoring that requests went down exponentially
- Actions Taken: using strace to debug the problem
- Resolution: the problem was fixed almost instantly.

**Root Cause and Resolution:**
- Cause: the root cause of the problem was a typo in an file extension that was pushed recently adding another p to the .php.
- Resolution: the problem was fixed almost instantly, using strace showed that some file are
not present following the trail of bread croms provied by the starce command the issue was fixed.

**Corrective and Preventative Measures:**
- Improvements: the issue was an honest mistake by our new junior developer.
