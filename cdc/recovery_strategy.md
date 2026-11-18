# Recovery Strategy

If the load fails:

1. Watermark remains unchanged.
2. Failed batch is logged.
3. Pipeline retries automatically.
4. Next execution resumes from last successful watermark.