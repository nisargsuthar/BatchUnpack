### Step 1:

> Use Detect It Easy to recursively scan your malware directory and save the results. Use deep scan to compare with normal scan results.
> Append to your malware executable corresponding strings of the packer used. (_upx, _nspack, _aspack etc.)
---

### Step 2:
Run the script from the root of your malware directory.

---

### Note:
> Currently I could only make the unpacking work via the command line for UPX packed malware. If you find the relevant one liners for other packers please open a PR.