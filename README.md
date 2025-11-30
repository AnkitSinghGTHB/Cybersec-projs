# Cybersec projs

28 cybersec projects

Security Engineering 🏗️ (code)

1. File integrity checker (detect modified files via hashes)
2. Secure password generator with strength meter
3. Log redaction tool to remove secrets/PII
4. Basic encrypted notes vault (AES + passphrase)
5. Simple network port scanner + service banner grabber
6. JWT verifier CLI (expiry + signature validation)
7. Config security checker (weak ciphers / hard-coded creds flags)

Threat Detection 🔍

8. Suspicious process detector (monitor CPU/memory spikes)
9. Basic network anomaly script (alert on unusual ports/IPs)
10. Failed login monitor + alerting
11. DNS monitoring tool (flag suspicious domains)
12. K8s audit log flagger for privilege escalation attempts
13. Simple phishing URL checker (regex + known bad patterns)
14. Basic file reputation checker (hash → offline known-bad list)

Incident Response 🚑

15. Log bundler tool (collect logs into one archive)
16. Memory snapshot script for triage
17. System information collector (OS, users, services, open ports)
18. Evidence tagging tool (hash files + timestamp)
19. Email phishing reporting script (extract headers + artefacts)
20. IR notebook template generator (timeline + notes)
21. K8s pod snapshot + metadata collector

Security Architecture 📊 (design)

22. Basic zero-trust network diagram + baseline configs
23. Secure Kubernetes baseline (RBAC, namespaces, network policies)
24. Cloud least-privilege IAM policy template
25. Secrets management pattern (Vault/KMS + short-lived creds)
26. TLS-everywhere blueprint (internal + external services)
27. Logging + monitoring pipeline (SIEM-ready)
28. IaC folder structure + policy baseline (Terraform security module)
